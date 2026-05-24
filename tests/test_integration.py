import textwrap
from pathlib import Path
from unittest.mock import patch

import pytest

from bookcraft import generate
from bookcraft.book import Book

_SETTINGS = textwrap.dedent("""\
    title:
      text: Test Lodge
    books:
      - path: TestBook
        title: Test Book
    colour:
      enabled: false
      italic: false
      roles: false
      highlight_roles: false
    text:
      default:
        height: 20
        cursor: {family: Helvetica, style: '', size: 12, colour: [0,0,0], fill: [255,255,255]}
      bold:
        height: 20
        cursor: {family: Helvetica, style: 'B', size: 12, colour: null, fill: null}
      italic:
        height: 20
        cursor: {family: Helvetica, style: 'I', size: 12, colour: [0,0,0], fill: [255,255,255]}
      heading:
        height: 24
        cursor: {family: Helvetica, style: 'B', size: 14, colour: [0,0,0], fill: [255,255,255]}
      heading_spacing:
        height: 3
      template:
        height: 20
        cursor: {family: Helvetica, style: '', size: 12, colour: [0,0,0], fill: [255,255,255]}
    roles:
      W. M.:
        dark: [255, 255, 255]
        light: [200, 200, 200]
    page:
      top_margin: 18
      margin_size: 40
      bottom_margin: 15
""")


def _setup_book(tmp_path, content: bytes) -> None:
    book_dir = tmp_path / "TestBook"
    book_dir.mkdir()
    (book_dir / "page-1.txt").write_bytes(content)
    (tmp_path / "settings.yaml").write_text(_SETTINGS)
    (tmp_path / "fonts.yaml").write_text(
        "fonts:\n  - family: Helvetica\n    style: ''\n    fname: helvetica.ttf\n"
    )
    (tmp_path / "keywords.yaml").write_text("keywords:\n  - W. M.\n")


def _generate(tmp_path, mode: str = "craft") -> Path:
    output = tmp_path / "output.pdf"
    with patch.object(Book, "set_book_font", lambda self, fonts: self):
        generate(
            books_path=str(tmp_path) + "/",
            settings_path=str(tmp_path / "settings.yaml"),
            fonts_path=str(tmp_path / "fonts.yaml"),
            keywords_path=str(tmp_path / "keywords.yaml"),
            output_path=str(output),
            mode=mode,
        )
    return output


def test_generate_produces_pdf(tmp_path):
    _setup_book(tmp_path, b"Hello World=\n")
    output = _generate(tmp_path)
    assert output.exists()
    assert output.stat().st_size > 1000


def test_generate_with_role_and_keyword(tmp_path):
    _setup_book(tmp_path, b"$W. M. Brethren, assist me to open the Lodge.=\n")
    output = _generate(tmp_path)
    assert output.exists()
    assert output.stat().st_size > 1000


def test_generate_with_heading(tmp_path):
    _setup_book(tmp_path, b"#Opening the Lodge=\nHello World=\n")
    output = _generate(tmp_path)
    assert output.exists()
    assert output.stat().st_size > 1000


def test_generate_dark_mode(tmp_path):
    _setup_book(tmp_path, b"Hello World=\n")
    output = _generate(tmp_path, mode="craft-dark")
    assert output.exists()
    assert output.stat().st_size > 1000


def test_generate_raises_for_invalid_mode(tmp_path):
    with pytest.raises(ValueError, match="Unknown mode"):
        generate(
            books_path=str(tmp_path),
            settings_path="",
            fonts_path="",
            keywords_path="",
            output_path="",
            mode="invalid",
        )
