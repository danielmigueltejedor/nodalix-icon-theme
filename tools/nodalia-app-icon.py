#!/usr/bin/env python3
"""Fit a Nodalia app portrait to the Colloid application-icon grid.

Colloid draws every application tile at 224 px inside a 256 px canvas (a
16 px margin), with a 51.5 px corner radius and a soft shadow 5 px below it.
Those numbers were measured from Colloid's own renders, so a Nodalia icon
made here sits in the app grid exactly like the icons around it.

Usage: nodalia-app-icon.py SOURCE OUTPUT.svg [--comment TEXT]

SOURCE is the app's artwork: a full-bleed square, or a tile with its own
margin and shadow (that tile is cropped out first). Needs Pillow.
"""
import argparse
import base64
import io
import sys

from PIL import Image, ImageDraw, ImageFilter

CANVAS, MARGIN, RADIUS = 256, 16, 51.5
SHADOW_OFFSET, SHADOW_BLUR, SHADOW_OPACITY = 5, 3.5, 0.144
TILE = CANVAS - 2 * MARGIN
ART = 2 * TILE  # sharp at 2x scaling of the largest common size
QUALITY = 90


def artwork(path):
    image = Image.open(path).convert('RGBA')
    opaque = image.getchannel('A').point(lambda v: 255 if v > 250 else 0)
    box = opaque.getbbox()
    if box is None:
        sys.exit(f'{path}: the image is fully transparent')
    left, top, right, bottom = box
    if (right - left, bottom - top) != image.size:
        # A tile with its own margin: keep the tile, drop its edge pixels.
        inset = max(1, round((right - left) / 256))
        image = image.crop((left + inset, top + inset, right - inset, bottom - inset))
    # Corners outside the tile are clipped away; fill them so JPEG has no seams.
    backing = Image.new('RGBA', image.size, image.getpixel((image.width // 2, 0)))
    flat = Image.alpha_composite(backing, image).convert('RGB')
    return flat.resize((ART, ART), Image.LANCZOS)


def shadow():
    # Drawn as an image rather than an SVG blur filter: not every icon
    # renderer applies filters, and one that skips it draws a hard slab.
    scale = 2
    size = CANVAS * scale
    mask = Image.new('L', (size, size), 0)
    top = (MARGIN + SHADOW_OFFSET) * scale
    ImageDraw.Draw(mask).rounded_rectangle(
        (MARGIN * scale, top, (MARGIN + TILE) * scale, top + TILE * scale),
        radius=RADIUS * scale, fill=round(255 * SHADOW_OPACITY))
    mask = mask.filter(ImageFilter.GaussianBlur(SHADOW_BLUR * scale))
    layer = Image.new('LA', (size, size), 0)
    layer.putalpha(mask)
    return layer


def encode(image, kind, **options):
    buffer = io.BytesIO()
    image.save(buffer, kind, optimize=True, **options)
    return base64.b64encode(buffer.getvalue()).decode()


def svg(art, comment):
    data = encode(art, 'JPEG', quality=QUALITY, progressive=True)
    under = encode(shadow(), 'PNG')
    tile = f'x="{MARGIN}" width="{TILE}" height="{TILE}" rx="{RADIUS}"'
    note = f'<!-- {comment} -->\n' if comment else ''
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'{note}'
        f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
        f'width="{CANVAS}" height="{CANVAS}" viewBox="0 0 {CANVAS} {CANVAS}">\n'
        '  <defs>\n'
        f'    <clipPath id="tile"><rect y="{MARGIN}" {tile}/></clipPath>\n'
        '  </defs>\n'
        f'  <image width="{CANVAS}" height="{CANVAS}" '
        f'xlink:href="data:image/png;base64,{under}"/>\n'
        f'  <image x="{MARGIN}" y="{MARGIN}" width="{TILE}" height="{TILE}" '
        f'clip-path="url(#tile)" xlink:href="data:image/jpeg;base64,{data}"/>\n'
        '</svg>\n'
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('source')
    parser.add_argument('output')
    parser.add_argument('--comment', default='')
    args = parser.parse_args()
    if '--' in args.comment:
        sys.exit('--comment cannot contain "--" (it ends an XML comment)')
    with open(args.output, 'w', encoding='utf-8') as stream:
        stream.write(svg(artwork(args.source), args.comment))


if __name__ == '__main__':
    main()
