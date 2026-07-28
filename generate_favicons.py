#!/usr/bin/env python3
"""Generate favicons for sheep5.net that fill the frame with no gaps.

Google search results crops favicons to a circle/rounded square. To look
"perfect" we fill the entire square with the brand color and draw the
globe so it touches the safe circular area with minimal padding.
"""

from PIL import Image, ImageDraw
import math
import os

# Brand color sampled from the original favicon
BRAND_RED = (194, 59, 15)       # #C23B0F
WHITE = (255, 255, 255)

OUTPUT_DIR = "static"


def _line_width(size):
    """Scale line width so it stays crisp at tiny sizes."""
    return max(1, int(round(size / 18)))


def draw_globe(draw, size, margin_factor=0.0):
    """Draw a white wire-frame globe that fills the canvas.

    Args:
        draw: PIL ImageDraw object.
        size: canvas width/height in px.
        margin_factor: tiny margin as fraction of size. 0 means edge-to-edge.
    """
    margin = int(size * margin_factor)
    x0, y0 = margin, margin
    x1, y1 = size - margin, size - margin

    cx = (x0 + x1) / 2
    cy = (y0 + y1) / 2
    r = (x1 - x0) / 2
    lw = _line_width(size)

    # Outer circle (the globe sphere)
    draw.ellipse([x0, y0, x1, y1], outline=WHITE, width=lw)

    if size <= 20:
        # 16x16: just a cross inside the circle reads better than a dense grid
        draw.line([(cx, y0), (cx, y1)], fill=WHITE, width=lw)
        draw.line([(x0, cy), (x1, cy)], fill=WHITE, width=lw)
        return

    # Vertical meridians: two ellipses left and right
    offset = r * 0.45
    for dx in (-offset, offset):
        bbox = [cx - r + abs(dx), y0, cx + r - abs(dx), y1]
        draw.ellipse(bbox, outline=WHITE, width=lw)

    if size <= 40:
        # 32x32: keep it readable
        draw.line([(cx, y0), (cx, y1)], fill=WHITE, width=lw)
        draw.line([(x0, cy), (x1, cy)], fill=WHITE, width=lw)
        return

    # Horizontal latitude lines for larger sizes
    for dy_mult in (-0.45, 0.0, 0.45):
        dy = cy + dy_mult * r
        chord = math.sqrt(max(0, r * r - (dy - cy) * (dy - cy)))
        draw.line([(cx - chord, dy), (cx + chord, dy)], fill=WHITE, width=lw)

    # Center vertical line (front meridian)
    draw.line([(cx, y0), (cx, y1)], fill=WHITE, width=lw)


def make_icon(size, margin_factor=0.0):
    img = Image.new("RGBA", (size, size), BRAND_RED + (255,))
    draw = ImageDraw.Draw(img)
    draw_globe(draw, size, margin_factor=margin_factor)
    return img


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    sizes = {
        "favicon-16x16.png": 16,
        "favicon-32x32.png": 32,
        "apple-touch-icon.png": 180,
        "favicon.png": 512,      # Google often picks this high-res PNG
    }

    for filename, size in sizes.items():
        img = make_icon(size, margin_factor=0.0)
        img.save(os.path.join(OUTPUT_DIR, filename), "PNG")
        print(f"Generated {filename} ({size}x{size})")

    # Also generate a 192x192 for PWA / Google high-res favicon if desired
    img = make_icon(192, margin_factor=0.0)
    img.save(os.path.join(OUTPUT_DIR, "favicon-192x192.png"), "PNG")
    print("Generated favicon-192x192.png (192x192)")


if __name__ == "__main__":
    main()
