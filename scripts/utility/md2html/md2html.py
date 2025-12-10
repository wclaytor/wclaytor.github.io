#!/usr/bin/env python3
"""
Markdown to HTML Converter

Converts Markdown files to beautiful, themed HTML pages with light/dark mode toggle.
Inspired by the Alpine Resume styling.

Usage:
    python md2html.py input.md [output.html]
    
    If output.html is not specified, it will use the input filename with .html extension.

Example:
    python md2html.py README.md
    # Creates README.html in the same directory
    
    python md2html.py docs/guide.md output/guide.html
    # Creates guide.html in output directory
"""

import sys
import os
import re
from pathlib import Path
import markdown
from markdown.extensions import fenced_code, tables, toc, nl2br, sane_lists

def read_markdown_file(file_path):
    """Read markdown content from file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        sys.exit(1)

def extract_title(markdown_content):
    """Extract title from first H1 heading in markdown."""
    match = re.search(r'^#\s+(.+)$', markdown_content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return "Documentation"

def convert_markdown_to_html(markdown_content):
    """Convert markdown content to HTML with extensions."""
    md = markdown.Markdown(
        extensions=[
            'fenced_code',
            'tables',
            'toc',
            'nl2br',
            'sane_lists',
            'codehilite',
        ],
        extension_configs={
            'codehilite': {
                'css_class': 'highlight',
                'linenums': False
            }
        }
    )
    return md.convert(markdown_content)

def generate_html_template(title, content):
    """Generate complete HTML page with theme toggle."""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="{title}">
  <title>{title}</title>
  
  <!-- Bootstrap Icons CDN -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.0/font/bootstrap-icons.css">
  
  <!-- Theme Initialization - Prevent FOUC -->
  <script>
    (function() {{
      const savedTheme = localStorage.getItem('theme');
      const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
      const theme = savedTheme || (prefersDark ? 'dark' : 'light');
      document.documentElement.setAttribute('data-theme', theme);
    }})();
  </script>
  
  <style>
    /* CSS Variables for Theme */
    :root {{
      /* Light theme colors */
      --bg-primary: #ffffff;
      --bg-secondary: #f8f9fa;
      --bg-code: #f5f5f5;
      --text-primary: #1a202c;
      --text-secondary: #4a5568;
      --text-muted: #718096;
      --border-color: #e2e8f0;
      --link-color: #3b82f6;
      --link-hover: #2563eb;
      --shadow: rgba(0, 0, 0, 0.1);
      --code-text: #d63384;
      --blockquote-border: #3b82f6;
      --blockquote-bg: #eff6ff;
      --table-header-bg: #f1f5f9;
      --highlight-bg: #fef3c7;
    }}
    
    [data-theme="dark"] {{
      /* Dark theme colors */
      --bg-primary: #1a202c;
      --bg-secondary: #2d3748;
      --bg-code: #2d3748;
      --text-primary: #f7fafc;
      --text-secondary: #e2e8f0;
      --text-muted: #a0aec0;
      --border-color: #4a5568;
      --link-color: #60a5fa;
      --link-hover: #93c5fd;
      --shadow: rgba(0, 0, 0, 0.3);
      --code-text: #f687b3;
      --blockquote-border: #60a5fa;
      --blockquote-bg: #1e3a5f;
      --table-header-bg: #374151;
      --highlight-bg: #7c2d12;
    }}
    
    /* Prevent FOUC */
    [x-cloak] {{ display: none !important; }}
    
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    
    body {{
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
      line-height: 1.6;
      color: var(--text-primary);
      background-color: var(--bg-primary);
      transition: background-color 0.3s ease, color 0.3s ease;
      overflow-x: hidden;
    }}
    
    /* Header Styling */
    header {{
      background-color: var(--bg-primary);
      border-bottom: 1px solid var(--border-color);
      padding: 1rem 0;
      position: sticky;
      top: 0;
      z-index: 1000;
      box-shadow: 0 2px 4px var(--shadow);
    }}
    
    .header-content {{
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 2rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    
    .header-title {{
      font-size: 1.25rem;
      font-weight: 600;
      color: var(--text-primary);
    }}
    
    /* Theme Toggle Button */
    .theme-toggle {{
      background: none;
      border: none;
      cursor: pointer;
      padding: 0.5rem;
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--text-primary);
      border-radius: 0.375rem;
      transition: background-color 0.2s ease, transform 0.1s ease;
      font-size: 1.25rem;
    }}
    
    .theme-toggle:hover {{
      background-color: var(--bg-secondary);
    }}
    
    .theme-toggle:active {{
      transform: scale(0.95);
    }}
    
    .theme-toggle i {{
      transition: transform 0.3s ease;
    }}
    
    /* Main Content Container */
    .container {{
      max-width: 1200px;
      margin: 0 auto;
      padding: 2rem;
    }}
    
    @media (max-width: 768px) {{
      .container {{
        padding: 1rem;
      }}
    }}
    
    /* Content Styling */
    .content {{
      background-color: var(--bg-primary);
      border-radius: 0.5rem;
      padding: 2rem;
      box-shadow: 0 1px 3px var(--shadow);
    }}
    
    @media (max-width: 768px) {{
      .content {{
        padding: 1.5rem;
      }}
    }}
    
    /* Typography */
    h1, h2, h3, h4, h5, h6 {{
      color: var(--text-primary);
      margin-top: 2rem;
      margin-bottom: 1rem;
      font-weight: 600;
      line-height: 1.3;
    }}
    
    h1 {{ font-size: 2.5rem; margin-top: 0; }}
    h2 {{ font-size: 2rem; border-bottom: 2px solid var(--border-color); padding-bottom: 0.5rem; }}
    h3 {{ font-size: 1.5rem; }}
    h4 {{ font-size: 1.25rem; }}
    h5 {{ font-size: 1.125rem; }}
    h6 {{ font-size: 1rem; }}
    
    @media (max-width: 768px) {{
      h1 {{ font-size: 2rem; }}
      h2 {{ font-size: 1.75rem; }}
      h3 {{ font-size: 1.375rem; }}
    }}
    
    p {{
      margin-bottom: 1rem;
      color: var(--text-secondary);
    }}
    
    /* Links */
    a {{
      color: var(--link-color);
      text-decoration: none;
      transition: color 0.2s ease;
    }}
    
    a:hover {{
      color: var(--link-hover);
      text-decoration: underline;
    }}
    
    /* Lists */
    ul, ol {{
      margin-bottom: 1rem;
      padding-left: 2rem;
      color: var(--text-secondary);
    }}
    
    li {{
      margin-bottom: 0.5rem;
    }}
    
    ul ul, ol ol, ul ol, ol ul {{
      margin-top: 0.5rem;
      margin-bottom: 0.5rem;
    }}
    
    /* Code */
    code {{
      background-color: var(--bg-code);
      color: var(--code-text);
      padding: 0.2rem 0.4rem;
      border-radius: 0.25rem;
      font-family: 'Monaco', 'Courier New', monospace;
      font-size: 0.875rem;
    }}
    
    pre {{
      background-color: var(--bg-code);
      border: 1px solid var(--border-color);
      border-radius: 0.5rem;
      padding: 1rem;
      overflow-x: auto;
      margin-bottom: 1rem;
    }}
    
    pre code {{
      background: none;
      padding: 0;
      color: var(--text-primary);
      font-size: 0.875rem;
      line-height: 1.5;
    }}
    
    /* Blockquotes */
    blockquote {{
      border-left: 4px solid var(--blockquote-border);
      background-color: var(--blockquote-bg);
      padding: 1rem 1.5rem;
      margin: 1rem 0;
      border-radius: 0.25rem;
    }}
    
    blockquote p {{
      margin-bottom: 0;
      color: var(--text-primary);
    }}
    
    /* Tables */
    table {{
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 1rem;
      overflow-x: auto;
      display: block;
    }}
    
    @media (min-width: 768px) {{
      table {{
        display: table;
      }}
    }}
    
    thead {{
      background-color: var(--table-header-bg);
    }}
    
    th, td {{
      padding: 0.75rem;
      text-align: left;
      border-bottom: 1px solid var(--border-color);
    }}
    
    th {{
      font-weight: 600;
      color: var(--text-primary);
    }}
    
    td {{
      color: var(--text-secondary);
    }}
    
    tr:hover {{
      background-color: var(--bg-secondary);
    }}
    
    /* Horizontal Rule */
    hr {{
      border: none;
      border-top: 2px solid var(--border-color);
      margin: 2rem 0;
    }}
    
    /* Images */
    img {{
      max-width: 100%;
      height: auto;
      border-radius: 0.5rem;
      margin: 1rem 0;
    }}
    
    /* Strong and Emphasis */
    strong {{
      font-weight: 600;
      color: var(--text-primary);
    }}
    
    em {{
      font-style: italic;
    }}
    
    /* Smooth scrolling */
    html {{
      scroll-behavior: smooth;
    }}
    
    /* Respect reduced motion preference */
    @media (prefers-reduced-motion: reduce) {{
      * {{
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
        scroll-behavior: auto !important;
      }}
    }}
    
    /* Print styles */
    @media print {{
      body {{
        background: white;
        color: black;
      }}
      
      header {{
        position: static;
        box-shadow: none;
      }}
      
      .theme-toggle {{
        display: none;
      }}
      
      a {{
        color: #0066cc;
        text-decoration: underline;
      }}
      
      pre, blockquote {{
        page-break-inside: avoid;
      }}
    }}
  </style>
</head>
<body>
  <!-- Header with Theme Toggle -->
  <header>
    <div class="header-content">
      <h1 class="header-title">{title}</h1>
      <button 
        class="theme-toggle" 
        onclick="toggleTheme()"
        aria-label="Toggle theme"
        title="Toggle light/dark theme">
        <i class="bi bi-sun-fill" id="theme-icon-light" style="display: none;"></i>
        <i class="bi bi-moon-stars-fill" id="theme-icon-dark" style="display: none;"></i>
      </button>
    </div>
  </header>
  
  <!-- Main Content -->
  <div class="container">
    <div class="content">
      {content}
    </div>
  </div>
  
  <!-- Theme Toggle Script -->
  <script>
    // Initialize theme icons on page load
    function updateThemeIcon() {{
      const theme = document.documentElement.getAttribute('data-theme');
      const lightIcon = document.getElementById('theme-icon-light');
      const darkIcon = document.getElementById('theme-icon-dark');
      
      if (theme === 'dark') {{
        lightIcon.style.display = 'block';
        darkIcon.style.display = 'none';
      }} else {{
        lightIcon.style.display = 'none';
        darkIcon.style.display = 'block';
      }}
    }}
    
    // Toggle theme function
    function toggleTheme() {{
      const currentTheme = document.documentElement.getAttribute('data-theme');
      const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
      
      document.documentElement.setAttribute('data-theme', newTheme);
      localStorage.setItem('theme', newTheme);
      updateThemeIcon();
    }}
    
    // Update icon on load
    updateThemeIcon();
    
    // Listen for system theme changes
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {{
      if (!localStorage.getItem('theme')) {{
        const newTheme = e.matches ? 'dark' : 'light';
        document.documentElement.setAttribute('data-theme', newTheme);
        updateThemeIcon();
      }}
    }});
  </script>
</body>
</html>"""

def main():
    if len(sys.argv) < 2:
        print("Usage: python md2html.py input.md [output.html]")
        print("\nExample:")
        print("  python md2html.py README.md")
        print("  python md2html.py docs/guide.md output/guide.html")
        sys.exit(1)
    
    input_path = Path(sys.argv[1])
    
    if not input_path.exists():
        print(f"Error: Input file '{input_path}' not found")
        sys.exit(1)
    
    if not input_path.suffix.lower() in ['.md', '.markdown']:
        print(f"Error: Input file must be a Markdown file (.md or .markdown)")
        sys.exit(1)
    
    # Determine output path
    if len(sys.argv) >= 3:
        output_path = Path(sys.argv[2])
    else:
        output_path = input_path.with_suffix('.html')
    
    # Create output directory if it doesn't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    print(f"Converting: {input_path}")
    print(f"Output to: {output_path}")
    
    # Read markdown content
    markdown_content = read_markdown_file(input_path)
    
    # Extract title
    title = extract_title(markdown_content)
    
    # Convert markdown to HTML
    html_content = convert_markdown_to_html(markdown_content)
    
    # Generate complete HTML page
    full_html = generate_html_template(title, html_content)
    
    # Write output file
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(full_html)
        print(f"✅ Successfully created: {output_path}")
        print(f"📄 Title: {title}")
        print(f"🎨 Features: Light/Dark theme toggle, responsive design, print-ready")
    except Exception as e:
        print(f"Error writing output file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
