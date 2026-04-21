#!/usr/bin/env python3
"""
Combine OWASP-6.jpg and OWASP-7.jpg into a single panoramic hero image.

Expected input files (place in the same directory as this script):
  - OWASP-6.jpg  -> LEFT half  ("Global Expertise. Stronger Together.")
  - OWASP-7.jpg  -> RIGHT half (group photo with OWASP LAHORE + tkxel logos)

Output:
  - owasp-lahore-hero.jpg  (side-by-side, same height)

Usage:
  cd assets/images/content/owasp-lahore
  python3 combine_hero.py
"""
from pathlib import Path
from PIL import Image

HERE = Path(__file__).parent
LEFT = HERE / "OWASP-6.jpg"
RIGHT = HERE / "OWASP-7.jpg"
OUT = HERE / "owasp-lahore-hero.jpg"


def main() -> None:
    if not LEFT.exists() or not RIGHT.exists():
        missing = [str(p) for p in (LEFT, RIGHT) if not p.exists()]
        raise SystemExit(f"Missing input file(s): {missing}")

    left = Image.open(LEFT).convert("RGB")
    right = Image.open(RIGHT).convert("RGB")

    target_height = min(left.height, right.height)

    def resize_to_height(img: Image.Image, h: int) -> Image.Image:
        if img.height == h:
            return img
        new_width = int(img.width * (h / img.height))
        return img.resize((new_width, h), Image.LANCZOS)

    left = resize_to_height(left, target_height)
    right = resize_to_height(right, target_height)

    combined = Image.new("RGB", (left.width + right.width, target_height))
    combined.paste(left, (0, 0))
    combined.paste(right, (left.width, 0))
    combined.save(OUT, "JPEG", quality=90, optimize=True)
    print(f"Wrote {OUT} ({combined.size[0]}x{combined.size[1]})")


if __name__ == "__main__":
    main()
