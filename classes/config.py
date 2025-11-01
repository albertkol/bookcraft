from dataclasses import dataclass

import yaml

SWITCH = "ra-"

with open("fonts.yaml", "r") as file:
    FONTS = yaml.safe_load(file).get("fonts")

with open(SWITCH + "settings.yaml", "r") as file:
    SETTINGS = yaml.safe_load(file)

with open(SWITCH + "keywords.yaml", "r") as file:
    KEYWORDS = yaml.safe_load(file).get("keywords")


@dataclass
class Config:
    BOOKS_PATH = "./books/"
    FONTS: dict
    SETTINGS: dict
    KEYWORDS: list

    def __init__(self, fonts: dict, settings: dict, keywords: dict):
        self.FONTS = fonts
        self.SETTINGS = settings
        self.KEYWORDS = keywords

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


CONFIG = Config(fonts=FONTS, settings=SETTINGS, keywords=KEYWORDS)
