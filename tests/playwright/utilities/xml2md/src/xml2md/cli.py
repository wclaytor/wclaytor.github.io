"""Command-line interface for xml2md."""

import xml.etree.ElementTree as ET
from pathlib import Path

import click

from .formatter import generate_markdown
from .parser import parse_junit_xml


@click.command()
@click.argument("xml_file", type=click.Path(exists=True, path_type=Path))
@click.option(
    "-o",
    "--output",
    type=click.Path(path_type=Path),
    help="Output path for Markdown file. Can be a file or directory.",
)
def main(xml_file: Path, output: Path | None) -> None:
    """
    Convert a JUnit XML test report to a Markdown report.

    XML_FILE is the path to the JUnit XML report to convert.

    Examples:

        xml2md report.xml                    # Output to report.md

        xml2md report.xml -o custom.md       # Custom output file

        xml2md report.xml -o results/        # Output to directory
    """
    # Parse the XML
    try:
        suites = parse_junit_xml(xml_file)
    except ET.ParseError as e:
        raise click.ClickException(f"Failed to parse XML: {e}")

    # Generate Markdown
    markdown = generate_markdown(suites, xml_file)

    # Determine output path
    if output is None:
        output_path = xml_file.with_suffix(".md")
    elif output.is_dir() or str(output).endswith("/"):
        output.mkdir(parents=True, exist_ok=True)
        output_path = output / xml_file.with_suffix(".md").name
    else:
        output_path = output
        output_path.parent.mkdir(parents=True, exist_ok=True)

    # Write output
    output_path.write_text(markdown)
    click.echo(f"✅ Markdown report saved to: {output_path}")


if __name__ == "__main__":
    main()
