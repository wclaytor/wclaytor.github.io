#!/usr/bin/env python3
"""
Create Persona Script

Fetches a Wikipedia page and generates a structured Markdown persona file
that can be used for reference in prompts.

Usage:
    python create-persona.py <wikipedia_url> [output_directory]

Examples:
    python create-persona.py "https://en.wikipedia.org/wiki/Bastard_Operator_From_Hell"
    python create-persona.py "https://en.wikipedia.org/wiki/Alan_Turing" ./personas
    python create-persona.py "https://en.wikipedia.org/wiki/Ada_Lovelace" --output ./personas
"""

import argparse
import json
import re
import sys
import urllib.request
import urllib.parse
from datetime import datetime
from pathlib import Path


def extract_title_from_url(url):
    """Extract the Wikipedia article title from a URL."""
    match = re.search(r'/wiki/([^#?]+)', url)
    if match:
        return urllib.parse.unquote(match.group(1).replace('_', ' '))
    raise ValueError("Could not extract article title from URL: " + url)


def get_wikipedia_title_for_api(url):
    """Get the title formatted for the Wikipedia API."""
    match = re.search(r'/wiki/([^#?]+)', url)
    if match:
        return match.group(1)
    raise ValueError("Could not extract article title from URL: " + url)


def fetch_wikipedia_content(title):
    """Fetch Wikipedia article content using the MediaWiki API."""
    api_url = "https://en.wikipedia.org/w/api.php"
    params = {
        'action': 'query',
        'titles': title,
        'prop': 'extracts|info|categories',
        'explaintext': 'true',
        'format': 'json',
        'inprop': 'url',
        'cllimit': '50'
    }
    
    query_string = urllib.parse.urlencode(params)
    full_url = api_url + "?" + query_string
    
    try:
        with urllib.request.urlopen(full_url, timeout=30) as response:
            data = json.loads(response.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            
            if not pages:
                raise ValueError("No pages found in Wikipedia response")
            
            page = list(pages.values())[0]
            
            if 'missing' in page:
                raise ValueError("Wikipedia article not found: " + title)
            
            return page
    except urllib.error.URLError as e:
        raise ConnectionError("Failed to fetch Wikipedia page: " + str(e))


def slugify(text):
    """Convert text to a URL/filename-friendly slug."""
    slug = text.lower()
    slug = re.sub(r'[\s_]+', '-', slug)
    slug = re.sub(r'[^a-z0-9-]', '', slug)
    slug = re.sub(r'-+', '-', slug)
    slug = slug.strip('-')
    return slug


def parse_sections(content):
    """Parse Wikipedia content into sections."""
    sections = {}
    current_section = 'introduction'
    current_content = []
    
    lines = content.split('\n')
    
    for line in lines:
        header_match = re.match(r'^(=+)\s*(.+?)\s*=+$', line)
        if header_match:
            if current_content:
                sections[current_section] = '\n'.join(current_content).strip()
            current_section = header_match.group(2).strip()
            current_content = []
        else:
            current_content.append(line)
    
    if current_content:
        sections[current_section] = '\n'.join(current_content).strip()
    
    return sections


def generate_markdown(title, url, content, categories):
    """Generate a structured Markdown file from Wikipedia content."""
    sections = parse_sections(content)
    
    md_lines = []
    
    md_lines.append("# " + title)
    md_lines.append("")
    md_lines.append("> Source: [Wikipedia](" + url + ")")
    md_lines.append("")
    
    if 'introduction' in sections and sections['introduction']:
        md_lines.append("## Overview")
        md_lines.append("")
        intro = sections['introduction']
        intro = re.sub(
            r'\b(' + re.escape(title) + r')\b',
            r'**\1**',
            intro,
            count=1,
            flags=re.IGNORECASE
        )
        md_lines.append(intro)
        md_lines.append("")
    
    skip_sections = {
        'introduction', 'References', 'See also', 'Further reading',
        'External links', 'Notes', 'Sources', 'Bibliography'
    }
    
    for section_name, section_content in sections.items():
        if section_name in skip_sections or not section_content:
            continue
        
        md_lines.append("## " + section_name)
        md_lines.append("")
        md_lines.append(section_content)
        md_lines.append("")
    
    if categories:
        md_lines.append("## Categories")
        md_lines.append("")
        for cat in categories[:10]:
            cat_name = cat.get('title', '').replace('Category:', '')
            if cat_name and not cat_name.startswith('Articles') and not cat_name.startswith('All '):
                md_lines.append("- " + cat_name)
        md_lines.append("")
    
    if 'External links' in sections:
        md_lines.append("## External Links")
        md_lines.append("")
        md_lines.append(sections['External links'])
        md_lines.append("")
    
    md_lines.append("---")
    md_lines.append("")
    md_lines.append("## Usage in Prompts")
    md_lines.append("")
    md_lines.append("When referencing " + title + " in prompts, you can use this file as context.")
    md_lines.append("")
    md_lines.append("### Example Prompt Usage")
    md_lines.append("")
    md_lines.append("```")
    md_lines.append("Using the context from " + slugify(title) + ".md, please [your request here].")
    md_lines.append("```")
    md_lines.append("")
    
    md_lines.append("---")
    md_lines.append("")
    md_lines.append("*Last updated: " + datetime.now().strftime('%B %Y') + "*")
    md_lines.append("*Source: Wikipedia - " + title + "*")
    md_lines.append("")
    
    return '\n'.join(md_lines)


def main():
    parser = argparse.ArgumentParser(
        description='Create a persona Markdown file from a Wikipedia page.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s "https://en.wikipedia.org/wiki/Alan_Turing"
  %(prog)s "https://en.wikipedia.org/wiki/Ada_Lovelace" --output ./personas
  %(prog)s "https://en.wikipedia.org/wiki/Bastard_Operator_From_Hell" -o ./
        """
    )
    
    parser.add_argument(
        'url',
        help='Wikipedia URL of the person/character to create a persona for'
    )
    
    parser.add_argument(
        '-o', '--output',
        default='.',
        help='Output directory for the generated Markdown file (default: current directory)'
    )
    
    parser.add_argument(
        '-n', '--name',
        help='Custom filename (without .md extension). If not provided, derived from article title.'
    )
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose output'
    )
    
    args = parser.parse_args()
    
    if 'wikipedia.org' not in args.url:
        print("Error: Please provide a valid Wikipedia URL", file=sys.stderr)
        sys.exit(1)
    
    try:
        title = extract_title_from_url(args.url)
        api_title = get_wikipedia_title_for_api(args.url)
        
        if args.verbose:
            print("Fetching Wikipedia article: " + title)
        
        page_data = fetch_wikipedia_content(api_title)
        
        content = page_data.get('extract', '')
        if not content:
            print("Error: No content found in Wikipedia article", file=sys.stderr)
            sys.exit(1)
        
        actual_title = page_data.get('title', title)
        canonical_url = page_data.get('fullurl', args.url)
        categories = page_data.get('categories', [])
        
        if args.verbose:
            print("Article title: " + actual_title)
            print("Content length: " + str(len(content)) + " characters")
        
        markdown = generate_markdown(actual_title, canonical_url, content, categories)
        
        if args.name:
            filename = args.name + ".md"
        else:
            filename = slugify(actual_title) + ".md"
        
        output_dir = Path(args.output)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        output_path = output_dir / filename
        output_path.write_text(markdown, encoding='utf-8')
        
        print("Created persona file: " + str(output_path))
        print("  Title: " + actual_title)
        print("  Source: " + canonical_url)
        
    except ValueError as e:
        print("Error: " + str(e), file=sys.stderr)
        sys.exit(1)
    except ConnectionError as e:
        print("Connection Error: " + str(e), file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print("Unexpected error: " + str(e), file=sys.stderr)
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
