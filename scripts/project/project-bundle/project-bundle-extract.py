#!/usr/bin/env python3
"""
Alpine Resume - Project Bundle Extractor

This script extracts an Alpine Resume deployment bundle into the appropriate
directory structure for GitHub Pages deployment.

Usage:
    python project-bundle-extract.py [--input BUNDLE_FILE] [--target TARGET_DIR]

Options:
    --input, -i     Input bundle filename (default: alpine-resume-bundle.tar.gz)
    --target, -t    Target directory (default: projects/alpine-resume)
    --force, -f     Overwrite existing files without prompting
    --dry-run       Show what would be extracted without actually extracting
    --help, -h      Show this help message
"""

import os
import sys
import tarfile
import argparse
import shutil
from pathlib import Path


def validate_bundle(bundle_path):
    """
    Validate that the bundle file exists and is a valid tar.gz file.
    
    Args:
        bundle_path: Path to the bundle file
        
    Returns:
        bool: True if valid, raises exception otherwise
    """
    if not bundle_path.exists():
        raise FileNotFoundError(f"Bundle file not found: {bundle_path}")
    
    if not tarfile.is_tarfile(bundle_path):
        raise ValueError(f"File is not a valid tar archive: {bundle_path}")
    
    return True


def list_bundle_contents(bundle_path):
    """
    List the contents of the bundle file.
    
    Args:
        bundle_path: Path to the bundle file
        
    Returns:
        list: List of file names in the bundle
    """
    with tarfile.open(bundle_path, 'r:gz') as tar:
        return tar.getnames()


def extract_bundle(bundle_path, target_dir, force=False, dry_run=False):
    """
    Extract the bundle to the target directory.
    
    Args:
        bundle_path: Path to the bundle file
        target_dir: Target directory for extraction
        force: Overwrite existing files without prompting
        dry_run: Show what would be extracted without extracting
    """
    # Create target directory if it doesn't exist
    if not dry_run:
        target_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"📦 Extracting bundle: {bundle_path.name}")
    print(f"📂 Target directory: {target_dir}")
    
    if dry_run:
        print("🔍 DRY RUN MODE - No files will be modified")
    
    print()
    
    # Check if target directory has existing files
    existing_files = []
    if target_dir.exists():
        existing_files = [f for f in target_dir.rglob('*') if f.is_file()]
    
    if existing_files and not force and not dry_run:
        print(f"⚠️  Warning: Target directory contains {len(existing_files)} existing file(s)")
        response = input("Continue and overwrite? [y/N]: ").strip().lower()
        if response not in ('y', 'yes'):
            print("❌ Extraction cancelled")
            return False
        print()
    
    # Extract files
    with tarfile.open(bundle_path, 'r:gz') as tar:
        members = tar.getmembers()
        
        print(f"📄 Extracting {len(members)} file(s):")
        print()
        
        for member in members:
            if member.isfile():
                target_path = target_dir / member.name
                
                # Check if file exists
                status = "📝 NEW" if not target_path.exists() else "🔄 UPDATE"
                
                print(f"  {status} {member.name}")
                
                if not dry_run:
                    # Extract the file
                    tar.extract(member, path=target_dir)
    
    if not dry_run:
        # Set permissions for extracted files
        for file_path in target_dir.rglob('*'):
            if file_path.is_file():
                # Make HTML, CSS, JS, and JSON files readable
                if file_path.suffix in ['.html', '.css', '.js', '.json']:
                    file_path.chmod(0o644)
    
    print()
    if dry_run:
        print("✅ Dry run complete - no files were modified")
    else:
        print("✅ Extraction complete!")
        print()
        print("Next steps:")
        print("1. Test the application locally")
        print("2. Commit and push changes to GitHub")
        print("3. Your site will be live at https://wclaytor.github.io/projects/alpine-resume/")
    
    return True


def get_bundle_info(bundle_path):
    """
    Display information about the bundle.
    
    Args:
        bundle_path: Path to the bundle file
    """
    size_bytes = os.path.getsize(bundle_path)
    size_kb = size_bytes / 1024
    size_mb = size_kb / 1024
    
    if size_mb >= 1:
        size_str = f"{size_mb:.2f} MB"
    else:
        size_str = f"{size_kb:.2f} KB"
    
    print(f"📊 Bundle Information:")
    print(f"  File: {bundle_path.name}")
    print(f"  Size: {size_str}")
    print()


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description='Extract Alpine Resume deployment bundle',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Extract bundle to default location
  python project-bundle-extract.py
  
  # Extract specific bundle to custom directory
  python project-bundle-extract.py --input my-bundle.tar.gz --target custom/path
  
  # Preview extraction without making changes
  python project-bundle-extract.py --dry-run
  
  # Force overwrite without prompting
  python project-bundle-extract.py --force
        """
    )
    
    parser.add_argument(
        '--input', '-i',
        default='alpine-resume-bundle.tar.gz',
        help='Input bundle filename (default: alpine-resume-bundle.tar.gz)'
    )
    
    parser.add_argument(
        '--target', '-t',
        default='projects/alpine-resume',
        help='Target directory (default: projects/alpine-resume)'
    )
    
    parser.add_argument(
        '--force', '-f',
        action='store_true',
        help='Overwrite existing files without prompting'
    )
    
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be extracted without actually extracting'
    )
    
    parser.add_argument(
        '--list', '-l',
        action='store_true',
        help='List bundle contents without extracting'
    )
    
    args = parser.parse_args()
    
    try:
        # Resolve paths
        bundle_path = Path(args.input).resolve()
        target_dir = Path(args.target).resolve()
        
        # Validate bundle
        validate_bundle(bundle_path)
        
        # Show bundle info
        get_bundle_info(bundle_path)
        
        # List contents if requested
        if args.list:
            print("📋 Bundle Contents:")
            contents = list_bundle_contents(bundle_path)
            for item in sorted(contents):
                print(f"  • {item}")
            print()
            print(f"Total: {len(contents)} file(s)")
            return 0
        
        # Extract bundle
        success = extract_bundle(
            bundle_path,
            target_dir,
            force=args.force,
            dry_run=args.dry_run
        )
        
        return 0 if success else 1
        
    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
        return 1
    except ValueError as e:
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
