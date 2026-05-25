from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional

from typing_extensions import TypeAlias

from bookcraft.config import Config

RGBColour: TypeAlias = list[int]
Page: TypeAlias = list[str]


class OFFICE(Enum):
    MASTER = "W. M."
    SENIOR_WARDEN = "S. W."
    JUNIOR_WARDEN = "J. W."
    SENIOR_DEACON = "S. D."
    JUNIOR_DEACON = "J. D."
    INNER_GUARD = " I. G."
    CANDIDATE = "Can."


class RuleType(Enum):
    TITLE = auto()
    DEFAULT = auto()
    ROLE = auto()
    ROLE_HIGHLIGHT = auto()
    PARENTHESES = auto()
    ITALIC_START = auto()
    ITALIC_END = auto()
    UNDERLINE_START = auto()
    UNDERLINE_END = auto()
    KEYWORD = auto()
    BLANK_SPACE = auto()
    CONTENTS_ITEM = auto()


class MarkerType(Enum):
    START = "start"
    END = "end"


@dataclass
class Cursor:
    family: Optional[str] = None
    style: Optional[str] = None
    size: Optional[int] = None
    colour: Optional[RGBColour] = None
    fill: Optional[RGBColour] = None
    is_italic: bool = False
    is_bold: bool = False
    is_underline: bool = False


@dataclass
class CursorModifier:
    rule: RuleType
    cursor: Cursor
    counter: int


@dataclass
class Cell:
    width: float
    height: float
    text: str = ""
    has_border: bool = False
    has_break: bool = False
    has_fill: bool = False
    cursor: Optional[Cursor] = None


@dataclass
class Context:
    i: int
    j: int
    memory: list[Page]
    config: Config
    cursor: Cursor
