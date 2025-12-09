# Image Processing Scripts

## png2jpg.py

Converts PNG screenshots to optimized JPG format for web use. This is essential for reducing file sizes while maintaining good visual quality on the website.

### Features

- ✅ Converts PNG to JPG with customizable quality
- ✅ Handles transparency (converts to white background)
- ✅ Optimizes for web with progressive JPG
- ✅ Shows file size savings
- ✅ Outputs JPG in same location as source PNG
- ✅ **Keeps original PNG by default** (safer, version control friendly)

### Requirements

- Python 3.6+
- Pillow (PIL) library

The dev container already has Pillow installed. If running locally, install with:
```bash
pip install Pillow
```

### Usage

#### Basic conversion (keeps PNG):
```bash
python3 scripts/image/png2jpg.py path/to/screenshot.png
```

#### Specify quality (1-100, default is 85):
```bash
python3 scripts/image/png2jpg.py path/to/screenshot.png --quality 90
```

#### Delete the original PNG file after conversion:
```bash
python3 scripts/image/png2jpg.py path/to/screenshot.png --delete-png
```

#### Combined options:
```bash
python3 scripts/image/png2jpg.py path/to/screenshot.png --quality 90 --delete-png
```

### Quality Guidelines

- **85** (default): Good balance of quality and file size for most screenshots
- **90-95**: Higher quality for detailed images or hero images
- **75-80**: Smaller files when maximum quality isn't critical
- **100**: Maximum quality (not recommended, file size is much larger)

### Examples

Convert a project screenshot (keeps PNG):
```bash
python3 scripts/image/png2jpg.py assets/img/alpine-resume-screenshot.png
```

Convert with higher quality and delete original:
```bash
python3 scripts/image/png2jpg.py assets/img/hero-image.png --quality 92 --delete-png
```

### Output Example

```
Converting: screenshot.png
Quality: 85
Original size: 2,458,392 bytes (2.34 MB)
New size: 324,156 bytes (0.31 MB)
Savings: 2,134,236 bytes (86.8%)
Created: /path/to/screenshot.jpg
Kept original PNG: screenshot.png

✓ Conversion successful!
```

### Design Philosophy

**By default, the script keeps the original PNG** to:
- Prevent accidental data loss
- Allow comparison between formats
- Maintain source files for future re-processing
- Be version control friendly

Use `--delete-png` only when you're certain you want to remove the original.

### Notes

- JPG doesn't support transparency. PNG images with transparency will be converted to white backgrounds.
- Progressive JPG format is used for better loading on web pages (loads incrementally).
- The `optimize` flag is enabled for additional file size reduction.
- Original PNG is **kept by default** for safety. Use `--delete-png` to remove it after conversion.

### Troubleshooting

**Error: PNG file not found**
- Check the file path is correct
- Use absolute or relative paths from your current directory

**Error: File must be a PNG image**
- The script only accepts `.png` files
- Check the file extension

**Error: Quality must be between 1 and 100**
- Use a quality value between 1-100
- Default is 85 if not specified