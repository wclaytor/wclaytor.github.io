#!/usr/bin/env python3
"""
PNG to JPG Converter for wclaytor.github.io
Converts PNG screenshots to optimized JPG format for web use.

Usage:
    python png2jpg.py <path_to_png_file> [--quality QUALITY] [--delete-png]

Arguments:
    path_to_png_file    Path to the PNG file to convert
    --quality           JPG quality (1-100, default: 85)
    --delete-png        Delete the original PNG file after conversion

Example:
    python png2jpg.py screenshot.png
    python png2jpg.py screenshot.png --quality 90
    python png2jpg.py screenshot.png --quality 90 --delete-png
"""

import argparse
import os
import sys
from pathlib import Path
from PIL import Image


def convert_png_to_jpg(png_path, quality=85, delete_png=False):
    """
    Convert PNG image to optimized JPG format.
    
    Args:
        png_path (str): Path to the PNG file
        quality (int): JPG quality (1-100, default 85)
        delete_png (bool): Whether to delete the original PNG file
        
    Returns:
        str: Path to the created JPG file
        
    Raises:
        FileNotFoundError: If PNG file doesn't exist
        ValueError: If file is not a PNG or quality is out of range
    """
    # Validate inputs
    png_path = Path(png_path)
    
    if not png_path.exists():
        raise FileNotFoundError(f"PNG file not found: {png_path}")
    
    if png_path.suffix.lower() != '.png':
        raise ValueError(f"File must be a PNG image: {png_path}")
    
    if not 1 <= quality <= 100:
        raise ValueError(f"Quality must be between 1 and 100, got: {quality}")
    
    # Create JPG path (same location, different extension)
    jpg_path = png_path.with_suffix('.jpg')
    
    print(f"Converting: {png_path.name}")
    print(f"Quality: {quality}")
    
    try:
        # Open PNG image
        with Image.open(png_path) as img:
            # Get original size
            original_size = png_path.stat().st_size
            print(f"Original size: {original_size:,} bytes ({original_size / 1024 / 1024:.2f} MB)")
            
            # Convert RGBA to RGB if necessary (JPG doesn't support transparency)
            if img.mode in ('RGBA', 'LA', 'P'):
                # Create white background
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'P':
                    img = img.convert('RGBA')
                background.paste(img, mask=img.split()[-1] if img.mode in ('RGBA', 'LA') else None)
                img = background
            elif img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Save as JPG with optimization
            img.save(
                jpg_path,
                'JPEG',
                quality=quality,
                optimize=True,
                progressive=True  # Progressive JPG for better web loading
            )
        
        # Get new size and calculate savings
        new_size = jpg_path.stat().st_size
        savings = original_size - new_size
        savings_percent = (savings / original_size) * 100
        
        print(f"New size: {new_size:,} bytes ({new_size / 1024 / 1024:.2f} MB)")
        print(f"Savings: {savings:,} bytes ({savings_percent:.1f}%)")
        print(f"Created: {jpg_path}")
        
        # Delete original PNG if requested
        if delete_png:
            png_path.unlink()
            print(f"Deleted original PNG: {png_path.name}")
        else:
            print(f"Kept original PNG: {png_path.name}")
        
        return str(jpg_path)
        
    except Exception as e:
        # Clean up partial JPG if conversion failed
        if jpg_path.exists():
            jpg_path.unlink()
        raise Exception(f"Error converting image: {e}")


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description='Convert PNG screenshots to optimized JPG format for web use.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s screenshot.png
  %(prog)s screenshot.png --quality 90
  %(prog)s screenshot.png --quality 90 --delete-png
  %(prog)s /path/to/screenshot.png --quality 85
        """
    )
    
    parser.add_argument(
        'png_path',
        help='Path to the PNG file to convert'
    )
    
    parser.add_argument(
        '--quality',
        type=int,
        default=85,
        help='JPG quality (1-100, default: 85). Higher = better quality but larger file.'
    )
    
    parser.add_argument(
        '--delete-png',
        action='store_true',
        help='Delete the original PNG file after conversion (default: keeps PNG)'
    )
    
    args = parser.parse_args()
    
    try:
        jpg_path = convert_png_to_jpg(args.png_path, args.quality, args.delete_png)
        print("\n✓ Conversion successful!")
        return 0
        
    except FileNotFoundError as e:
        print(f"\n✗ Error: {e}", file=sys.stderr)
        return 1
        
    except ValueError as e:
        print(f"\n✗ Error: {e}", file=sys.stderr)
        return 1
        
    except Exception as e:
        print(f"\n✗ Error: {e}", file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())