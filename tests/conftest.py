import pytest

from bookcraft.config import Config
from bookcraft.models import Context, Cursor
from bookcraft.schema import (
    ChapterEntry,
    ColourConfig,
    CursorConfig,
    FontEntry,
    HeadingSpacingConfig,
    PageConfig,
    RoleColours,
    Settings,
    TextConfig,
    TextStyleConfig,
    TitleConfig,
)

_cursor = CursorConfig(
    family="Arial", style="", size=12, colour=[0, 0, 0], fill=[255, 255, 255]
)
_cursor_null = CursorConfig(family="Arial", style="", size=12, colour=None, fill=None)
_text_style = TextStyleConfig(height=20, cursor=_cursor)


@pytest.fixture
def config():
    return Config(
        books_path="./books/",
        fonts=[FontEntry(family="Arial", style="", fname="arial.ttf")],
        settings=Settings(
            title=TitleConfig(text="Test"),
            books=[ChapterEntry(path="TestBook", title="Test Book")],
            colour=ColourConfig(
                enabled=False, italic=False, roles=False, highlight_roles=False
            ),
            text=TextConfig(
                default=_text_style,
                bold=TextStyleConfig(height=20, cursor=_cursor_null),
                italic=_text_style,
                underline=_text_style,
                heading=_text_style,
                heading_spacing=HeadingSpacingConfig(height=3),
                template=_text_style,
            ),
            roles={
                "W. M.": RoleColours(dark=[255, 255, 255], light=[200, 200, 200]),
                "S. W.": RoleColours(dark=[100, 150, 200], light=[150, 190, 240]),
            },
            page=PageConfig(top_margin=18, margin_size=40, bottom_margin=15),
        ),
        keywords=["W. M.", "S. W."],
        switch="c-",
    )


@pytest.fixture
def make_context(config):
    def _make(page, i=0, j=0, cursor=None):
        return Context(
            i=i,
            j=j,
            memory=[page],
            config=config,
            cursor=cursor or Cursor(),
        )

    return _make
