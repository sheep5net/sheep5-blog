#!/usr/bin/env python3
"""Generate favicons for sheep5.net from a source PNG.

Usage: place the source icon at static/favicon-source.png and run this script.
It will resize the source to common favicon sizes while preserving transparency.
"""

from PIL import Image
import os

OUTPUT_DIR = "static"
SOURCE = "static/favicon-source.png"

SIZES = {
    "favicon-16x16.png": 16,
    "favicon-32x32.png": 32,
    "apple-touch-icon.png": 180,
    "favicon-192x192.png": 192,
    "favicon.png": 512,
}


def generate():
    if not os.path.exists(SOURCE):
        raise FileNotFoundError(f"Source icon not found: {SOURCE}")

    src = Image.open(SOURCE).convert("RGBA")
    # Ensure source is square by center-cropping to the smaller dimension
    w, h = src.size
    if w != h:
        side = min(w, h)
        left = (w - side) // 2
        top = (h - side) // 2
        src = src.crop((left, top, left + side, top + side))

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for filename, size in SIZES.items():
        resized = src.resize((size, size), Image.Resampling.LANCZOS)
        out_path = os.path.join(OUTPUT_DIR, filename)
        resized.save(out_path, "PNG")
        print(f"Generated {out_path} ({size}x{size})")


if __name__ == "__main__":
    generate()
