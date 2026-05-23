#!/usr/bin/env python3
"""
Rebuild Claude-Code-101 PDF with:
  - Fixed cover page (fits A4, no overflow)
  - TOC with internal hyperlinks
  - Source attribution footer on every lesson
Also patches source attribution into both HTML files.
"""

import re, subprocess, os, sys

ROOT      = "/Users/ding/Documents/claude/200_Reference/past-work/course-notes/claude-code/101/output"
SRC_HTML  = f"{ROOT}/_dev/Claude-Code-101-notes.html"
ELEC_HTML = f"{ROOT}/index.html"
PDF_OUT   = f"{ROOT}/handouts/Claude-Code-101-notes.pdf"
CHROME    = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PLAYLIST  = "https://youtube.com/playlist?list=PLmWCw1CzcFilebjK89WLb5cAvM8K0cLB3&si=6K86NWePoZl9vmu5"

SOURCE_FOOTER = f"""
<footer class="source-footer">
  資料來源：整理自 <a href="{PLAYLIST}" target="_blank">Claude 官方 YouTube 課程</a>
</footer>"""

FOOTER_CSS = """
.source-footer {
  margin-top: 48px;
  padding: 16px 0 8px;
  border-top: 1px solid #e5e7eb;
  font-size: 12px;
  color: #888;
  text-align: center;
}
.source-footer a { color: #d97706; text-decoration: none; }
.source-footer a:hover { text-decoration: underline; }
"""

# ── 1. patch both HTML files ────────────────────────────────────────────────

def patch_html(path):
    with open(path, encoding="utf-8") as f:
        html = f.read()

    # skip if already patched
    if 'source-footer' in html:
        print(f"  already patched: {os.path.basename(path)}")
        return

    # inject CSS before </style>
    html = html.replace("</style>", FOOTER_CSS + "</style>", 1)

    # inject footer before </main>
    html = html.replace("</main>", SOURCE_FOOTER + "\n</main>", 1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  patched: {os.path.basename(path)}")

print("Step 1 — patching HTML files...")
patch_html(SRC_HTML)
patch_html(ELEC_HTML)

# ── 2. extract lesson sections from the combined HTML ──────────────────────

print("Step 2 — extracting lesson sections...")

with open(SRC_HTML, encoding="utf-8") as f:
    raw = f.read()

# lesson meta: (id, en_title, zh_title, yt_url)
LESSONS = [
    ("lesson01", "What is Claude Code?",                  "什麼是 Claude Code？",       "https://www.youtube.com/watch?v=fl1DSmwQKKY"),
    ("lesson02", "Installing Claude Code",                "安裝 Claude Code",            "https://www.youtube.com/watch?v=0kILa02vKuI"),
    ("lesson03", "How Claude Code Works",                 "Claude Code 如何運作",        "https://www.youtube.com/watch?v=6bs5b4FltCU"),
    ("lesson04", "Your First Prompt",                     "你的第一個 Prompt",           "https://www.youtube.com/watch?v=gbetp6D7J_Q"),
    ("lesson05", "The CLAUDE.md File",                    "CLAUDE.md 設定檔",            "https://www.youtube.com/watch?v=O0FGCxkHM-U"),
    ("lesson06", "Explore → Plan → Code → Commit",        "探索→計畫→程式設計→提交",     "https://www.youtube.com/watch?v=xJQuF02NAK8"),
    ("lesson07", "Context Management",                    "情境視窗管理",                "https://www.youtube.com/watch?v=eW3oTyfeWZ0"),
    ("lesson08", "MCP",                                   "整合外部工具",                "https://www.youtube.com/watch?v=kkBFmwkDzdo"),
    ("lesson09", "Hooks in Claude Code",                  "確定性自動化",                "https://www.youtube.com/watch?v=IkaPHiMDazM"),
]

# extract each <section class="lesson" id="lessonXX"> ... </section>
def extract_section(html, lid):
    pat = rf'(<section class="lesson" id="{lid}">.*?</section>)'
    m = re.search(pat, html, re.DOTALL)
    return m.group(1) if m else ""

lesson_sections = []
for lid, en, zh, yt in LESSONS:
    sec = extract_section(raw, lid)
    # replace video thumbnail block with a pdf-friendly link block
    sec = re.sub(
        r'<a href="[^"]*" target="_blank" class="video-link">.*?</a>',
        f'<div class="pdf-video-link">▶ <a href="{yt}">前往 YouTube 觀看影片</a></div>',
        sec, flags=re.DOTALL
    )
    # inject "回目錄" button after lesson-tag span
    sec = re.sub(
        r'(<span class="lesson-tag">Lesson \d+</span>)',
        r'<div class="lesson-top">\1<a href="#toc" class="back-btn">↑ 回目錄</a></div>',
        sec
    )
    lesson_sections.append((lid, en, zh, sec))

# ── inject source attribution inside last lesson's notes-section ────────────
_source_html = (
    f'\n  <div class="pdf-source">'
    f'資料來源：整理自 <a href="{PLAYLIST}">Claude Youtube 官方頻道課程 Claude-Code-101</a>'
    f'</div>'
)
_lid, _en, _zh, _sec = lesson_sections[-1]
_last_div = _sec.rfind('</div>')
_sec = _sec[:_last_div] + _source_html + '\n  ' + _sec[_last_div:]
lesson_sections[-1] = (_lid, _en, _zh, _sec)

# ── 3. build PDF source HTML ───────────────────────────────────────────────

print("Step 3 — building PDF source HTML...")

# extract body CSS from combined HTML (everything inside <style>...</style>)
css_m = re.search(r'<style>(.*?)</style>', raw, re.DOTALL)
body_css = css_m.group(1) if css_m else ""

# remove sidebar / layout CSS we don't need
body_css = re.sub(r'/\* ── Layout[^}]*\}', '', body_css, flags=re.DOTALL)
body_css = re.sub(r'/\* ── Sidebar[^/]*/\*[^}]*\}', '', body_css, flags=re.DOTALL)
body_css = re.sub(r'\.sidebar\b[^{]*\{[^}]*\}', '', body_css, flags=re.DOTALL)
body_css = re.sub(r'\.sidebar-header\b[^{]*\{[^}]*\}', '', body_css, flags=re.DOTALL)
body_css = re.sub(r'\.nav-[a-z]+\b[^{]*\{[^}]*\}', '', body_css, flags=re.DOTALL)
body_css = re.sub(r'\.layout\b[^{]*\{[^}]*\}', '', body_css, flags=re.DOTALL)
body_css = re.sub(r'\.main\b[^{]*\{[^}]*\}', '', body_css, flags=re.DOTALL)

toc_items = "\n".join(
    f'    <li><a href="#{lid}"><span class="toc-num">0{i+1}</span>{en}<span class="toc-zh">{zh}</span></a></li>'
    for i, (lid, en, zh, _) in enumerate(lesson_sections)
)

lesson_html = "\n\n".join(sec for _, _, _, sec in lesson_sections)

pdf_html = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<title>Claude Code 101 — 學習筆記</title>
<style>
/* ── Page Setup ── */
@page {{
  size: A4;
  margin: 16mm 18mm;
}}

/* ── Reset ── */
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans TC", sans-serif;
  background: #fff;
  color: #1a1a1a;
  font-size: 13.5px;
  line-height: 1.75;
}}

/* ── Cover Page ── */
.cover {{
  height: 265mm;          /* A4 - top/bottom margins (16mm×2) */
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  background: #1a1a1a;
  color: #fff;
  border-radius: 6px;
  padding: 32px;
  overflow: hidden;
  break-after: page;
  page-break-after: always;
}}
.cover-tag {{
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: #d97706;
  background: rgba(217,119,6,.15);
  padding: 4px 14px;
  border-radius: 99px;
  margin-bottom: 24px;
}}
.cover h1 {{
  font-size: 36px;
  font-weight: 900;
  color: #fff;
  letter-spacing: -0.01em;
  margin-bottom: 10px;
  line-height: 1.2;
  border: none;
  padding: 0;
}}
.cover-sub {{
  font-size: 16px;
  color: #aaa;
  margin-bottom: 36px;
  font-weight: 400;
}}
.cover-divider {{
  width: 48px;
  height: 3px;
  background: #d97706;
  border-radius: 2px;
  margin: 0 auto 32px;
}}
.cover-desc {{
  font-size: 13px;
  color: #888;
  line-height: 1.8;
  max-width: 420px;
}}
.cover-source {{
  margin-top: 36px;
  font-size: 11px;
  color: #555;
}}
.cover-source a {{
  color: #d97706;
  text-decoration: none;
}}

/* ── TOC Page ── */
.toc-page {{
  break-after: page;
  page-break-after: always;
}}
.toc-page h2 {{
  font-size: 22px;
  font-weight: 800;
  color: #111;
  margin-bottom: 28px;
  padding-bottom: 10px;
  border-bottom: 3px solid #d97706;
  display: block;
  letter-spacing: normal;
  text-transform: none;
}}
.toc-page h2::before {{ display: none; }}
.toc-list {{
  list-style: none;
  padding: 0;
}}
.toc-list li {{
  margin-bottom: 0;
  border-bottom: 1px solid #f0f0ee;
}}
.toc-list a {{
  display: flex;
  align-items: baseline;
  gap: 12px;
  padding: 10px 4px;
  color: #1a1a1a;
  text-decoration: none;
  font-size: 14px;
  font-weight: 600;
}}
.toc-list a:hover {{ color: #d97706; }}
.toc-num {{
  font-size: 11px;
  font-weight: 700;
  color: #d97706;
  min-width: 24px;
  font-family: "SF Mono", monospace;
}}
.toc-zh {{
  font-size: 12px;
  font-weight: 400;
  color: #888;
  margin-left: 6px;
}}

/* ── PDF Video Link ── */
.pdf-video-link {{
  background: #fffbeb;
  border: 1px solid #fde68a;
  border-left: 3px solid #d97706;
  border-radius: 6px;
  padding: 9px 14px;
  font-size: 12.5px;
  margin: 10px 0 18px;
  color: #92400e;
  break-inside: avoid;
  page-break-inside: avoid;
}}
.pdf-video-link a {{ color: #b45309; word-break: break-all; }}

/* ── Lesson Section ── */
.lesson {{
  margin-bottom: 0;
  padding-bottom: 0;
  border-bottom: none;
}}

/* ── Resource List ── */
.resource-list {{ list-style: none; padding: 0; }}
.resource-list li {{ padding: 9px 0; border-bottom: 1px solid #fde68a; }}
.resource-list li:last-child {{ border-bottom: none; padding-bottom: 0; }}
.resource-list a {{ font-weight: 700; color: #92400e; font-size: 13px; text-decoration: none; }}
.resource-desc {{ font-size: 12px; color: #666; margin-top: 3px; line-height: 1.5; }}

/* ── Back-to-TOC button ── */
.lesson-top {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 10px;
}}
.back-btn {{
  font-size: 11px;
  font-weight: 600;
  color: #b45309;
  background: #fef3c7;
  border: 1px solid #fde68a;
  border-radius: 99px;
  padding: 3px 12px;
  text-decoration: none;
  white-space: nowrap;
  flex-shrink: 0;
}}

/* ── Source Footer ── */
.pdf-source {{
  margin-top: 20px;
  padding: 10px 0 4px;
  border-top: 1px solid #e5e7eb;
  font-size: 11px;
  color: #aaa;
  text-align: center;
}}
.pdf-source a {{ color: #d97706; text-decoration: none; }}

/* ── Inherited styles ── */
{body_css}

/* ── No-split pagination ── */
table, thead, tbody, tr,
pre,
.example-box, .tip-box, .key-rule, .cta-box,
.workflow, .cmd-cards, .scope-cards, .exit-codes,
.pdf-video-link,
.notes-section,
figure, img {{
  break-inside: avoid;
  page-break-inside: avoid;
}}
h1, h2, h3 {{
  break-after: avoid;
  page-break-after: avoid;
  orphans: 4; widows: 4;
}}
h2 + p, h2 + ol, h2 + ul, h2 + table, h2 + pre,
h2 + .example-box, h2 + .tip-box, h2 + .cta-box,
h2 + .workflow, h2 + .cmd-cards, h2 + .scope-cards,
h3 + p, h3 + ol, h3 + ul, h3 + table, h3 + pre {{
  break-before: avoid;
  page-break-before: avoid;
}}
li {{
  break-inside: avoid;
  page-break-inside: avoid;
}}
.lesson {{
  break-before: page;
  page-break-before: always;
}}
</style>
</head>
<body>

<!-- ══ COVER ══ -->
<div class="cover">
  <div class="cover-tag">Claude Code 101</div>
  <h1>Claude Code 101</h1>
  <div class="cover-sub">學習筆記</div>
  <div class="cover-divider"></div>
  <div class="cover-desc">
    9 堂課帶你從零認識 Claude Code<br>
    從安裝到進階工作流，從 CLAUDE.md 到 Hooks<br>
    一份筆記，完整掌握
  </div>
  <div class="cover-source">
    資料來源：整理自 <a href="{PLAYLIST}">Claude Youtube 官方頻道課程 Claude-Code-101</a>
  </div>
</div>

<!-- ══ TOC ══ -->
<div class="toc-page" id="toc">
  <h2>目錄 Contents</h2>
  <ul class="toc-list">
{toc_items}
  </ul>
</div>

<!-- ══ LESSONS ══ -->
{lesson_html}

</body>
</html>"""

pdf_src = f"{ROOT}/_dev/_pdf_src.html"
with open(pdf_src, "w", encoding="utf-8") as f:
    f.write(pdf_html)
print(f"  PDF source written ({len(pdf_html):,} chars)")

# ── 4. generate PDF ────────────────────────────────────────────────────────

print("Step 4 — generating PDF with Chrome headless...")
cmd = [
    CHROME,
    "--headless=new",
    "--no-sandbox",
    "--disable-gpu",
    "--run-all-compositor-stages-before-draw",
    "--no-pdf-header-footer",
    f"--print-to-pdf={PDF_OUT}",
    f"file://{pdf_src}",
]
result = subprocess.run(cmd, capture_output=True, text=True)
if result.returncode != 0:
    print("Chrome stderr:", result.stderr[:500])
    sys.exit(1)

os.remove(pdf_src)
size_kb = os.path.getsize(PDF_OUT) // 1024
print(f"  PDF saved: {PDF_OUT} ({size_kb} KB)")
print("Done.")
