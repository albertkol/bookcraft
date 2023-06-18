from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional, TypeAlias

RGBColour: TypeAlias = tuple[int, int, int]
Page: TypeAlias = list[list[str]]


class OFFICE(Enum):
    MASTER = "W. M."
    SENIOR_WARDEN = "S. W."
    JUNIOR_WARDEN = "J. W."
    SENIOR_DEACON = "S. D."
    JUNIOR_DEACON = "J. D."
    INNER_GUARD = " I. G."
    CANDIDATE = "Can."


class FontStyle(Enum):
    NONE = ""
    BOLD = "B"
    ITALIC = "I"
    ITALICBOLD = "IB"


class Reason(Enum):
    TITLE_RULE = auto()
    ROLE_RULE = auto()
    ROLE_HIGHLIGHT_RULE = auto()
    PARENTHESES_RULE = auto()
    INSIDE_PARENTHESES_RULE = auto()
    INSIDE_UNDERSCORE_RULE = auto()
    KEYWORD_RULE = auto()


@dataclass
class Cursor:
    family: Optional[str] = None
    style: Optional[FontStyle] = None
    size: Optional[int] = None
    colour: Optional[RGBColour] = None
    fill: Optional[RGBColour] = None


@dataclass
class CursorModifier:
    reason: Reason
    cursor: Cursor
    counter: int
    priority: int


@dataclass
class Cell:
    width: float
    height: float
    text: str = ""
    has_border: bool = False
    has_break: bool = False
    has_fill: bool = False
    cursor: Optional[Cursor] = None

    def set_cursor(self, cursor: Cursor):
        self.cursor = cursor
