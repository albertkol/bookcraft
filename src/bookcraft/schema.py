from typing import Optional

from pydantic import BaseModel


class CursorConfig(BaseModel):
    family: Optional[str] = None
    style: str
    size: Optional[int] = None
    colour: Optional[list[int]] = None
    fill: Optional[list[int]] = None


class TextStyleConfig(BaseModel):
    height: float
    cursor: CursorConfig


class HeadingSpacingConfig(BaseModel):
    height: float


class TextConfig(BaseModel):
    default: TextStyleConfig
    bold: TextStyleConfig
    italic: TextStyleConfig
    underline: TextStyleConfig
    heading: TextStyleConfig
    heading_spacing: HeadingSpacingConfig
    template: TextStyleConfig


class ColourConfig(BaseModel):
    enabled: bool
    italic: bool
    roles: bool
    highlight_roles: bool


class RoleColours(BaseModel):
    dark: list[int]
    light: list[int]


class PageConfig(BaseModel):
    top_margin: int
    margin_size: int
    bottom_margin: int


class TitleConfig(BaseModel):
    text: str


class ChapterEntry(BaseModel):
    path: str
    title: str


class Settings(BaseModel):
    title: TitleConfig
    books: list[ChapterEntry]
    colour: ColourConfig
    text: TextConfig
    roles: dict[str, RoleColours]
    page: PageConfig


class FontEntry(BaseModel):
    family: str
    style: str
    fname: str
