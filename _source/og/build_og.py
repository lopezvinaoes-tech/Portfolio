"""Builds the link-preview images (assets/og.jpg and assets/og-es.jpg, 1200x630).

Run from the repo root:  python3 _source/og/build_og.py
Background photo: _source/og/photo.jpg. Fonts: _source/cv/fonts (static Inter).
"""
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
FONTS = ROOT / "_source" / "cv" / "fonts"
PHOTO = (HERE / "photo.jpg").as_uri()

VARIANTS = {
    "og.jpg": {"lang": "en", "kicker": "I am", "a": "Coding", "b": "Student.", "loc": "Barcelona, Spain", "hire": "Available to hire"},
    "og-es.jpg": {"lang": "es", "kicker": "Soy", "a": "Programador", "b": "en formación.", "loc": "Barcelona, España", "hire": "Disponible para trabajar"},
}

FACES = "".join(
    f'@font-face{{font-family:Inter;font-weight:{w};src:url({(FONTS / f"inter-latin-{w}-normal.woff2").as_uri()}) format("woff2")}}'
    for w in (400, 500, 600)
)


def page(v):
    return f"""<!doctype html><html lang="{v['lang']}"><head><meta charset="utf-8"><style>{FACES}
html,body{{margin:0}}
body{{width:1200px;height:630px;overflow:hidden;background:#000;font-family:Inter,sans-serif;color:#f5f5f7;position:relative}}
.photo{{position:absolute;inset:0;background:#000 url({PHOTO}) no-repeat;background-size:1200px 630px;background-position:230px 0}}
.fade{{position:absolute;inset:0;background:linear-gradient(90deg,#000 0%,#000 38%,rgba(0,0,0,0) 62%)}}
.txt{{position:absolute;left:72px;top:50%;transform:translateY(-50%);display:flex;flex-direction:column;gap:18px}}
.k{{font-size:26px;font-weight:500;color:#86868b;letter-spacing:-.01em}}
.role{{margin:0;font-weight:600;letter-spacing:-.05em;line-height:.95;font-size:{'84px' if v['lang']=='en' else '64px'}}}
.role span{{display:block}}
.g{{color:oklch(0.8 0.2 152);text-shadow:0 0 18px oklch(0.8 0.2 152 / .55),0 0 48px oklch(0.8 0.2 152 / .3)}}
.gray{{color:#86868b}}
.name{{margin-top:22px;font-size:34px;font-weight:600;letter-spacing:-.03em}}
.meta{{display:flex;align-items:center;gap:16px;font-size:20px;font-weight:500;color:#a1a1a6;letter-spacing:-.01em}}
.pill{{display:flex;align-items:center;gap:9px;height:38px;padding:0 16px;border-radius:999px;background:oklch(0.8 0.2 152 / .14);border:1px solid oklch(0.8 0.2 152 / .35);color:oklch(0.85 0.17 152)}}
.dot{{width:8px;height:8px;border-radius:50%;background:oklch(0.8 0.2 152);box-shadow:0 0 8px oklch(0.8 0.2 152)}}
</style></head><body>
<div class="photo"></div><div class="fade"></div>
<div class="txt">
  <div class="k">{v['kicker']}</div>
  <p class="role"><span class="g">{v['a']}</span><span class="gray">{v['b']}</span></p>
  <div class="name">Santiago Lopez Viñao</div>
  <div class="meta"><span>{v['loc']}</span><span class="pill"><span class="dot"></span>{v['hire']}</span></div>
</div>
</body></html>"""


def main():
    from playwright.sync_api import sync_playwright
    exe = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
    with sync_playwright() as p:
        b = p.chromium.launch(**({"executable_path": exe} if os.path.exists(exe) else {}))
        pg = b.new_page(viewport={"width": 1200, "height": 630})
        for name, v in VARIANTS.items():
            src = HERE / f"_{v['lang']}.html"
            src.write_text(page(v), encoding="utf-8")
            pg.goto(src.as_uri())
            pg.evaluate("document.fonts.ready")
            pg.wait_for_timeout(200)
            pg.screenshot(path=str(ROOT / "assets" / name), type="jpeg", quality=86)
            src.unlink()
            print("wrote", ROOT / "assets" / name)
        b.close()


if __name__ == "__main__":
    main()
