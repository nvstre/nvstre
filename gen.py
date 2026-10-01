"""Generates the animated SVG assets for the GitHub profile README."""
from pathlib import Path

OUT = Path(__file__).parent / "assets"
OUT.mkdir(exist_ok=True)

BG = "#07060b"
PANEL = "#0e0c16"
PINK = "#f72585"
PURPLE = "#7b2cbf"
CYAN = "#4cc9f0"
TEXT = "#ece9f5"
MUTED = "#8b86a3"
SANS = "'Segoe UI', 'Helvetica Neue', Helvetica, Arial, sans-serif"
MONO = "'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace"


# ---------------------------------------------------------------- hero
def hero():
    w, h = 1200, 440
    # synthwave grid: horizontal lines that drift toward the viewer
    hlines = "".join(
        f'<line x1="0" x2="{w}" y1="{y}" y2="{y}"/>' for y in range(0, 140, 20)
    )
    vlines = "".join(
        f'<line x1="{w/2 + (i * 40)}" y1="0" x2="{w/2 + (i * 260)}" y2="140"/>'
        for i in range(-16, 17)
    )
    words = [
        "shipping a GTA 6 companion platform",
        "teaching AI to referee arguments",
        "building multiplayer for Geometry Dash",
        "turning side projects into products",
    ]
    n = len(words)
    cycle = n * 3.2
    rot = ""
    for i, wd in enumerate(words):
        rot += f'<text class="rot" style="animation-delay:{i*3.2}s" x="600" y="296" text-anchor="middle">{wd}</text>'
    rot_kf = (
        f"@keyframes rot{{0%{{opacity:0;transform:translateY(14px);filter:blur(4px)}}"
        f"{100/n*0.12:.2f}%{{opacity:1;transform:translateY(0);filter:blur(0)}}"
        f"{100/n*0.85:.2f}%{{opacity:1;transform:translateY(0);filter:blur(0)}}"
        f"{100/n:.2f}%{{opacity:0;transform:translateY(-14px);filter:blur(4px)}}"
        f"100%{{opacity:0}}}}"
    )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<defs>
  <linearGradient id="nameb" x1="0" y1="0" x2="1" y2="0" spreadMethod="repeat">
    <stop offset="0" stop-color="{CYAN}"/>
    <stop offset="0.33" stop-color="{PINK}"/>
    <stop offset="0.66" stop-color="{PURPLE}"/>
    <stop offset="1" stop-color="{CYAN}"/>
    <animateTransform attributeName="gradientTransform" type="translate" values="0 0;1 0" dur="6s" repeatCount="indefinite"/>
  </linearGradient>
  <linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="{BG}" stop-opacity="1"/>
    <stop offset="1" stop-color="{BG}" stop-opacity="0"/>
  </linearGradient>
  <linearGradient id="hz" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="{PINK}" stop-opacity="0"/>
    <stop offset="0.5" stop-color="{PINK}"/>
    <stop offset="1" stop-color="{PINK}" stop-opacity="0"/>
  </linearGradient>
  <radialGradient id="sun" cx="0.5" cy="0.5" r="0.5">
    <stop offset="0" stop-color="{PINK}" stop-opacity="0.55"/>
    <stop offset="1" stop-color="{PINK}" stop-opacity="0"/>
  </radialGradient>
  <filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="60"/></filter>
  <filter id="glow" x="-20%" y="-50%" width="140%" height="200%">
    <feGaussianBlur stdDeviation="10" result="b"/>
    <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <clipPath id="clip"><rect width="{w}" height="{h}" rx="22"/></clipPath>
  <pattern id="noise" width="4" height="4" patternUnits="userSpaceOnUse">
    <rect width="4" height="1" fill="#fff" opacity="0.025"/>
  </pattern>
</defs>
<style>
  .blob{{animation:drift 16s ease-in-out infinite alternate}}
  .b2{{animation-duration:20s;animation-delay:-6s}}
  .b3{{animation-duration:24s;animation-delay:-12s}}
  @keyframes drift{{0%{{transform:translate(0,0) scale(1)}}50%{{transform:translate(120px,40px) scale(1.25)}}100%{{transform:translate(-90px,-30px) scale(0.9)}}}}
  .grid{{animation:grid 1.6s linear infinite}}
  @keyframes grid{{from{{transform:translateY(0)}}to{{transform:translateY(20px)}}}}
  .name{{font:900 128px {SANS};letter-spacing:18px;animation:in 1.2s cubic-bezier(.2,.8,.2,1) both}}
  .tag{{font:600 15px {MONO};letter-spacing:6px;fill:{MUTED};animation:in 1.2s .3s cubic-bezier(.2,.8,.2,1) both}}
  @keyframes in{{from{{opacity:0;transform:translateY(24px)}}to{{opacity:1;transform:translateY(0)}}}}
  .rot{{font:500 22px {MONO};fill:{TEXT};opacity:0;animation:rot {cycle}s infinite}}
  {rot_kf}
  .caret{{animation:blink 1s steps(1) infinite}}
  @keyframes blink{{50%{{opacity:0}}}}
  .scan{{animation:scan 5s linear infinite}}
  @keyframes scan{{from{{transform:translateY(-60px)}}to{{transform:translateY({h+60}px)}}}}
  .pulse{{animation:pulse 4s ease-in-out infinite;transform-origin:600px 320px}}
  @keyframes pulse{{50%{{opacity:.55;transform:scale(1.08)}}}}
</style>
<g clip-path="url(#clip)">
  <rect width="{w}" height="{h}" fill="{BG}"/>
  <g filter="url(#blur)" opacity="0.75">
    <circle class="blob" cx="260" cy="120" r="170" fill="{PURPLE}"/>
    <circle class="blob b2" cx="940" cy="110" r="190" fill="{PINK}" opacity="0.7"/>
    <circle class="blob b3" cx="620" cy="360" r="160" fill="{CYAN}" opacity="0.45"/>
  </g>
  <ellipse class="pulse" cx="600" cy="320" rx="300" ry="110" fill="url(#sun)"/>
  <g transform="translate(0 {h-130})">
    <g class="grid" stroke="{PINK}" stroke-opacity="0.22" stroke-width="1">{hlines}</g>
    <g stroke="{PINK}" stroke-opacity="0.18" stroke-width="1">{vlines}</g>
    <rect y="-2" width="{w}" height="50" fill="url(#fade)"/>
    <rect y="-1" width="{w}" height="2" fill="url(#hz)"/>
  </g>
  <rect width="{w}" height="{h}" fill="url(#noise)"/>
  <text class="tag" x="600" y="84" text-anchor="middle">INDIE BUILDER · STUDENT · ALBA IULIA, RO</text>
  <g filter="url(#glow)">
    <text class="name" x="609" y="214" text-anchor="middle" fill="url(#nameb)">MATEO
      <animate attributeName="fill-opacity" values="1;0.92;1;1;0.85;1" dur="7s" repeatCount="indefinite"/>
    </text>
  </g>
  <g font-family="{MONO}">
    <text x="600" y="262" text-anchor="middle" font-size="14" fill="{PINK}" letter-spacing="3">~/currently $</text>
    {rot}
  </g>
  <rect class="scan" x="0" y="0" width="{w}" height="2" fill="#ffffff" opacity="0.05"/>
  <rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="22" fill="none" stroke="#ffffff" stroke-opacity="0.08"/>
</g>
</svg>"""


# ------------------------------------------------------------ terminal
def terminal():
    w = 1200
    lines = [
        ("cmd", "whoami"),
        ("out", "mateo — student @ Colegiul Economic, Alba Iulia 🇷🇴"),
        ("out", "financial director @ F.E. Nirvana S.R.L. (yes, the spreadsheets too)"),
        ("cmd", "cat stack.txt"),
        ("out", "next.js · react · typescript · supabase · maplibre · vercel · claude code"),
        ("cmd", "echo $MOTTO"),
        ("hl", "ship it, then make it pretty."),
    ]
    y0, lh = 92, 36
    h = y0 + lh * len(lines) + 40
    body = ""
    t = 0.4
    for i, (kind, txt) in enumerate(lines):
        y = y0 + i * lh
        chars = len(txt) + (2 if kind == "cmd" else 0)
        dur = max(0.35, chars * 0.028) if kind == "cmd" else 0.35
        width = 20 + chars * 12.4
        if kind == "cmd":
            content = f'<tspan fill="{PINK}">❯</tspan> <tspan fill="{TEXT}">{txt}</tspan>'
            anim = f"animation:type {dur:.2f}s steps({chars}) {t:.2f}s both"
        else:
            color = CYAN if kind == "hl" else MUTED
            content = f'<tspan fill="{color}">{txt}</tspan>'
            anim = f"animation:fadein .35s ease-out {t:.2f}s both"
        if kind == "cmd":
            body += (
                f'<clipPath id="c{i}"><rect x="48" y="{y-24}" width="{width:.0f}" height="34" '
                f'style="transform-box:fill-box;transform-origin:left;{anim}"/></clipPath>'
                f'<text x="56" y="{y}" clip-path="url(#c{i})">{content}</text>'
            )
        else:
            body += f'<text x="56" y="{y}" style="{anim}">{content}</text>'
        t += dur + (0.45 if kind == "cmd" else 0.12)
    cy = y0 + lh * len(lines)
    body += (
        f'<text x="56" y="{cy}" style="animation:fadein .2s {t:.2f}s both"><tspan fill="{PINK}">❯</tspan>'
        f'<tspan class="caret" fill="{PINK}" dx="10">█</tspan></text>'
    )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<defs>
  <linearGradient id="bar" x1="0" x2="1">
    <stop offset="0" stop-color="{PURPLE}" stop-opacity="0.35"/>
    <stop offset="1" stop-color="{PINK}" stop-opacity="0.15"/>
  </linearGradient>
  <linearGradient id="edge" x1="0" x2="1" y1="0" y2="1">
    <stop offset="0" stop-color="{PINK}" stop-opacity="0.6"/>
    <stop offset="0.5" stop-color="#ffffff" stop-opacity="0.06"/>
    <stop offset="1" stop-color="{CYAN}" stop-opacity="0.5"/>
  </linearGradient>
</defs>
<style>
  text{{font:500 19px {MONO};white-space:pre}}
  @keyframes type{{from{{transform:scaleX(0)}}to{{transform:scaleX(1)}}}}
  @keyframes fadein{{from{{opacity:0;transform:translateY(6px)}}to{{opacity:1;transform:none}}}}
  .caret{{animation:blink 1s steps(1) infinite}}
  @keyframes blink{{50%{{opacity:0}}}}
  .ttl{{font:600 14px {MONO};fill:{MUTED};letter-spacing:1px}}
</style>
<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="18" fill="{PANEL}" stroke="url(#edge)" stroke-width="1.5"/>
<path d="M1 19a18 18 0 0 1 18-18h{w-38}a18 18 0 0 1 18 18v31H1z" fill="url(#bar)"/>
<circle cx="32" cy="26" r="7" fill="#ff5f57"/><circle cx="56" cy="26" r="7" fill="#febc2e"/><circle cx="80" cy="26" r="7" fill="#28c840"/>
<text class="ttl" x="{w/2}" y="31" text-anchor="middle">mateo@alba-iulia: ~</text>
{body}
</svg>"""


# --------------------------------------------------------------- cards
ICONS = {
    # simple line glyphs, drawn in a 40x40 box
    "map": '<path d="M4 9l10-4 12 4 10-4v26l-10 4-12-4-10 4z M14 5v26 M26 9v26"/>',
    "scale": '<path d="M20 4v32 M10 36h20 M6 10h28 M10 10l-6 12h12z M30 10l-6 12h12z"/><circle cx="20" cy="6" r="2"/>',
    "tri": '<path d="M20 5l15 27H5z"/><path d="M20 16l6 11H14z"/>',
    "bolt": '<path d="M22 3L8 22h11l-3 15 16-21H21z"/>',
}


def card(slug, title, lines, status, status_color, tags, icon, accent):
    w, h = 580, 230
    desc = "".join(
        f'<text class="d" x="34" y="{122 + i*24}">{ln}</text>' for i, ln in enumerate(lines)
    )
    tx, tag_svg = 34, ""
    for tg in tags:
        tw = 16 + len(tg) * 8.2
        tag_svg += (
            f'<rect x="{tx}" y="182" width="{tw:.0f}" height="26" rx="13" fill="{accent}" fill-opacity="0.1" stroke="{accent}" stroke-opacity="0.35"/>'
            f'<text class="t" x="{tx + tw/2:.0f}" y="199.5" text-anchor="middle">{tg}</text>'
        )
        tx += tw + 8
    sw = 34 + len(status) * 9.8
    perim = 2 * (w - 4) + 2 * (h - 4)
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<defs>
  <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="{accent}" stop-opacity="0.22"/>
    <stop offset="0.55" stop-color="{PANEL}" stop-opacity="0"/>
  </linearGradient>
  <linearGradient id="ln" x1="0" x2="1"><stop offset="0" stop-color="{accent}"/><stop offset="1" stop-color="{PINK}"/></linearGradient>
  <filter id="gl" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation="3"/></filter>
</defs>
<style>
  .h{{font:800 28px {SANS};fill:{TEXT}}}
  .d{{font:400 16.5px {SANS};fill:{MUTED}}}
  .t{{font:600 12.5px {MONO};fill:{accent}}}
  .s{{font:700 12px {MONO};fill:{status_color};letter-spacing:1.5px}}
  .run{{stroke-dasharray:140 {perim-140};animation:run 6s linear infinite}}
  @keyframes run{{to{{stroke-dashoffset:-{perim}}}}}
  .dot{{animation:ping 1.8s ease-out infinite;transform-box:fill-box;transform-origin:center}}
  @keyframes ping{{0%{{transform:scale(1);opacity:.9}}100%{{transform:scale(3);opacity:0}}}}
  .ic{{animation:float 4s ease-in-out infinite}}
  @keyframes float{{50%{{transform:translateY(-4px)}}}}
  .all{{animation:rise .9s cubic-bezier(.2,.8,.2,1) both}}
  @keyframes rise{{from{{opacity:0;transform:translateY(12px)}}to{{opacity:1;transform:none}}}}
</style>
<g class="all">
<rect x="2" y="2" width="{w-4}" height="{h-4}" rx="20" fill="{PANEL}"/>
<rect x="2" y="2" width="{w-4}" height="{h-4}" rx="20" fill="url(#g)"/>
<rect x="2" y="2" width="{w-4}" height="{h-4}" rx="20" fill="none" stroke="#ffffff" stroke-opacity="0.07"/>
<rect class="run" x="2" y="2" width="{w-4}" height="{h-4}" rx="20" fill="none" stroke="url(#ln)" stroke-width="2.5" filter="url(#gl)"/>
<rect class="run" x="2" y="2" width="{w-4}" height="{h-4}" rx="20" fill="none" stroke="url(#ln)" stroke-width="1.5"/>
<g class="ic" transform="translate(34 30)"><g fill="none" stroke="{accent}" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round">{ICONS[icon]}</g></g>
<text class="h" x="88" y="62">{title}</text>
<rect x="{w-34-sw:.0f}" y="38" width="{sw:.0f}" height="28" rx="14" fill="{status_color}" fill-opacity="0.12" stroke="{status_color}" stroke-opacity="0.4"/>
<circle class="dot" cx="{w-34-sw+15:.0f}" cy="52" r="4" fill="{status_color}"/>
<circle cx="{w-34-sw+15:.0f}" cy="52" r="4" fill="{status_color}"/>
<text class="s" x="{w-34-sw+26:.0f}" y="56.5">{status}</text>
{desc}
{tag_svg}
</g>
</svg>"""
    (OUT / f"card-{slug}.svg").write_text(svg)


# -------------------------------------------------------------- divider
def divider(label):
    w, h = 1200, 60
    tw = len(label) * 11 + 40
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<defs>
  <linearGradient id="l" x1="0" x2="1">
    <stop offset="0" stop-color="{PINK}" stop-opacity="0"/>
    <stop offset="0.5" stop-color="{PINK}"/>
    <stop offset="1" stop-color="{CYAN}" stop-opacity="0"/>
    <animateTransform attributeName="gradientTransform" type="translate" values="-0.6 0;0.6 0;-0.6 0" dur="7s" repeatCount="indefinite"/>
  </linearGradient>
</defs>
<rect x="0" y="29" width="{w}" height="2" fill="url(#l)"/>
<rect x="{(w-tw)/2}" y="14" width="{tw}" height="32" rx="16" fill="{BG}" stroke="{PINK}" stroke-opacity="0.45"/>
<text x="{w/2}" y="35" text-anchor="middle" font-family="{MONO}" font-size="15" font-weight="700" letter-spacing="3" fill="{TEXT}">{label}</text>
</svg>"""


if __name__ == "__main__":
    (OUT / "hero.svg").write_text(hero())
    (OUT / "terminal.svg").write_text(terminal())
    for lbl in ["PROJECTS", "STACK", "STATS"]:
        (OUT / f"div-{lbl.lower()}.svg").write_text(divider(lbl))
    card("leonida", "Leonida Link",
         ["GTA 6 fan companion — forum, wiki and an", "interactive 3D map of the state of Leonida."],
         "LIVE", "#22c55e", ["next.js", "supabase", "maplibre"], "map", CYAN)
    card("fairpoint", "FairPoint",
         ["Drop the screenshots of an argument, get a", "fact-checked verdict on who's actually right."],
         "BUILDING", "#f59e0b", ["ai", "fact-check", "next.js"], "scale", PINK)
    card("gdmp", "GDMP",
         ["Geometry Dash Multiplayer — a launcher for", "community servers. FiveM energy, but for GD."],
         "BUILDING", "#f59e0b", ["launcher", "multiplayer", "discord"], "tri", "#b07cff")
    card("fit", "fit-tracker",
         ["Personal gym, food and body tracker that", "pulls smart-scale data from Apple Health."],
         "EARLY", "#94a3b8", ["ios", "healthkit", "tracking"], "bolt", "#22c55e")
    print("ok")
