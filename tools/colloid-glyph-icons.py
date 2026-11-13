#!/usr/bin/env python3
"""Draw Colloid-style application icons for apps the theme does not cover yet.

Every icon sits in the same grid as the rest of Colloid's application icons
(a 224 px tile in a 256 px canvas, 51.5 px corner radius, soft shadow below),
with a two-tone gradient and a simple white glyph. The glyphs are original
work: they hint at what the app does and do not copy any app's logo.

Usage: colloid-glyph-icons.py [ICON-NAME ...]

Without arguments it writes every icon below into src/apps/scalable/. The
names are the Icon= of each app's .desktop file. Needs Pillow.
"""
import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ICONS = HERE.parent / 'src' / 'apps' / 'scalable'

spec = importlib.util.spec_from_file_location('app_icon', HERE / 'nodalia-app-icon.py')
app_icon = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app_icon)

W = '#FFFFFF'


def digit(bit, x, y, opacity):
    """A 0 or a 1, drawn as shapes so that no font is needed."""
    stroke = f'fill="none" stroke="#FFFFFF" stroke-opacity="{opacity}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"'
    if bit:
        return f'<path d="M{x + 2} {y + 10} L{x + 14} {y} V{y + 44} M{x + 2} {y + 44} H{x + 26}" {stroke}/>'
    return f'<rect x="{x}" y="{y}" width="26" height="44" rx="13" {stroke}/>'


def digits(row):
    patterns = ('0110', '1001')
    return ''.join(digit(int(c), 58 + i * 38, 76 + row * 64, 1 if row == 0 else .6) for i, c in enumerate(patterns[row]))
SOFT = '#FFFFFF" fill-opacity=".55'

# name: (top colour, bottom colour, description, glyph drawn on the 256 canvas)
ICONS_DEF = {
    'org.gnome.design.Contrast': ('#5B6577', '#2F3644', 'Contrast: two overlapping discs, one light and one dark.',
        f'<circle cx="104" cy="128" r="52" fill="{W}"/>'
        f'<circle cx="152" cy="128" r="52" fill="#11151D" fill-opacity=".85"/>'
        f'<path d="M128 87 a52 52 0 0 1 0 82 a52 52 0 0 1 0 -82z" fill="#8E97A8"/>'),
    'org.gnome.design.Emblem': ('#F0A030', '#D9621D', 'Emblem: a shield with a star.',
        f'<path d="M128 56 L186 76 V124 C186 158 162 182 128 198 C94 182 70 158 70 124 V76 Z" fill="{W}"/>'
        f'<path d="M128 90 L137 112 L160 114 L142 129 L148 152 L128 140 L108 152 L114 129 L96 114 L119 112 Z" fill="#D9621D"/>'),
    'org.gnome.design.Palette': ('#9C6ADE', '#5E3FB5', 'Palette: three colour swatches.',
        f'<rect x="66" y="76" width="124" height="104" rx="14" fill="{W}"/>'
        f'<rect x="76" y="86" width="34" height="84" rx="8" fill="#F0A030"/>'
        f'<rect x="114" y="86" width="34" height="84" rx="8" fill="#2EC27E"/>'
        f'<rect x="152" y="86" width="28" height="84" rx="8" fill="#3584E4"/>'),
    'org.pipewire.Helvum': ('#3FA7C9', '#1E5E8E', 'Helvum: nodes joined by patch cables.',
        f'<rect x="58" y="70" width="52" height="38" rx="9" fill="{W}"/>'
        f'<rect x="58" y="146" width="52" height="38" rx="9" fill="{W}"/>'
        f'<rect x="146" y="108" width="52" height="38" rx="9" fill="{W}"/>'
        f'<path d="M110 89 C130 89 126 127 146 127" fill="none" stroke="{W}" stroke-width="7" stroke-linecap="round"/>'
        f'<path d="M110 165 C130 165 126 127 146 127" fill="none" stroke="{W}" stroke-width="7" stroke-linecap="round" stroke-opacity=".7"/>'),
    'io.github.nozwock.Packet': ('#35C1B3', '#17837C', 'Packet: a paper plane sending files.',
        f'<path d="M62 124 L194 66 L160 190 L124 152 Z" fill="{W}"/>'
        f'<path d="M124 152 L194 66 L110 134 Z" fill="#17837C" fill-opacity=".35"/>'
        f'<path d="M124 152 L120 192 L144 168 Z" fill="{W}" fill-opacity=".7"/>'),
    'io.github.getnf.embellish': ('#E8629A', '#B0306B', 'Embellish: a letter with a font swash.',
        f'<path d="M62 188 L102 84 L142 188 M77 154 H127" fill="none" stroke="{W}" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/>'
        f'<circle cx="170" cy="162" r="22" fill="none" stroke="{W}" stroke-width="12"/><path d="M192 140 V188" stroke="{W}" stroke-width="12" stroke-linecap="round"/>'
        f'<path d="M60 206 C92 196 150 214 196 200" fill="none" stroke="{W}" stroke-width="7" stroke-linecap="round" stroke-opacity=".7"/>'),
    'io.podman_desktop.PodmanDesktop': ('#8A6BD6', '#4B3A9A', 'Podman Desktop: a container cube.',
        f'<path d="M128 56 L190 90 V158 L128 192 L66 158 V90 Z" fill="{W}"/>'
        f'<path d="M128 56 L190 90 L128 124 L66 90 Z" fill="#FFFFFF" fill-opacity=".0"/>'
        f'<path d="M128 124 V192 M128 124 L66 90 M128 124 L190 90" fill="none" stroke="#4B3A9A" stroke-width="7" stroke-linejoin="round" stroke-opacity=".55"/>'),
    'com.ranfdev.DistroShelf': ('#C4733E', '#8A4620', 'DistroShelf: a shelf holding boxes.',
        f'<rect x="60" y="68" width="38" height="52" rx="7" fill="{W}"/>'
        f'<rect x="104" y="84" width="38" height="36" rx="7" fill="{W}" fill-opacity=".8"/>'
        f'<rect x="148" y="60" width="38" height="60" rx="7" fill="{W}"/>'
        f'<rect x="52" y="124" width="152" height="9" rx="4.5" fill="{W}"/>'
        f'<rect x="72" y="146" width="44" height="30" rx="7" fill="{W}" fill-opacity=".8"/>'
        f'<rect x="124" y="140" width="56" height="36" rx="7" fill="{W}"/>'
        f'<rect x="52" y="180" width="152" height="9" rx="4.5" fill="{W}"/>'),
    'org.gnome.NetworkDisplays': ('#3584E4', '#1B4F9C', 'Network Displays: a screen casting to another.',
        f'<rect x="62" y="68" width="132" height="86" rx="12" fill="{W}"/>'
        f'<path d="M96 184 H160" stroke="{W}" stroke-width="9" stroke-linecap="round"/>'
        f'<path d="M92 128 a22 22 0 0 1 22 22 M92 112 a38 38 0 0 1 38 38" fill="none" stroke="#1B4F9C" stroke-width="8" stroke-linecap="round"/>'
        f'<circle cx="92" cy="148" r="5" fill="#1B4F9C"/>'),
    'io.github.flattool.Ignition': ('#F0613A', '#B82E1A', 'Ignition: a power symbol for startup apps.',
        f'<path d="M94 94 a54 54 0 1 0 68 0" fill="none" stroke="{W}" stroke-width="14" stroke-linecap="round"/>'
        f'<path d="M128 58 V122" stroke="{W}" stroke-width="14" stroke-linecap="round"/>'),
    'io.github.fizzyizzy05.binary': ('#4C5A74', '#252E40', 'Binary: ones and zeros.',
        digits(0) + digits(1)),
    'org.nickvision.cavalier': ('#8E5BD9', '#3F2B96', 'Cavalier: audio visualiser bars.',
        ''.join(f'<rect x="{x}" y="{200 - h}" width="16" height="{h}" rx="8" fill="{W}"/>'
                for x, h in ((62, 56), (84, 100), (106, 76), (128, 132), (150, 88), (172, 108)))),
    'io.github.jeffshee.Hidamari': ('#40B6E0', '#2377B8', 'Hidamari: a live wallpaper frame with a play mark.',
        f'<rect x="58" y="72" width="140" height="100" rx="14" fill="{W}"/>'
        f'<path d="M112 100 L152 122 L112 144 Z" fill="#2377B8"/>'
        f'<path d="M96 192 H160" stroke="{W}" stroke-width="9" stroke-linecap="round" stroke-opacity=".7"/>'),
    'io.github.diegoivanme.flowtime': ('#EE6E73', '#B83A55', 'Flowtime: a stopwatch.',
        f'<circle cx="128" cy="138" r="54" fill="none" stroke="{W}" stroke-width="13"/>'
        f'<path d="M128 138 V108 M128 138 L148 150" stroke="{W}" stroke-width="10" stroke-linecap="round"/>'
        f'<path d="M110 66 H146" stroke="{W}" stroke-width="12" stroke-linecap="round"/>'),
    'io.github.vikdevelop.SaveDesktop': ('#2CB67D', '#177A55', 'Save Desktop: a screen with a save arrow.',
        f'<rect x="60" y="70" width="136" height="92" rx="12" fill="{W}"/>'
        f'<path d="M128 90 V132 M108 114 L128 134 L148 114" fill="none" stroke="#177A55" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>'
        f'<path d="M96 188 H160" stroke="{W}" stroke-width="9" stroke-linecap="round"/>'),
    'net.mkiol.Speech-Note': ('#E5603C', '#A8351F', 'Speech Note: a microphone with a sound wave.',
        f'<rect x="108" y="56" width="40" height="84" rx="20" fill="{W}"/>'
        f'<path d="M84 118 a44 44 0 0 0 88 0 M128 162 V190 M104 190 H152" fill="none" stroke="{W}" stroke-width="10" stroke-linecap="round"/>'),
    'org.nickvision.tagger': ('#5F8BE0', '#3452A8', 'Tagger: a tag and a music note.',
        f'<path d="M64 64 H132 L192 124 L132 184 L64 124 Z" fill="{W}"/>'
        f'<circle cx="92" cy="92" r="9" fill="#3452A8"/>'
        f'<path d="M128 150 V108 L156 102 V144" fill="none" stroke="#3452A8" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>'
        f'<circle cx="120" cy="152" r="9" fill="#3452A8"/><circle cx="148" cy="146" r="9" fill="#3452A8"/>'),
    'org.nickvision.money': ('#3EB86A', '#1E7A44', 'Money: a coin with a mark.',
        f'<circle cx="128" cy="128" r="62" fill="{W}"/>'
        f'<circle cx="128" cy="128" r="46" fill="none" stroke="#1E7A44" stroke-width="7" stroke-opacity=".5"/>'
        f'<path d="M144 106 C132 96 108 100 112 116 C116 132 146 122 144 142 C142 158 118 158 110 146" fill="none" stroke="#1E7A44" stroke-width="10" stroke-linecap="round"/>'
        f'<path d="M128 90 V166" stroke="#1E7A44" stroke-width="8" stroke-linecap="round"/>'),
    'org.kde.kasts': ('#4FA3E8', '#2A5FB0', 'Kasts: a podcast microphone with signal waves.',
        f'<circle cx="128" cy="116" r="20" fill="{W}"/>'
        f'<path d="M96 148 a44 44 0 1 1 64 0" fill="none" stroke="{W}" stroke-width="11" stroke-linecap="round"/>'
        f'<path d="M80 168 a68 68 0 1 1 96 0" fill="none" stroke="{W}" stroke-width="11" stroke-linecap="round" stroke-opacity=".6"/>'
        f'<path d="M128 140 V190 M108 190 H148" stroke="{W}" stroke-width="11" stroke-linecap="round"/>'),
}


def svg(name, top, bottom, note, glyph):
    gid = name.replace('.', '_').replace('-', '_')
    under = app_icon.encode(app_icon.shadow(), 'PNG')
    m, t, r = app_icon.MARGIN, app_icon.TILE, app_icon.RADIUS
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<!-- {note} Original work, fitted to the Colloid tile. -->\n'
        '<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
        'width="256" height="256" viewBox="0 0 256 256">\n'
        '  <defs>\n'
        f'    <clipPath id="tile"><rect x="{m}" y="{m}" width="{t}" height="{t}" rx="{r}"/></clipPath>\n'
        f'    <linearGradient id="{gid}" x1="0" y1="0" x2="0" y2="1">'
        f'<stop offset="0" stop-color="{top}"/><stop offset="1" stop-color="{bottom}"/></linearGradient>\n'
        '  </defs>\n'
        f'  <image width="256" height="256" xlink:href="data:image/png;base64,{under}"/>\n'
        '  <g clip-path="url(#tile)">\n'
        f'    <rect x="{m}" y="{m}" width="{t}" height="{t}" fill="url(#{gid})"/>\n'
        f'    <g>{glyph}</g>\n'
        '  </g>\n'
        '</svg>\n'
    )


def main():
    wanted = sys.argv[1:] or list(ICONS_DEF)
    for name in wanted:
        if name not in ICONS_DEF:
            sys.exit(f'{name}: not defined in this script')
        top, bottom, note, glyph = ICONS_DEF[name]
        if not app_icon.ICON_NAME.fullmatch(name):
            sys.exit(f'{name!r} is not an icon name')
        (ICONS / f'{name}.svg').write_text(svg(name, top, bottom, note, glyph), encoding='utf-8')
        print(f'wrote {name}.svg')


if __name__ == '__main__':
    main()
