# bookcraft

[![PyPI version](https://img.shields.io/pypi/v/bookcraft)](https://pypi.org/project/bookcraft/)
[![Python versions](https://img.shields.io/pypi/pyversions/bookcraft)](https://pypi.org/project/bookcraft/)
[![Downloads](https://img.shields.io/pypi/dm/bookcraft)](https://pypi.org/project/bookcraft/)
[![codecov](https://codecov.io/gh/albertkol/bookcraft/graph/badge.svg)](https://codecov.io/gh/albertkol/bookcraft)
[![type checked: ty](https://img.shields.io/badge/type%20checked-ty-blue)](https://github.com/astral-sh/ty)

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

## Page format

Pages are plain `.txt` files named `page-1.txt`, `page-2.txt`, etc. inside each book directory.

### Headings

A line starting with `#` is rendered as a heading.

```
#Opening the Lodge in the First Degree
```

### Roles

A line starting with `$` highlights the speaker's role name.

```
$W. M. Brethren, assist me to open the Lodge.
```

### Line breaks

`=` at the end of a line inserts a line break. Multiple `=` insert multiple breaks.

```
$W. M. What is the first care of every Freemason?=
$J. W. To see that the Lodge is properly tyled.=
```

### Italic text

Text wrapped in `>` and `<` is rendered in italic.

```
$I. G. (to J. W., by name) >I. G. gives k....s and is answered by Tyler.<
```

### Keywords

Words and abbreviations listed in `keywords.yaml` are automatically rendered in bold wherever they appear in the text.

```
$W. M. The candidate is an E. A.
```

## Development setup

After cloning, install the pre-commit hooks (one-time):

```bash
uv run pre-commit install
```

This runs type checking and tests automatically before every commit.

## Releasing a new version

1. Bump the version in `pyproject.toml`
2. Add an entry to `CHANGELOG.md`
3. Commit and tag:

```bash
git add pyproject.toml CHANGELOG.md
git commit -m "Release v0.2.0"
git tag v0.2.0
git push && git push --tags
```

GitHub Actions will build and publish to PyPI automatically.

## Content layout

Your content project should provide:

```
your-project/
├── books/          # directories of page-N.txt files
├── fonts/          # font files referenced in fonts.yaml
├── config/
│   ├── fonts.yaml
│   ├── c-settings.yaml
│   ├── c-keywords.yaml
│   ├── ra-settings.yaml
│   └── ra-keywords.yaml
└── output/         # generated PDFs written here
```
