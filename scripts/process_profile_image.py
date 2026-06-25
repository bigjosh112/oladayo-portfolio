#!/usr/bin/env python3
"""Process uploaded portrait into hero profile and favicon assets."""

from __future__ import annotations

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
ASSETS_DIR = Path("/Users/dayo/.cursor/projects/Users-dayo-timi-new-portfolio/assets")
PUBLIC_DIR = ROOT / "public"

PROFILE_MAX_WIDTH = 800
FAVICON_SIZE = 192


def find_source_image() -> Path:
    matches = sorted(ASSETS_DIR.glob("fine_boy*.png"))
    if not matches:
        raise FileNotFoundError(f"No fine_boy portrait found in {ASSETS_DIR}")
    return matches[0]


def save_profile_image(source: Image.Image, output: Path) -> None:
    image = source.copy()
    if image.width > PROFILE_MAX_WIDTH:
        ratio = PROFILE_MAX_WIDTH / image.width
        new_size = (PROFILE_MAX_WIDTH, int(image.height * ratio))
        image = image.resize(new_size, Image.Resampling.LANCZOS)
    image.save(output, format="PNG", optimize=True)


def save_favicon_image(source: Image.Image, output: Path) -> None:
    width, height = source.size
    crop_size = min(width, int(height * 0.55))
    left = (width - crop_size) // 2
    top = int(height * 0.08)
    right = left + crop_size
    bottom = top + crop_size
    cropped = source.crop((left, top, right, bottom))
    favicon = cropped.resize((FAVICON_SIZE, FAVICON_SIZE), Image.Resampling.LANCZOS)
    favicon.save(output, format="PNG", optimize=True)


def main() -> None:
    source_path = find_source_image()
    PUBLIC_DIR.mkdir(parents=True, exist_ok=True)

    with Image.open(source_path) as image:
        image = image.convert("RGB")
        profile_path = PUBLIC_DIR / "profile.png"
        favicon_path = PUBLIC_DIR / "favicon.png"
        legacy_path = PUBLIC_DIR / "jsm-logo.png"

        save_profile_image(image, profile_path)
        save_favicon_image(image, favicon_path)
        save_favicon_image(image, legacy_path)

    print(f"Source: {source_path}")
    print(f"Wrote: {profile_path}")
    print(f"Wrote: {favicon_path}")
    print(f"Wrote: {legacy_path}")


if __name__ == "__main__":
    main()
