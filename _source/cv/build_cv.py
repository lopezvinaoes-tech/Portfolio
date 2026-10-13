"""Builds the CV PDFs (ES + EN) served from assets/cv/.

Edit the CONTENT dict below, then run from the repo root:
    python3 _source/cv/build_cv.py
Requires Python 3 + Playwright with Chromium.
"""
import html
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / "assets" / "cv"
# Static weights (not the variable font): Chromium embeds variable fonts as Type 3,
# which some CV parsers (ATS) read poorly.
FONTS = Path(__file__).with_name("fonts")

NAME = "Santiago Lopez Viñao"
EMAIL = "lopezvinaoes@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/santiago-lopez-vi%C3%B1ao/"
LINKEDIN_LABEL = "linkedin.com/in/santiago-lopez-viñao"
# GitHub and the portfolio URL are left out on purpose: the CV is downloaded from the portfolio itself.

CONTENT = {
    "es": {
        "file": "Santiago-Lopez-CV-ES.pdf",
        "title": "Santiago Lopez Viñao — CV",
        "role": "Estudiante de Desarrollo de Aplicaciones Multiplataforma y Web (DAM/DAW)",
        "location": "Barcelona, España",
        "h": {"profile": "Perfil", "education": "Formación", "project": "Proyecto",
              "skills": "Habilidades", "experience": "Experiencia", "more": "Información adicional"},
        "profile": (
            "Estudiante de DAM/DAW en Universae con base en HTML, CSS y JavaScript. "
            "Vengo de cinco años en hostelería y administración, donde lideré equipos pequeños, "
            "gestioné caja, stock y reservas, y atendí a clientela internacional de alto perfil. "
            "Busco prácticas o un primer puesto junior donde aportar organización, comunicación "
            "y orientación al cliente mientras crezco como desarrollador."
        ),
        "education": [("Desarrollo de Aplicaciones Multiplataforma y Web (DAM/DAW)",
                       "Universae · Barcelona", "En curso – 2028")],
        "project": {
            "name": "Portfolio personal",
            "meta": "Web propia, publicada en Vercel · código en GitHub",
            "bullets": [
                "Web de una sola página con animaciones ligadas al scroll, menú adaptado a móvil "
                "y formulario de contacto con protección anti-spam (hCaptcha + Web3Forms).",
                "Optimización de rendimiento (fuente e iconos alojados en la propia web, caché), "
                "SEO (datos estructurados, sitemap) y accesibilidad (navegación por teclado, "
                "respeto a «reducir movimiento»).",
            ],
        },
        "skills": [
            ("Desarrollo", "HTML, CSS, JavaScript"),
            ("Herramientas", "GitHub, Vercel, Opera Cloud (PMS), TPV, Canva, Adobe Premiere"),
            ("Idiomas", "Español (nativo), inglés (B2)"),
        ],
        "experience": [
            ("Front Office Agent", "ME Sitges Terramar (Meliá) · Sitges", "04/2026 – Actualidad", [
                "Check-in, check-out, reservas y comunicaciones previas a la llegada en Opera Cloud.",
                "Facturación, cobros y resolución de incidencias con clientela internacional de alto perfil.",
                "Coordinación de peticiones especiales con Guest Experience y los outlets del hotel.",
            ]),
            ("Camarero & Guest Experience Trainee", "ME Sitges Terramar (Meliá) · Sitges", "08/2025 – 03/2026", [
                "Personalización de estancias y gestión de peticiones especiales para mejorar el NPS.",
                "Upselling en piscina y restaurante; 100 % de cumplimiento en protocolos de alérgenos.",
            ]),
            ("Encargado", "Happy Park · Mallorca", "06/2024 – 07/2025", [
                "Control financiero diario: cierres de caja sin descuadres y reportes de rendimiento.",
                "Cobros por TPV con un margen de error inferior al 1 %.",
                "Coordinación del equipo y supervisión de zonas de riesgo sin incidentes (+120 visitantes diarios).",
            ]),
            ("Encargado", "Three Monkeys Bar · Buenos Aires", "03/2022 – 05/2023", [
                "Gestión de un equipo de 4 personas: tareas y turnos.",
                "Control de stock: −15 % de desperdicio y −30 % en tiempos de reposición.",
            ]),
            ("Administrativo", "ByC Gastronomía · Buenos Aires", "01/2021 – 02/2022", [
                "Registro de ventas diarias en el sistema contable y seguimiento de stock.",
                "Actualización de listas de precios y apoyo en propuestas comerciales.",
            ]),
        ],
        "more": "Disponibilidad inmediata, también con traslado.",
    },
    "en": {
        "file": "Santiago-Lopez-CV-EN.pdf",
        "title": "Santiago Lopez Viñao — CV",
        "role": "Multiplatform & Web App Development student (DAM/DAW)",
        "location": "Barcelona, Spain",
        "h": {"profile": "Profile", "education": "Education", "project": "Project",
              "skills": "Skills", "experience": "Experience", "more": "Additional information"},
        "profile": (
            "DAM/DAW student at Universae with a foundation in HTML, CSS and JavaScript. "
            "I come from five years in hospitality and administration, where I led small teams, "
            "handled cash, stock and reservations, and looked after high-profile international guests. "
            "I'm looking for an internship or a first junior role where I can bring organisation, "
            "communication and a customer focus while I grow as a developer."
        ),
        "education": [("Multiplatform & Web App Development (DAM/DAW)",
                       "Universae · Barcelona", "In progress – 2028")],
        "project": {
            "name": "Personal portfolio",
            "meta": "Own website, deployed on Vercel · code on GitHub",
            "bullets": [
                "Single-page site with scroll-driven animations, a mobile menu and a contact form "
                "with spam protection (hCaptcha + Web3Forms).",
                "Performance work (self-hosted font and icons, caching), SEO (structured data, "
                "sitemap) and accessibility (keyboard navigation, reduced-motion support).",
            ],
        },
        "skills": [
            ("Development", "HTML, CSS, JavaScript"),
            ("Tools", "GitHub, Vercel, Opera Cloud (PMS), POS, Canva, Adobe Premiere"),
            ("Languages", "Spanish (native), English (B2)"),
        ],
        "experience": [
            ("Front Office Agent", "ME Sitges Terramar (Meliá) · Sitges", "04/2026 – Present", [
                "Check-ins, check-outs, reservations and pre-arrival communications in Opera Cloud.",
                "Billing, payments and issue resolution for high-profile international guests.",
                "Coordinating special requests with Guest Experience and the hotel's outlets.",
            ]),
            ("Waiter & Guest Experience Trainee", "ME Sitges Terramar (Meliá) · Sitges", "08/2025 – 03/2026", [
                "Personalised stays and special requests to raise guest satisfaction (NPS).",
                "Upselling at the pool and restaurant; 100% compliance with allergen protocols.",
            ]),
            ("Manager", "Happy Park · Mallorca", "06/2024 – 07/2025", [
                "Daily financial control: cash-ups with no discrepancies and performance reports.",
                "POS payments with an error rate below 1%.",
                "Team coordination and supervision of high-risk areas with zero incidents (120+ daily visitors).",
            ]),
            ("Bar Manager", "Three Monkeys Bar · Buenos Aires", "03/2022 – 05/2023", [
                "Led a team of four: tasks and shift planning.",
                "Stock control: cut waste by 15% and restocking times by 30%.",
            ]),
            ("Administrative Assistant", "ByC Gastronomía · Buenos Aires", "01/2021 – 02/2022", [
                "Logged daily sales in the accounting system and tracked stock.",
                "Updated price lists and supported sales proposals.",
            ]),
        ],
        "more": "Available immediately, including relocation.",
    },
}

CSS = """
%(fontfaces)s
@page{size:A4;margin:0}
*{box-sizing:border-box}
html,body{margin:0}
body{font-family:Inter,system-ui,sans-serif;color:#1d1d1f;font-size:9.4pt;line-height:1.42;
  -webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{width:210mm;min-height:297mm;padding:15mm 17mm 13mm}
a{color:inherit;text-decoration:none}
header{display:flex;justify-content:space-between;align-items:flex-end;gap:10mm;
  padding-bottom:5mm;border-bottom:1px solid #e5e5ea}
h1{margin:0;font-size:25pt;line-height:1;font-weight:600;letter-spacing:-.035em}
h1 span{color:#86868b}
.role{margin-top:2.4mm;font-size:10pt;font-weight:500;color:#1f8a4c;letter-spacing:-.01em}
.contact{text-align:right;font-size:8.6pt;line-height:1.6;color:#6e6e73;white-space:nowrap}
.contact a{color:#1d1d1f}
section{margin-top:5mm}
h2{margin:0 0 2mm;font-size:8pt;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:#1f8a4c}
p{margin:0}
.item{margin-top:2.6mm;break-inside:avoid}
.item:first-of-type{margin-top:0}
.row{display:flex;justify-content:space-between;gap:6mm;align-items:baseline}
.t{font-weight:600;font-size:10pt;letter-spacing:-.015em}
.m{color:#6e6e73;font-size:8.8pt}
.d{color:#6e6e73;font-size:8.6pt;white-space:nowrap;font-variant-numeric:tabular-nums}
ul{margin:1mm 0 0;padding-left:4mm}
li{margin:.4mm 0;color:#3a3a3c}
li::marker{color:#86868b}
.skills{display:grid;grid-template-columns:28mm 1fr;row-gap:1.2mm}
.skills b{font-weight:600}
"""


FONTFACES = "".join(
    f'@font-face{{font-family:Inter;font-weight:{w};src:url({(FONTS / f"inter-latin-{w}-normal.woff2").as_uri()}) format("woff2")}}'
    for w in (400, 500, 600)
)


def esc(s):
    return html.escape(s, quote=True)


def bullets(items):
    return "<ul>" + "".join(f"<li>{esc(b)}</li>" for b in items) + "</ul>"


def page(c):
    first, rest = NAME.split(" ", 1)
    exp = "".join(
        f'<div class="item"><div class="row"><span><span class="t">{esc(t)}</span> '
        f'<span class="m">· {esc(org)}</span></span><span class="d">{esc(d)}</span></div>{bullets(b)}</div>'
        for t, org, d, b in c["experience"]
    )
    edu = "".join(
        f'<div class="item"><div class="row"><span><span class="t">{esc(t)}</span> '
        f'<span class="m">· {esc(org)}</span></span><span class="d">{esc(d)}</span></div></div>'
        for t, org, d in c["education"]
    )
    pr = c["project"]
    skills = "".join(f"<b>{esc(k)}</b><span>{esc(v)}</span>" for k, v in c["skills"])
    h = c["h"]
    return f"""<!doctype html><html lang="{'es' if c is CONTENT['es'] else 'en'}"><head><meta charset="utf-8">
<title>{esc(c['title'])}</title><style>{CSS % {'fontfaces': FONTFACES}}</style></head><body><div class="page">
<header>
  <div><h1>{esc(first)} <span>{esc(rest)}</span></h1><div class="role">{esc(c['role'])}</div></div>
  <div class="contact">{esc(c['location'])}<br>
    <a href="mailto:{EMAIL}">{EMAIL}</a><br>
    <a href="{LINKEDIN}">{esc(LINKEDIN_LABEL)}</a></div>
</header>
<section><h2>{h['profile']}</h2><p>{esc(c['profile'])}</p></section>
<section><h2>{h['education']}</h2>{edu}</section>
<section><h2>{h['project']}</h2><div class="item"><div class="row"><span><span class="t">{esc(pr['name'])}</span>
  <span class="m">· {esc(pr['meta'])}</span></span></div>{bullets(pr['bullets'])}</div></section>
<section><h2>{h['skills']}</h2><div class="skills">{skills}</div></section>
<section><h2>{h['experience']}</h2>{exp}</section>
<section><h2>{h['more']}</h2><p>{esc(c['more'])}</p></section>
</div></body></html>"""


def main():
    from playwright.sync_api import sync_playwright

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    exe = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
    with sync_playwright() as p:
        b = p.chromium.launch(**({"executable_path": exe} if os.path.exists(exe) else {}))
        pg = b.new_page()
        for lang, c in CONTENT.items():
            src = Path(__file__).with_name(f"cv-{lang}.html")
            src.write_text(page(c), encoding="utf-8")
            pg.goto(src.as_uri())
            pg.evaluate("document.fonts.ready")
            pg.pdf(path=str(OUT_DIR / c["file"]), format="A4", print_background=True,
                   prefer_css_page_size=True)
            print("wrote", OUT_DIR / c["file"])
        b.close()


if __name__ == "__main__":
    main()
