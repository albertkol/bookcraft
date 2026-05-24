from dataclasses import dataclass

import yaml


@dataclass
class Config:
    BOOKS_PATH: str
    FONTS: dict
    SETTINGS: dict
    KEYWORDS: list
    switch: str  # "c-", "c-dark-", "ra-", "ra-dark-"

    @property
    def is_dark(self) -> bool:
        return "dark" in self.switch

    @property
    def is_ra(self) -> bool:
        return "ra" in self.switch

    @property
    def PAGE(self) -> dict:
        return self.SETTINGS.get("page")

    @property
    def COLOUR(self) -> dict:
        return self.SETTINGS.get("colour")

    @property
    def ROLES(self) -> dict:
        return self.SETTINGS.get("roles")

    @property
    def TEXT(self) -> dict:
        return self.SETTINGS.get("text")

    @property
    def DEFAULT_CURSOR(self) -> dict:
        return {
            "family": self.TEXT["default"]["cursor"]["family"],
            "style": self.TEXT["default"]["cursor"]["style"],
            "size": self.TEXT["default"]["cursor"]["size"],
            "colour": self.TEXT["default"]["cursor"]["colour"],
            "fill": self.TEXT["default"]["cursor"]["fill"],
        }

    @property
    def DEFAULT_FONT(self) -> dict:
        return {
            "family": self.TEXT["default"]["cursor"]["family"],
            "style": self.TEXT["default"]["cursor"]["style"],
            "size": self.TEXT["default"]["cursor"]["size"],
        }

    @property
    def DEFAULT_HEIGHT(self) -> dict:
        return self.TEXT["default"]["height"]

    @property
    def DEFAULT_FILL(self) -> dict:
        return self.TEXT["default"]["cursor"]["fill"]

    @property
    def TEMPLATE_FONT(self) -> dict:
        return {
            "family": self.TEXT["template"]["cursor"]["family"],
            "style": self.TEXT["template"]["cursor"]["style"],
            "size": self.TEXT["template"]["cursor"]["size"],
        }

    @property
    def TEMPLATE_COLOR(self) -> dict:
        return self.TEXT["template"]["cursor"]["colour"]

    @property
    def TEMPLATE_HEIGHT(self) -> int:
        return self.TEXT["template"]["height"]

    @property
    def BOLD_CURSOR(self) -> dict:
        return {
            "family": self.TEXT["bold"]["cursor"]["family"],
            "style": self.TEXT["bold"]["cursor"]["style"],
            "size": self.TEXT["bold"]["cursor"]["size"],
            "colour": self.TEXT["bold"]["cursor"]["colour"],
            "fill": self.TEXT["bold"]["cursor"]["fill"],
        }

    @property
    def ITALIC_CURSOR(self) -> dict:
        return {
            "family": self.TEXT["italic"]["cursor"]["family"],
            "style": self.TEXT["italic"]["cursor"]["style"],
            "size": self.TEXT["italic"]["cursor"]["size"],
            "colour": self.TEXT["italic"]["cursor"]["colour"],
            "fill": self.TEXT["italic"]["cursor"]["fill"],
        }

    @property
    def HEADING_CURSOR(self) -> dict:
        return {
            "family": self.TEXT["heading"]["cursor"]["family"],
            "style": self.TEXT["heading"]["cursor"]["style"],
            "size": self.TEXT["heading"]["cursor"]["size"],
            "colour": self.TEXT["heading"]["cursor"]["colour"],
            "fill": self.TEXT["heading"]["cursor"]["fill"],
        }

    @property
    def HEADING_SPACING_HEIGHT(self) -> int:
        return self.TEXT["heading_spacing"]["height"]


def load_config(
    books_path: str,
    settings_path: str,
    fonts_path: str,
    keywords_path: str,
    switch: str,
) -> Config:
    with open(fonts_path, "r") as f:
        fonts = yaml.safe_load(f).get("fonts")
    with open(settings_path, "r") as f:
        settings = yaml.safe_load(f)
    with open(keywords_path, "r") as f:
        keywords = yaml.safe_load(f).get("keywords")
    return Config(
        BOOKS_PATH=books_path,
        FONTS=fonts,
        SETTINGS=settings,
        KEYWORDS=keywords,
        switch=switch,
    )
