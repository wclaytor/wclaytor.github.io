# Personas Scripts

Scripts for creating and managing persona reference files from Wikipedia.

## create-persona.py

Fetches a Wikipedia page (via API or saved HTML file) and generates a structured Markdown persona file that can be used for reference in prompts.

### Usage

```bash
python scripts/personas/create-persona.py <wikipedia_url_or_html_file> [options]
```

### Options

| Option | Description |
|--------|-------------|
| `-o, --output` | Output directory for the generated Markdown file (default: current directory) |
| `-n, --name` | Custom filename (without .md extension). If not provided, derived from article title |
| `-v, --verbose` | Enable verbose output |

### Examples

```bash
# From Wikipedia URL - creates file in current directory
python scripts/personas/create-persona.py "https://en.wikipedia.org/wiki/Alan_Turing"

# From saved HTML file
python scripts/personas/create-persona.py "./lando-norris.html" --output ./personas

# Specify output directory
python scripts/personas/create-persona.py "https://en.wikipedia.org/wiki/Ada_Lovelace" --output ./personas

# Custom filename
python scripts/personas/create-persona.py "https://en.wikipedia.org/wiki/Bastard_Operator_From_Hell" -n bofh

# Verbose output
python scripts/personas/create-persona.py "https://en.wikipedia.org/wiki/Grace_Hopper" -v

# From HTML file with custom name
python scripts/personas/create-persona.py "./page.html" -n custom-name -v
```

### Output

The script generates a Markdown file with the following structure:

- **Title and Source**: Article title with Wikipedia link
- **Overview**: Introduction/summary from Wikipedia
- **Sections**: All major sections from the article
- **Categories**: Wikipedia categories (limited to 10)
- **External Links**: Links from the article
- **Usage in Prompts**: Template for using the persona in prompts

### Requirements

- Python 3.6+
- No external dependencies (uses standard library only)

### Example Output

For `https://en.wikipedia.org/wiki/Bastard_Operator_From_Hell`:

```
Created persona file: ./bastard-operator-from-hell.md
  Title: Bastard Operator From Hell
  Source: https://en.wikipedia.org/wiki/Bastard_Operator_From_Hell
```

### Handling 403 Errors

If you encounter a `403: Forbidden` error when trying to fetch from Wikipedia:

1. **Save the page manually**: Open the Wikipedia page in your browser and save it as HTML (File → Save Page As)
2. **Run the script with the saved file**:
   ```bash
   python scripts/personas/create-persona.py ./saved-page.html -o ./personas
   ```

The script will parse the HTML and extract the content automatically.
