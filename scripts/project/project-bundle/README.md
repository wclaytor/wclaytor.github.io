# Alpine Resume - Project Bundle Scripts

This directory contains scripts to package and deploy the Alpine Resume application to your GitHub Pages site.

## Overview

These scripts simplify the process of deploying Alpine Resume from your private development repository to your public GitHub Pages site (`wclaytor.github.io`).

**What gets bundled:**
- Core application files (`index.html`, `sw.js`, `manifest.json`)
- Styling (`styles/` directory)
- Icons and assets (`icons/` directory)
- Documentation (`LICENSE.md`, `README.md`, `CHANGELOG.md`)
- Offline demo (`offline-demo.html`)
- Version information (`version.json`)

**What doesn't get bundled:**
- Development files (`tests/`, `docs/`, `examples/`)
- Build configuration (`package.json`, `playwright.config.js`)
- Git and CI/CD files (`.github/`, `.gitignore`)
- Scripts and tooling (`scripts/`)
- Skills and templates (`skills/`)

## Scripts

### `project-bundle.py`

Creates a compressed tar.gz archive containing all files needed for deployment.

**Basic Usage:**
```bash
# From anywhere in the alpine-resume repository
python scripts/project/project-bundle/project-bundle.py
```

**Advanced Usage:**
```bash
# Custom output filename
python project-bundle.py --output my-custom-bundle.tar.gz

# With timestamp

python project-bundle.py --output alpine-resume-$(date +%Y%m%d).tar.gz
# Show help
python project-bundle.py --help
```

**Output:**
- Creates `alpine-resume-bundle.tar.gz` in the current directory
- Shows list of bundled files
- Displays bundle size

### `project-bundle-extract.py`

Extracts the bundle into your GitHub Pages repository structure.

**Basic Usage:**
```bash
# From your wclaytor.github.io repository
python project-bundle-extract.py
```

This will extract files to `projects/alpine-resume/` by default.

**Advanced Usage:**
```bash
# Custom input bundle and target directory
python project-bundle-extract.py --input my-bundle.tar.gz --target custom/path

# Preview what would be extracted (dry run)
python project-bundle-extract.py --dry-run

# List bundle contents without extracting
python project-bundle-extract.py --list

# Force overwrite without prompting
python project-bundle-extract.py --force

# Show help
python project-bundle-extract.py --help
```

**Options:**
- `--input, -i`: Specify bundle filename (default: `alpine-resume-bundle.tar.gz`)
- `--target, -t`: Specify target directory (default: `projects/alpine-resume`)
- `--force, -f`: Overwrite existing files without confirmation
- `--dry-run`: Preview extraction without making changes
- `--list, -l`: Show bundle contents without extracting

## Deployment Workflow

### Step 1: Create the Bundle (Development Repo)

```bash
# Navigate to your alpine-resume repository
cd /path/to/alpine-resume

# Create the deployment bundle
python scripts/project/project-bundle/project-bundle.py

# This creates: alpine-resume-bundle.tar.gz
```

### Step 2: Transfer the Bundle

Copy the bundle to your GitHub Pages repository:

```bash
# Copy bundle to your wclaytor.github.io repository
cp alpine-resume-bundle.tar.gz /path/to/wclaytor.github.io/
```

Or use your preferred method:
- Git LFS (if the bundle is large)
- Cloud storage (Dropbox, Google Drive)
- Direct download from CI/CD artifacts
- SCP/SFTP to remote server

### Step 3: Extract the Bundle (GitHub Pages Repo)

```bash
# Navigate to your GitHub Pages repository
cd /path/to/wclaytor.github.io

# Extract the bundle
python project-bundle-extract.py

# Or copy the script first if needed
cp /path/to/alpine-resume/scripts/project/project-bundle/project-bundle-extract.py .
python project-bundle-extract.py
```

### Step 4: Test and Deploy

```bash
# Test locally (optional)
python -m http.server 8000
# Open http://localhost:8000/projects/alpine-resume/

# Commit and push to GitHub
git add projects/alpine-resume/
git commit -m "Update Alpine Resume application"
git push origin main

# Your site will be live at:
# https://wclaytor.github.io/projects/alpine-resume/
```

## Quick Reference

### One-Line Bundle Creation
```bash
cd alpine-resume && python scripts/project/project-bundle/project-bundle.py
```

### One-Line Extraction
```bash
cd wclaytor.github.io && python project-bundle-extract.py
```

### Complete Workflow (One Command Block)
```bash
# In alpine-resume repo
cd /path/to/alpine-resume
python scripts/project/project-bundle/project-bundle.py
cp alpine-resume-bundle.tar.gz /path/to/wclaytor.github.io/

# In wclaytor.github.io repo
cd /path/to/wclaytor.github.io
python project-bundle-extract.py
git add projects/alpine-resume/
git commit -m "Update Alpine Resume to $(date +%Y-%m-%d)"
git push
```

## Advanced Features

### Preview Before Extracting
```bash
# See what files would be extracted
python project-bundle-extract.py --dry-run

# List bundle contents
python project-bundle-extract.py --list
```

### Automated Deployment Script

Create a deployment script in your alpine-resume repo:

```bash
#!/bin/bash
# deploy.sh

set -e

PAGES_REPO="/path/to/wclaytor.github.io"
BUNDLE_NAME="alpine-resume-$(date +%Y%m%d-%H%M%S).tar.gz"

echo "📦 Creating bundle..."
python scripts/project/project-bundle/project-bundle.py --output "$BUNDLE_NAME"

echo "📋 Copying to GitHub Pages repo..."
cp "$BUNDLE_NAME" "$PAGES_REPO/"

echo "📂 Extracting..."
cd "$PAGES_REPO"
python project-bundle-extract.py --input "$BUNDLE_NAME" --force

echo "🚀 Deploying..."
git add projects/alpine-resume/
git commit -m "Update Alpine Resume ($(date +%Y-%m-%d))"
git push

echo "✅ Deployment complete!"
echo "🌐 Live at: https://wclaytor.github.io/projects/alpine-resume/"

# Cleanup
rm "$BUNDLE_NAME"
```

Make it executable:
```bash
chmod +x deploy.sh
./deploy.sh
```

### CI/CD Integration

Add to your GitHub Actions workflow:

```yaml
name: Create Deployment Bundle

on:
  push:
    branches: [main]

jobs:
  bundle:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Create deployment bundle
        run: python scripts/project/project-bundle/project-bundle.py
      
      - name: Upload bundle as artifact
        uses: actions/upload-artifact@v3
        with:
          name: alpine-resume-bundle
          path: alpine-resume-bundle.tar.gz
```

## Troubleshooting

### "Project root not found" error
**Solution**: Run the script from within the alpine-resume repository, or ensure `index.html` exists in the project root.

### "Bundle file not found" error
**Solution**: Make sure you're in the correct directory and the bundle filename matches the `--input` parameter.

### Permission errors during extraction
**Solution**: Ensure you have write permissions in the target directory, or use `sudo` if necessary.

### Files not updating after extraction
**Solution**: Use `--force` flag to overwrite without prompting, or delete the target directory first.

## File Size Considerations

Typical bundle sizes:
- **Base application**: ~50-100 KB (HTML, CSS, JS)
- **Icons and assets**: ~200-500 KB (PNG files, favicon, splash screens)
- **Total bundle**: ~500 KB - 1 MB (compressed)

The bundle is optimized to include only production files, keeping deployment lean and fast.

## Manual Alternative

If you prefer not to use these scripts, you can manually tar/untar:

```bash
# Create bundle manually
cd alpine-resume
tar -czf alpine-resume-bundle.tar.gz \
  index.html manifest.json sw.js version.json offline-demo.html \
  styles/ icons/ LICENSE.md README.md CHANGELOG.md

# Extract manually
cd wclaytor.github.io
tar -xzf alpine-resume-bundle.tar.gz -C projects/alpine-resume/
```

However, the Python scripts provide:
- ✅ Validation and error checking
- ✅ Progress feedback
- ✅ Safety prompts before overwriting
- ✅ Automatic directory creation
- ✅ Dry-run and preview modes
- ✅ Consistent file permissions

## Support

For issues or questions:
- Check the [main project documentation](../../../README.md)
- Review [deployment guide](../../../docs/guides/DEPLOYMENT-GUIDE.md)
- Open an issue in the repository

## Version

These scripts are designed for Alpine Resume v1.x and Python 3.7+.

**Last Updated**: December 9, 2025
