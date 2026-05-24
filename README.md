# bookcraft

A Python library for generating PDF books from structured text content.

## Installation

```bash
pip install bookcraft
```

## Usage

```python
from bookcraft import generate

generate(
    books_path="./books/",
    settings_path="./c-settings.yaml",
    fonts_path="./fonts.yaml",
    keywords_path="./c-keywords.yaml",
    output_path="./output/craft.pdf",
    mode="craft",
)
```

### Modes

| Mode | Description |
|------|-------------|
| `craft` | Craft, light theme |
| `craft-dark` | Craft, dark theme |
| `ra` | Royal Arch, light theme |
| `ra-dark` | Royal Arch, dark theme |

## Content layout

Your content project should provide:

```
your-project/
├── books/          # directories of page-N.txt files
├── fonts/          # font files referenced in fonts.yaml
├── fonts.yaml
├── c-settings.yaml
├── c-keywords.yaml
├── ra-settings.yaml
├── ra-keywords.yaml
└── output/         # generated PDFs written here
```
