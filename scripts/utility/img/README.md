# img-utils

Image utility scripts for cropping, optimizing, and converting images.

## Features

- 🔲 **img-crop** - Crop images by removing pixels from edges (toolbars, docks, etc.)
- 🖼️ **img-optimize** - Convert and optimize images (PNG→JPG, quality settings)

## Installation

No installation needed! Just use `uv run`:

```bash
# From the repo root
uv run --directory ./scripts/utility/img img-crop --help
uv run --directory ./scripts/utility/img img-optimize --help
```

## Usage

### Crop Images

Remove UI elements like toolbars and docks from screenshots:

```bash
# Crop 95px from top (toolbar) and 33px from bottom (dock)
uv run --directory ./scripts/utility/img \
  img-crop screenshot.png --top 95 --bottom 33

# Specify output file
uv run --directory ./scripts/utility/img \
  img-crop screenshot.png -o cropped.png --top 100

# Crop all edges
uv run --directory ./scripts/utility/img \
  img-crop image.png --top 10 --bottom 10 --left 20 --right 20
```

### Optimize Images

Convert and compress images for web use:

```bash
# Convert PNG to optimized JPG (default quality 85)
uv run --directory ./scripts/utility/img \
  img-optimize screenshot.png

# Specify output and quality
uv run --directory ./scripts/utility/img \
  img-optimize screenshot.png -o final.jpg --quality 90

# Convert to WebP for maximum compression
uv run --directory ./scripts/utility/img \
  img-optimize photo.png -o photo.webp --quality 80
```

## Example: Screenshot Processing Pipeline

Process a screenshot by cropping UI elements and converting to optimized JPG:

```bash
# Step 1: Crop out toolbar and dock
uv run --directory ./scripts/utility/img \
  img-crop ./assets/img/screenshot.png \
  --top 95 --bottom 33 \
  -o ./assets/img/screenshot_cropped.png

# Step 2: Convert to optimized JPG
uv run --directory ./scripts/utility/img \
  img-optimize ./assets/img/screenshot_cropped.png \
  -o ./assets/img/screenshot.jpg --quality 85
```

## Development

Run tests:

```bash
cd scripts/utility/img
uv run pytest -v
```

## License

MIT License
