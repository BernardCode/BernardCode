#!/usr/bin/env python3
"""Build the profile's original SVGs. Standard library only; no network requests."""

import argparse
import html
from html.parser import HTMLParser
from pathlib import Path
import sys
from urllib.parse import urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
PALETTES = {
    "dark": dict(bg="#0d1117", panel="#111b22", ink="#edf4f7", muted="#9eafb9",
                 line="#293840", accent="#75e1cc", faint="#163b38", white="#17252c"),
    "light": dict(bg="#f6f9fa", panel="#ffffff", ink="#17282e", muted="#526870",
                  line="#d9e4e7", accent="#087f70", faint="#dcefeb", white="#eef4f6"),
}


def text(x, y, value, size=18, fill="ink", weight=400, extra=""):
    return (f'<text x="{x}" y="{y}" class="{fill}" font-size="{size}" '
            f'font-weight="{weight}" {extra}>{html.escape(value)}</text>')


def rect(x, y, w, h, radius=12, fill="panel", extra=""):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" '
            f'class="{fill}" {extra}/>')


def svg(w, h, theme, title, desc, content, animated=False):
    p = PALETTES[theme]
    colors = "\n".join(f".{name} {{ fill: {color}; }}" for name, color in p.items())
    animation = """
    .trace { stroke-dasharray: 76 1100; stroke-dashoffset: 1176; opacity: 0; }
    @media (prefers-reduced-motion: no-preference) {
      .trace { animation: travel 4s ease-in-out 0.4s 1; }
    }
    @keyframes travel {
      0% { stroke-dashoffset: 1176; opacity: 0; }
      15%, 80% { opacity: 1; }
      100% { stroke-dashoffset: 0; opacity: 0; }
    }
    """ if animated else ""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">
  <title id="title">{html.escape(title)}</title>
  <desc id="desc">{html.escape(desc)}</desc>
  <defs>
    <radialGradient id="wash"><stop stop-color="{p['accent']}" stop-opacity=".14"/><stop offset="1" stop-color="{p['accent']}" stop-opacity="0"/></radialGradient>
    <linearGradient id="wire" x1="0" y1="0" x2="1" y2="1"><stop stop-color="{p['accent']}"/><stop offset="1" stop-color="{p['muted']}" stop-opacity=".35"/></linearGradient>
    <clipPath id="bounds"><rect width="{w}" height="{h}" rx="16"/></clipPath>
  </defs>
  <style>
    text {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; }}
    .mono {{ font-family: ui-monospace, SFMono-Regular, Consolas, 'Liberation Mono', monospace; }}
    {colors}
    .border {{ stroke: {p['line']}; stroke-width: 1; }}
    .wire {{ fill: none; stroke: {p['line']}; stroke-width: 1.5; }}
    .signal {{ fill: none; stroke: {p['accent']}; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }}
    {animation}
  </style>
  <g clip-path="url(#bounds)">
    {rect(0, 0, w, h, 16, 'bg')}
    {content}
  </g>
  <rect x=".5" y=".5" width="{w - 1}" height="{h - 1}" rx="15.5" fill="none" class="border"/>
</svg>
'''


def monogram():
    # A lowercase b drawn as three offset circuit traces, with routed terminals.
    parts = ['<circle cx="194" cy="133" r="190" fill="url(#wash)"/>']
    for n in range(3):
        x, top, bottom = 131 + n * 11, 33 + n * 11, 234 - n * 11
        d = (f"M 4 {top} H {x-24} Q {x} {top} {x} {top+24} V {bottom-47} "
             f"Q {x} {bottom} 195 {bottom} H 210 Q {275-n*11} {bottom} {275-n*11} 171 "
             f"Q {275-n*11} {111+n*11} 214 {111+n*11} H {x+37} "
             f"Q {x+11} {111+n*11} {x+11} {137+n*5} V 165 "
             f"Q {x+11} {186-n*4} 183 {186-n*4} H 325")
        parts.append(f'<path d="{d}" fill="none" stroke="url(#wire)" stroke-width="1.4"/>')
        if n == 1:
            parts.append(f'<path d="{d}" class="signal trace"/>')
        parts.append(f'<circle cx="4" cy="{top}" r="3" class="accent"/>')
    parts.append('<circle cx="325" cy="182" r="4" class="accent"/>')
    for x, y in [(68, 113), (302, 60), (68, 233), (305, 247)]:
        parts.append(f'<path d="M{x-3} {y}h6 M{x} {y-3}v6" class="wire"/>')
    return "".join(parts)


def hero(theme, mobile):
    if mobile:
        w, h = 480, 310
        content = (f'<g transform="translate(230 10) scale(.85)" opacity=".30">{monogram()}</g>'
                   + text(30, 46, "BERNARDCODE", 13, "muted", 500, 'letter-spacing="2"')
                   + text(27, 126, "Bernard", 68, weight=650, extra='letter-spacing="-3.5"')
                   + text(27, 201, "Freund.", 68, weight=650, extra='letter-spacing="-3.5"')
                   + text(30, 265, "Student developer · Bay Area", 20, "muted"))
    else:
        w, h = 960, 340
        content = (f'<g transform="translate(575 28)">{monogram()}</g>'
                   + text(44, 52, "BERNARDCODE", 13, "muted", 500, 'letter-spacing="2.5"')
                   + text(39, 144, "Bernard", 84, weight=650, extra='letter-spacing="-4.5"')
                   + text(39, 235, "Freund.", 84, weight=650, extra='letter-spacing="-4.5"')
                   + text(44, 293, "Student developer · Bay Area", 21, "muted"))
    return svg(w, h, theme, "Bernard Freund", "Student developer in the Bay Area. Three circuit traces form a lowercase b. A signal passes through once, then rests.", content, True)


HAND = [(87,174),(55,149),(34,117),(17,93),(4,72),
        (63,102),(57,64),(53,37),(49,12),
        (91,96),(91,52),(91,23),(91,0),
        (117,100),(123,58),(126,34),(128,13),
        (140,111),(153,83),(160,64),(166,47)]
CHAINS = [(0,1,2,3,4),(0,5,6,7,8),(5,9,13,17,0),(0,9,10,11,12),
          (0,13,14,15,16),(0,17,18,19,20)]


def hand(x, y, scale=1):
    result = [f'<g transform="translate({x} {y}) scale({scale})">']
    for chain in CHAINS:
        points = " ".join(f"{HAND[i][0]},{HAND[i][1]}" for i in chain)
        result.append(f'<polyline points="{points}" class="signal" opacity=".65"/>')
    for px, py in HAND:
        result.append(f'<circle cx="{px}" cy="{py}" r="3.5" class="panel" stroke="currentColor"/>')
    result.append('</g>')
    return "".join(result)


def letters(x, y, width=45, gap=7):
    result = []
    for row, word in enumerate(["MARTEN", "MARTIN"]):
        for col, char in enumerate(word):
            px, py = x + col * (width + gap), y + row * 55
            result.append(rect(px, py, width, 46, 8, 'faint' if col == 4 else 'white'))
            result.append(text(px + width/2, py + 31, char, 25, 'accent' if col == 4 else 'ink', 500, 'text-anchor="middle"'))
    return "".join(result)


def manua(theme, mobile):
    accent = PALETTES[theme]['accent']
    if mobile:
        w, h = 480, 395
        content = (rect(18, 18, 444, 163) + text(38, 55, "Camera calibration", 24, weight=550)
                   + text(38, 86, "On-device landmarks", 20, "muted")
                   + f'<g color="{accent}">{hand(310, 38, .65)}</g>'
                   + '<path d="M38 141h176" class="wire"/>'
                   + '<circle cx="38" cy="141" r="3" class="accent"/>'
                   + rect(18, 197, 444, 180)
                   + text(38, 231, "Practice feedback", 24, weight=550)
                   + text(38, 257, "Scripted example", 20, "muted")
                   + letters(38, 275, 43, 9)
                   + text(378, 305, "typed", 18, "muted")
                   + text(378, 360, "target", 18, "muted"))
    else:
        w, h = 960, 260
        content = (rect(20, 20, 398, 220) + text(44, 60, "Camera calibration", 22, weight=550)
                   + text(44, 91, "On-device landmarks", 17, "muted")
                   + f'<g color="{accent}">{hand(264, 65, .82)}</g>'
                   + '<path d="M44 194h165" class="wire"/>'
                   + '<circle cx="44" cy="194" r="3" class="accent"/>'
                   + rect(434, 20, 506, 220) + text(458, 60, "Practice feedback", 22, weight=550)
                   + text(458, 88, "Scripted example", 16, "muted")
                   + letters(458, 111, 51, 8)
                   + text(835, 143, "typed", 16, "muted")
                   + text(835, 198, "target", 16, "muted"))
    return svg(w, h, theme, "Manua — two separate practice foundations", "A schematic hand landmark graph illustrates camera calibration. Beside it, a scripted receptive-practice example highlights the I/E substitution in MARTEN and MARTIN. This is not a camera recognition result.", content)


def located(theme, mobile):
    if mobile:
        w, h = 480, 300
        content = text(26, 41, "Evidence → candidates → claim", 23, weight=550)
        names = [("Text", 26, 69, 91), ("Visual", 128, 69, 100), ("Recency", 239, 69, 119),
                 ("Location", 26, 115, 135), ("Category", 172, 115, 135)]
        for name, x, y, width in names:
            content += rect(x, y, width, 35, 8, 'panel') + text(x+14, y+24, name, 20, 'muted')
        content += ('<path d="M26 177h427" class="wire"/>'
                    + rect(26, 202, 187, 60, 10, 'faint') + text(43, 239, "Ranked matches", 20, 'accent', 550)
                    + '<path d="M222 232h23m-5-5 5 5-5 5" class="signal"/>'
                    + rect(259, 202, 194, 60, 10, 'panel') + text(276, 239, "Verify ownership", 20, weight=550))
    else:
        w, h = 960, 240
        content = text(34, 48, "Evidence", 17, 'muted')
        names = [("Text", 34, 73, 86), ("Visual", 132, 73, 99), ("Recency", 243, 73, 119),
                 ("Location", 34, 132, 131), ("Category", 177, 132, 132)]
        for name, x, y, width in names:
            content += rect(x, y, width, 42, 9, 'panel') + text(x+15, y+28, name, 18, 'muted')
        content += ('<path d="M374 94h28q18 0 18 18v9h29 M321 153h80q19 0 19-19v-13" class="wire"/>'
                    + rect(454, 73, 214, 101, 12, 'faint')
                    + text(478, 113, "Ranked", 22, 'accent', 550) + text(478, 144, "matches", 22, 'accent', 550)
                    + '<path d="M682 122h41m-6-6 6 6-6 6" class="signal"/>'
                    + rect(738, 73, 188, 101, 12, 'panel')
                    + text(762, 113, "Verify", 22, weight=550) + text(762, 144, "ownership", 22, weight=550)
                    + text(454, 211, "A suggestion is not proof of ownership.", 17, 'muted'))
    return svg(w, h, theme, "LocatED — matching and verification", "Text, visual description, recency, location, and category inform ranked candidates. Ownership verification is a separate step; this diagram shows architecture, not measured results.", content)


def build():
    for name, render in [('hero', hero), ('manua', manua), ('located', located)]:
        for theme in PALETTES:
            for mobile in [False, True]:
                filename = f"{name}{'-mobile' if mobile else ''}-{theme}.svg"
                content = '\n'.join(line.rstrip() for line in render(theme, mobile).splitlines()) + '\n'
                yield ROOT / 'assets' / filename, content


class ProfileLinks(HTMLParser):
    """Check the local asset and documentation links in the README's HTML."""

    def __init__(self):
        super().__init__()
        self.errors = []

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag == 'img' and not values.get('alt', '').strip():
            self.errors.append('Every profile image needs alternative text.')
        for key in ('href', 'src', 'srcset'):
            value = values.get(key, '')
            refs = [part.strip().split()[0] for part in value.split(',') if part.strip()] if key == 'srcset' else [value]
            for ref in refs:
                if ref.startswith('./') and not (ROOT / urlsplit(ref).path).is_file():
                    self.errors.append(f'Missing local file: {ref}')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Validate committed SVGs without changing them')
    args = parser.parse_args()
    stale = []
    total = 0
    for path, content in build():
        ET.fromstring(content)
        total += len(content.encode())
        if args.check:
            if not path.exists() or path.read_text() != content:
                stale.append(str(path.relative_to(ROOT)))
        else:
            path.parent.mkdir(exist_ok=True)
            path.write_text(content)
    if stale:
        print('Run python3 scripts/build_assets.py. Outdated assets: ' + ', '.join(stale), file=sys.stderr)
        return 1
    if args.check:
        links = ProfileLinks()
        links.feed((ROOT / 'README.md').read_text())
        if links.errors:
            print('\n'.join(links.errors), file=sys.stderr)
            return 1
    print(f"{'Verified' if args.check else 'Built'} 12 self-contained SVGs ({total:,} bytes total).")
    return 0


if __name__ == '__main__':
    sys.exit(main())
