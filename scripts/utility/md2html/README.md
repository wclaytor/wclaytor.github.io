# Markdown to HTML Converter

Convert Markdown files to beautiful, themed HTML pages with light/dark mode toggle.

## Features

✨ **Professional Styling**
- Clean, modern design inspired by Alpine Resume
- Light and dark theme with automatic system preference detection
- Smooth theme transitions with localStorage persistence

🎨 **Full Markdown Support**
- All standard Markdown syntax
- Fenced code blocks with syntax highlighting
- Tables with responsive design
- Blockquotes, lists, images, and more

📱 **Responsive Design**
- Mobile-first responsive layout
- Sticky header navigation
- Touch-friendly interface
- Optimized for all screen sizes

♿ **Accessible**
- Semantic HTML5
- ARIA labels
- Keyboard navigation
- Respects user motion preferences

🖨️ **Print Ready**
- Optimized print styles
- Clean, professional PDF output

## Installation

Install required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

Convert a Markdown file to HTML (creates file with same name):

```bash
python md2html.py README.md
```

This creates `README.html` in the same directory.

### Specify Output File

```bash
python md2html.py input.md output.html
```

### Examples

```bash
# Convert project README
python md2html.py README.md

# Convert to specific output location
python md2html.py docs/guide.md output/guide.html

# Convert multiple files
python md2html.py README.md
python md2html.py CONTRIBUTING.md
python md2html.py LICENSE.md
```

## Features in Detail

### Theme Toggle

- **Light Mode**: Clean, bright design for daytime reading
- **Dark Mode**: Easy on the eyes for night-time viewing
- **System Preference**: Automatically detects user's OS theme preference
- **Persistence**: Remembers user's choice using localStorage
- **Smooth Transitions**: Elegant color transitions between themes

### Styling

The generated HTML includes:
- Professional typography with system font stack
- Syntax-highlighted code blocks
- Responsive tables that work on mobile
- Styled blockquotes with visual distinction
- Clean, consistent spacing throughout
- Hover effects on interactive elements

### Responsive Design

- **Desktop**: Maximum 1200px content width with padding
- **Tablet**: Adjusted spacing and font sizes
- **Mobile**: Stacked layout, optimized touch targets
- **Print**: Clean, ink-efficient print styles

## Output Format

The script generates a standalone HTML file with:
- All CSS inlined (no external dependencies except Bootstrap Icons for theme toggle)
- Theme toggle button in header
- Responsive, accessible markup
- Complete page structure ready to deploy

## Requirements

- Python 3.7+
- `markdown` package with extensions

See `requirements.txt` for specific versions.

## Use Cases

Perfect for:
- Converting project READMEs for web viewing
- Creating documentation pages
- Building static content pages
- Converting guides and tutorials
- Generating shareable HTML from Markdown

## Example Output

Given this Markdown:

```markdown
# My Project

## Features

- Feature 1
- Feature 2

## Code Example

\`\`\`python
def hello():
    print("Hello, World!")
\`\`\`
```

The script generates a complete HTML page with:
- Sticky header showing "My Project"
- Theme toggle button
- Properly styled headings, lists, and code blocks
- Responsive layout
- Light/dark theme support

## Customization

The script includes extensive inline CSS that can be customized by editing the `generate_html_template()` function in `md2html.py`.

Key customization points:
- Color scheme (CSS variables in `:root` and `[data-theme="dark"]`)
- Typography (font family, sizes, line heights)
- Spacing and layout
- Code block styling
- Header design

## License

MIT License - Feel free to use and modify for your projects.

---

**Created by**: William Claytor  
**Inspired by**: Alpine Resume project styling  
**Version**: 1.0.0
