from dataclasses import dataclass
from pathlib import Path

import yaml

from bookcraft.schema import FontEntry, PageConfig, RoleColours, Settings


@dataclass
class Config:
    books_path: str
    fonts: list[FontEntry]
    settings: Settings
    keywords: list[str]
    switch: str  # "c-", "c-dark-", "ra-", "ra-dark-"

    @property
    def is_dark(self) -> bool:
        return "dark" in self.switch

    @property
    def is_ra(self) -> bool:
        return "ra" in self.switch

    @property
    def page(self) -> PageConfig:
        return self.settings.page

    @property
    def roles(self) -> dict[str, RoleColours]:
        return self.settings.roles

    @property
    def default_cursor(self) -> dict:
        return self.settings.text.default.cursor.model_dump()

    @property
    def default_height(self) -> float:
        return self.settings.text.default.height

    @property
    def default_fill(self) -> list[int]:
        return self.settings.text.default.cursor.fill or []

    @property
    def template_font(self) -> dict:
        c = self.settings.text.template.cursor
        return {"family": c.family, "style": c.style, "size": c.size}

    @property
    def template_color(self) -> list[int]:
        return self.settings.text.template.cursor.colour or []

    @property
    def template_height(self) -> float:
        return self.settings.text.template.height

    @property
    def bold_cursor(self) -> dict:
        return self.settings.text.bold.cursor.model_dump()

    @property
    def italic_cursor(self) -> dict:
        return self.settings.text.italic.cursor.model_dump()

    @property
    def underline_cursor(self) -> dict:
        return self.settings.text.underline.cursor.model_dump()

    @property
    def heading_cursor(self) -> dict:
        return self.settings.text.heading.cursor.model_dump()

    @property
    def heading_spacing_height(self) -> float:
        return self.settings.text.heading_spacing.height

    @property
    def page_no_offset(self) -> int:
        return self.settings.page.page_no_offset


def load_config(
    books_path: str,
    settings_path: str,
    fonts_path: str,
    keywords_path: str,
    switch: str,
) -> Config:
    with open(fonts_path, "r") as f:
        raw_fonts = yaml.safe_load(f).get("fonts")
    with open(settings_path, "r") as f:
        raw_settings = yaml.safe_load(f)
    with open(keywords_path, "r") as f:
        raw_keywords = yaml.safe_load(f).get("keywords")

    fonts_dir = Path(fonts_path).parent
    fonts = [
        FontEntry(**{**font, "fname": str((fonts_dir / font["fname"]).resolve())})
        for font in raw_fonts
    ]

    return Config(
        books_path=books_path,
        fonts=fonts,
        settings=Settings(**raw_settings),
        keywords=raw_keywords,
        switch=switch,
    )
