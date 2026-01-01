#!/usr/bin/env python3
"""
Crop images by removing specified pixels from edges.

Supports automatic detection of common UI elements like toolbars and docks,
or manual specification of crop values.
"""
import argparse
from pathlib import Path
from PIL import Image


def crop_image(
    input_path: str | Path,
    output_path: str | Path | None = None,
    top: int = 0,
    bottom: int = 0,
    left: int = 0,
    right: int = 0,
) -> Path:
    """
    Crop an image by removing pixels from edges.

    Args:
        input_path: Path to the input image
        output_path: Path for output (default: same name with _cropped suffix)
        top: Pixels to remove from top
        bottom: Pixels to remove from bottom
        left: Pixels to remove from left
        right: Pixels to remove from right

    Returns:
        Path to the output file
    """
    input_path = Path(input_path)

    if output_path is None:
        output_path = input_path.with_stem(f"{input_path.stem}_cropped")
    else:
        output_path = Path(output_path)

    with Image.open(input_path) as img:
        width, height = img.size

        # Calculate crop box (left, upper, right, lower)
        box = (
            left,
            top,
            width - right,
            height - bottom,
        )

        cropped = img.crop(box)

        # Ensure output directory exists
        output_path.parent.mkdir(parents=True, exist_ok=True)

        cropped.save(output_path)

        print(f"✂️  Cropped: {input_path.name}")
        print(f"   Original: {width}x{height}")
        print(f"   Cropped:  {cropped.width}x{cropped.height}")
        print(f"   Output:   {output_path}")

    return output_path


def main():
    """CLI entry point for img-crop command."""
    parser = argparse.ArgumentParser(
        description="Crop images by removing pixels from edges",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Crop 95px from top and 33px from bottom (remove toolbar and dock)
  img-crop screenshot.png --top 95 --bottom 33
  
  # Crop and specify output file
  img-crop screenshot.png -o cropped.jpg --top 100
  
  # Crop all edges
  img-crop image.png --top 10 --bottom 10 --left 20 --right 20
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
        help="Output file path (default: input_cropped.ext)",
    )
    parser.add_argument(
        "--top",
        type=int,
        default=0,
        help="Pixels to remove from top (default: 0)",
    )
    parser.add_argument(
        "--bottom",
        type=int,
        default=0,
        help="Pixels to remove from bottom (default: 0)",
    )
    parser.add_argument(
        "--left",
        type=int,
        default=0,
        help="Pixels to remove from left (default: 0)",
    )
    parser.add_argument(
        "--right",
        type=int,
        default=0,
        help="Pixels to remove from right (default: 0)",
    )

    args = parser.parse_args()

    if not args.input.exists():
        print(f"❌ Error: Input file not found: {args.input}")
        return 1

    try:
        crop_image(
            input_path=args.input,
            output_path=args.output,
            top=args.top,
            bottom=args.bottom,
            left=args.left,
            right=args.right,
        )
        return 0
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1


if __name__ == "__main__":
    exit(main())
