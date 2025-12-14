#!/usr/bin/env python3
"""
Alpine Resume - Project Bundle Creator

This script creates a deployment bundle containing only the files needed
to run the Alpine Resume application on a web server (e.g., GitHub Pages).

Usage:
    python project-bundle.py [--output OUTPUT_FILE]

Options:
    --output, -o    Output filename (default: alpine-resume-bundle.tar.gz)
    --help, -h      Show this help message
"""

import os
import sys
import tarfile
import argparse
from pathlib import Path
from datetime import datetime


# Files and directories to include in the bundle
BUNDLE_INCLUDES = [
    'index.html',
    'manifest.json',
    'sw.js',
    'version.json',
    'offline-demo.html',
    'styles/',
    'icons/',
    'LICENSE.md',
]

# Optional files to include if they exist
OPTIONAL_INCLUDES = [
    'CHANGELOG.md',
    'README.md',
]


def get_project_root():
    """Find the project root directory (where index.html is located)."""
    current_dir = Path(__file__).resolve().parent
    
    # Walk up the directory tree to find the project root
    while current_dir != current_dir.parent:
        if (current_dir / 'index.html').exists():
            return current_dir
        current_dir = current_dir.parent
    
    raise FileNotFoundError("Could not find project root (index.html not found)")


def collect_files(project_root):
    """
    Collect all files that should be included in the bundle.
    
    Returns:
        list: List of Path objects representing files to bundle
    """
    files_to_bundle = []
    
    for item in BUNDLE_INCLUDES:
        path = project_root / item
        
        if not path.exists():
            print(f"⚠️  Warning: Required file/directory not found: {item}")
            continue
        
        if path.is_file():
            files_to_bundle.append(path)
        elif path.is_dir():
            # Recursively add all files in the directory
            for file_path in path.rglob('*'):
                if file_path.is_file():
                    files_to_bundle.append(file_path)
    
    # Add optional files if they exist
    for item in OPTIONAL_INCLUDES:
        path = project_root / item
        if path.exists() and path.is_file():
            files_to_bundle.append(path)
    
    return files_to_bundle


def create_bundle(project_root, output_file, files):
    """
    Create a tar.gz bundle with the specified files.
    
    Args:
        project_root: Path to the project root directory
        output_file: Path to the output bundle file
        files: List of file paths to include
    """
    print(f"📦 Creating deployment bundle: {output_file}")
    print(f"📂 Project root: {project_root}")
    print(f"📄 Files to bundle: {len(files)}")
    print()
    
    # Create the tar.gz file
    with tarfile.open(output_file, 'w:gz') as tar:
        for file_path in sorted(files):
            # Get the relative path from project root
            arcname = file_path.relative_to(project_root)
            
            # Add file to archive
            tar.add(file_path, arcname=str(arcname))
            print(f"  ✓ {arcname}")
    
    # Get file size
    size_bytes = os.path.getsize(output_file)
    size_kb = size_bytes / 1024
    size_mb = size_kb / 1024
    
    if size_mb >= 1:
        size_str = f"{size_mb:.2f} MB"
    else:
        size_str = f"{size_kb:.2f} KB"
    
    print()
    print(f"✅ Bundle created successfully!")
    print(f"📊 Bundle size: {size_str}")
    print(f"📦 Output file: {output_file}")
    print()
    print("Next steps:")
    print("1. Copy this bundle to your wclaytor.github.io repository")
    print("2. Run project-bundle-extract.py in the target directory")
    print("3. The files will be extracted to projects/alpine-resume/")


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description='Create a deployment bundle for Alpine Resume',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Create bundle with default name
  python project-bundle.py
  
  # Create bundle with custom name
  python project-bundle.py --output my-bundle.tar.gz
  
  # Create bundle with timestamp
  python project-bundle.py --output alpine-resume-$(date +%Y%m%d).tar.gz
        """
    )
    
    parser.add_argument(
        '--output', '-o',
        default='alpine-resume-bundle.tar.gz',
        help='Output filename (default: alpine-resume-bundle.tar.gz)'
    )
    
    args = parser.parse_args()
    
    try:
        # Find project root
        project_root = get_project_root()
        
        # Collect files to bundle
        files = collect_files(project_root)
        
        if not files:
            print("❌ Error: No files found to bundle")
            return 1
        
        # Resolve output path
        output_path = Path(args.output).resolve()
        
        # Create the bundle
        create_bundle(project_root, output_path, files)
        
        return 0
        
    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
        return 1
    except KeyboardInterrupt:
        print("\n⚠️  Interrupted by user")
        return 130
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
