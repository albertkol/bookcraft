from dataclasses import dataclass

import yaml

from models import Cell, Cursor

with open("fonts.yaml", "r") as file:
    FONTS = yaml.safe_load(file).get("fonts")

with open("settings.yaml", "r") as file:
    SETTINGS = yaml.safe_load(file)

with open("keywords.yaml", "r") as file:
    KEYWORDS = yaml.safe_load(file).get("keywords")


@dataclass
class Config:
    BOOKS_PATH = "./books/"
    FONTS: dict
    SETTINGS: dict
    KEYWORDS: dict

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
    def DEFAULT_CELL(self) -> dict:
        return Cell(
            width=0,
            height=int(self.TEXT["default"]["height"]),
            cursor=Cursor(**self.TEXT["default"]["cursor"]),
        )

    @property
    def DEFAULT_FONT(self) -> dict:
        return {
            "family": self.TEXT["default"]["cursor"]["family"],
            "style": self.TEXT["default"]["cursor"]["style"],
            "size": self.TEXT["default"]["cursor"]["size"],
        }

    @property
    def TEMPLATE_FONT(self) -> dict:
        return {
            "family": self.TEXT["template"]["cursor"]["family"],
            "style": self.TEXT["template"]["cursor"]["style"],
            "size": self.TEXT["template"]["cursor"]["size"],
        }


CONFIG = Config(fonts=FONTS, settings=SETTINGS, keywords=KEYWORDS)
