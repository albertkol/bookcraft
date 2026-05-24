import textwrap

import pytest
from pydantic import ValidationError

from bookcraft.config import load_config
from bookcraft.schema import Settings


def test_is_dark_false_for_craft(config):
    assert config.is_dark is False


def test_is_dark_true_for_dark_switch(config):
    config.switch = "c-dark-"
    assert config.is_dark is True


def test_is_ra_false_for_craft(config):
    assert config.is_ra is False


def test_is_ra_true_for_ra_switch(config):
    config.switch = "ra-"
    assert config.is_ra is True


def test_page_returns_page_config(config):
    assert config.page.top_margin == 18
    assert config.page.margin_size == 40


def test_default_height(config):
    assert config.default_height == 20


def test_roles_accessible_by_name(config):
    assert config.roles["W. M."].light == [200, 200, 200]
    assert config.roles["S. W."].dark == [100, 150, 200]


def test_default_fill(config):
    assert config.default_fill == [255, 255, 255]


def test_template_font(config):
    font = config.template_font
    assert font["family"] == "Arial"
    assert font["style"] == ""
    assert font["size"] == 12


def test_template_color(config):
    assert config.template_color == [0, 0, 0]


def test_template_height(config):
    assert config.template_height == 20


def test_italic_cursor(config):
    cursor = config.italic_cursor
    assert cursor["family"] == "Arial"


def test_load_config(tmp_path):
    (tmp_path / "fonts.yaml").write_text(
        "fonts:\n  - family: Arial\n    style: ''\n    fname: arial.ttf\n"
    )
    (tmp_path / "keywords.yaml").write_text("keywords:\n  - W. M.\n")
    (tmp_path / "settings.yaml").write_text(
        textwrap.dedent("""\
        title:
          text: Test Book
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
            cursor: {family: Arial, style: '', size: 12, colour: [0,0,0], fill: [255,255,255]}
          bold:
            height: 20
            cursor: {family: Arial, style: 'B', size: 12, colour: null, fill: null}
          italic:
            height: 20
            cursor: {family: Arial, style: 'I', size: 12, colour: [0,0,0], fill: [255,255,255]}
          heading:
            height: 24
            cursor: {family: Arial, style: 'B', size: 14, colour: [0,0,0], fill: [255,255,255]}
          heading_spacing:
            height: 3
          template:
            height: 20
            cursor: {family: Arial, style: '', size: 12, colour: [0,0,0], fill: [255,255,255]}
        roles:
          W. M.:
            dark: [255, 255, 255]
            light: [200, 200, 200]
        page:
          top_margin: 18
          margin_size: 40
          bottom_margin: 15
        """)
    )
    config = load_config(
        books_path=str(tmp_path),
        settings_path=str(tmp_path / "settings.yaml"),
        fonts_path=str(tmp_path / "fonts.yaml"),
        keywords_path=str(tmp_path / "keywords.yaml"),
        switch="c-",
    )
    assert config.settings.title.text == "Test Book"
    assert len(config.fonts) == 1
    assert config.keywords == ["W. M."]


def test_invalid_settings_raises():
    with pytest.raises(ValidationError):
        Settings.model_validate(
            {
                "title": "not-a-dict",
                "books": [],
                "colour": {},
                "text": {},
                "roles": {},
                "page": {},
            }
        )
