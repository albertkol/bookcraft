from dataclasses import dataclass


@dataclass
class Cursor:
    font: str
    style: str
    size: int
    colour: list[int]
    fill: list
    bold_count: int = 0
    italic_count: int = 0
    role: str = ""
    is_italic: bool = False
    is_bold: bool = False
    dark_count: int = 0


@dataclass
class Cell:
    i: int
    j: int
    text: str = ""
    width: float = 0
    height: float = 18
    height_muliplier: float = 1
    has_br: bool = False
    has_fill: bool = False
    cursor: Cursor = None

    def set_cursor(self, cursor: Cursor):
        self.cursor = cursor
