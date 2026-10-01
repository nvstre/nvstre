"""Generates the profile header. Edit NAME / LINE, then run: python3 gen.py"""
from pathlib import Path

NAME = "mateo."
LINE = "builds things. ships them."

OUT = Path(__file__).parent / "assets"
OUT.mkdir(exist_ok=True)
SANS = "-apple-system, 'Segoe UI', 'Helvetica Neue', Helvetica, Arial, sans-serif"
MONO = "'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace"


def header(fg, dim, line):
    w, h = 1200, 300
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<style>
  .n{{font:700 112px {SANS};fill:{fg};letter-spacing:-4px;animation:in 1.4s cubic-bezier(.16,1,.3,1) both}}
  .l{{font:400 18px {MONO};fill:{dim};letter-spacing:1px;animation:fade 1.2s ease .6s both}}
  .r{{transform-box:fill-box;transform-origin:left;animation:draw 1.4s cubic-bezier(.65,0,.35,1) .35s both}}
  .d{{animation:fade .6s ease 1.5s both, pulse 3s ease-in-out 2.1s infinite}}
  @keyframes in{{from{{opacity:0;transform:translateY(18px);letter-spacing:6px}}to{{opacity:1;transform:none;letter-spacing:-4px}}}}
  @keyframes fade{{from{{opacity:0}}to{{opacity:1}}}}
  @keyframes draw{{from{{transform:scaleX(0)}}to{{transform:scaleX(1)}}}}
  @keyframes pulse{{50%{{opacity:.25}}}}
</style>
<text class="n" x="40" y="160">{NAME}</text>
<rect class="r" x="44" y="196" width="{w-88}" height="1" fill="{line}"/>
<circle class="d" cx="{w-48}" cy="196.5" r="4" fill="{fg}"/>
<text class="l" x="44" y="244">{LINE}</text>
</svg>"""


(OUT / "header-dark.svg").write_text(header("#f0f6fc", "#7d8590", "#30363d"))
(OUT / "header-light.svg").write_text(header("#1f2328", "#656d76", "#d0d7de"))
print("ok")
