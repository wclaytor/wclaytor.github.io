#!/usr/bin/env python3
"""
Optimize images by converting format and adjusting quality.

Supports PNG to JPG conversion with quality settings.
"""
import argparse
from pathlib import Path
from PIL import Image


def optimize_image(
    input_path: str | Path,
    output_path: str | Path | None = None,
    quality: int = 85,
    format: str | None = None,
) -> Path:
    """
    Optimize an image by converting format and/or adjusting quality.

    Args:
        input_path: Path to the input image
        output_path: Path for output (default: same name, jpg extension)
        quality: JPEG quality (1-100, default: 85)
        format: Output format (default: infer from output_path or 'JPEG')

    Returns:
        Path to the output file
    """
    input_path = Path(input_path)

    # Determine output path and format
    if output_path is None:
        output_path = input_path.with_suffix(".jpg")
    else:
        output_path = Path(output_path)

    # Infer format from extension if not specified
    if format is None:
        ext = output_path.suffix.lower()
        format_map = {
            ".jpg": "JPEG",
            ".jpeg": "JPEG",
            ".png": "PNG",
            ".webp": "WEBP",
            ".gif": "GIF",
        }
        format = format_map.get(ext, "JPEG")

    with Image.open(input_path) as img:
        original_size = input_path.stat().st_size

        # Convert RGBA to RGB if saving as JPEG
        if format == "JPEG" and img.mode in ("RGBA", "P"):
            # Create white background
            background = Image.new("RGB", img.size, (255, 255, 255))
            if img.mode == "P":
                img = img.convert("RGBA")
            background.paste(img, mask=img.split()[
                             3] if len(img.split()) == 4 else None)
            img = background

        # Ensure output directory exists
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Save with optimization
        save_kwargs = {"optimize": True}
        if format == "JPEG":
            save_kwargs["quality"] = quality
        elif format == "WEBP":
            save_kwargs["quality"] = quality

        img.save(output_path, format=format, **save_kwargs)

        new_size = output_path.stat().st_size
        reduction = ((original_size - new_size) / original_size) * 100

        print(f"🖼️  Optimized: {input_path.name}")
        print(f"   Format:   {format} (quality: {quality})")
        print(f"   Original: {original_size:,} bytes")
        print(f"   New:      {new_size:,} bytes ({reduction:.1f}% reduction)")
        print(f"   Output:   {output_path}")

    return output_path


def main():
    """CLI entry point for img-optimize command."""
    parser = argparse.ArgumentParser(
        description="Optimize images by converting format and adjusting quality",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Convert PNG to optimized JPG (default quality 85)
  img-optimize screenshot.png
  
  # Specify output and quality
  img-optimize screenshot.png -o final.jpg --quality 90
  
  # Convert to WebP for maximum compression
  img-optimize photo.png -o photo.webp --quality 80
        """,
    )

    parser.add_argument(
        "input",
        type=Path,
        help="Input image file",
    )
    parser.add_argument(
        "-o", "--output",
        type=Path,
        default=None,
        help="Output file path (default: input.jpg)",
    )
    parser.add_argument(
        "-q", "--quality",
        type=int,
        default=85,
        help="Output quality 1-100 (default: 85)",
    )
    parser.add_argument(
        "-f", "--format",
        type=str,
        choices=["JPEG", "PNG", "WEBP", "GIF"],
        default=None,
        help="Output format (default: infer from extension)",
    )

    args = parser.parse_args()

    if not args.input.exists():
        print(f"❌ Error: Input file not found: {args.input}")
        return 1

    try:
        optimize_image(
            input_path=args.input,
            output_path=args.output,
            quality=args.quality,
            format=args.format,
        )
        return 0
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1


if __name__ == "__main__":
    exit(main())
