import argparse

from bookcraft._generate import generate, _SWITCH_MAP


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a PDF book with bookcraft.")
    parser.add_argument("mode", choices=list(_SWITCH_MAP), help="Rendering mode")
    parser.add_argument("--books", required=True, help="Path to books directory")
    parser.add_argument("--settings", required=True, help="Path to settings YAML")
    parser.add_argument("--fonts", required=True, help="Path to fonts YAML")
    parser.add_argument("--keywords", required=True, help="Path to keywords YAML")
    parser.add_argument("--output", required=True, help="Output PDF path")
    args = parser.parse_args()

    generate(
        books_path=args.books,
        settings_path=args.settings,
        fonts_path=args.fonts,
        keywords_path=args.keywords,
        output_path=args.output,
        mode=args.mode,
    )
