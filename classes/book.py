from __future__ import annotations

from fpdf import FPDF

from classes.cell.CellFactory import CellFactory
from classes.config import CONFIG, SWITCH
from classes.cursor.CursorModifierFactory import CursorModifierFactory
from classes.cursor.CursorModifierProcessor import CursorModifierProcessor
from classes.cursor.CursorModifierReducer import CursorModifierReducer
from classes.helpers import get_pages
from classes.models import Cell, Context, CursorModifier, Page


class Book(FPDF):
    def __init__(self) -> Book:
        format = (535, 825) if "ra" in SWITCH else (475, 925)

        super().__init__(unit="pt", format=format)

    def header(self) -> None:
        page_no = self.page_no() + 22 if "ra" in SWITCH else self.page_no()

        self.set_font(**CONFIG.TEMPLATE_FONT)
        self.set_text_color(*CONFIG.TEMPLATE_COLOR)
        self.set_draw_color(*CONFIG.TEMPLATE_COLOR)
        width = self.w - self.l_margin - self.r_margin
        height = CONFIG.TEMPLATE_HEIGHT
        page_no_width = self.get_string_width(f"{page_no}")
        subject_width = self.get_string_width(self.subject)
        line_start = self.r_margin
        line_end = self.w - self.r_margin

        if "Cover" not in self.subject:
            self.cell(page_no_width, height, f"{page_no}")
            self.cell(width - page_no_width - subject_width, height, "", 0)
            self.cell(subject_width, height, self.subject, 0, 1)
            self.cell(width, height, "", 0, 1)
            self.dashed_line(line_start, self.y, line_end, self.y, 3, 3)
            self.cell(width, height, "", 0, 1)

    def footer(self) -> None:
        line_start = self.r_margin
        line_end = self.w - self.r_margin
        bottom = self.h - 35

        if "Cover" not in self.subject:
            self.set_font(**CONFIG.TEMPLATE_FONT)
            self.set_text_color(*CONFIG.TEMPLATE_COLOR)
            self.set_draw_color(*CONFIG.TEMPLATE_COLOR)
            self.dashed_line(line_start, bottom, line_end, bottom, 3, 3)

    def set_path(self, book_path: str) -> Book:
        self.book_path = book_path

        return self

    def set_book_font(self, fonts: dict) -> Book:
        [self.add_font(**font, uni=True) for font in fonts]

        return self

    def set_margin(self, page: dict) -> Book:
        self.set_top_margin(page["top_margin"])
        self.set_left_margin(page["margin_size"])
        self.set_right_margin(page["margin_size"])
        self.set_auto_page_break(True, page["bottom_margin"])
        self.c_margin = 0

        return self

    def set_title(self, title: str) -> Book:
        super().set_title(title)

        return self

    def set_subject(self, subject: str) -> Book:
        super().set_subject(subject)

        return self

    def set_cm_reducer(self, cm_reducer: CursorModifierReducer) -> Book:
        self.cm_reducer = cm_reducer

        return self

    def set_cm_processor(self, cm_processor: CursorModifierProcessor) -> Book:
        self.cm_processor = cm_processor

        return self

    def set_cm_factory(self, cm_factory: CursorModifierFactory) -> Book:
        self.cm_factory = cm_factory

        return self

    def set_cell_factory(self, cell_factory: CellFactory) -> Book:
        self.cell_factory = cell_factory

        return self

    def set_pages(self, pages: list[Page]) -> Book:
        self.modifiers: list[CursorModifier] = []

        for page_index in range(1, len(pages) + 1):
            memory = get_pages(self.book_path, page_index, 2)

            self._print_page(memory)

        return self

    def build(self) -> None:
        self.output(f"output/{self.title}.pdf")

    def _print_page(self, memory: list[Page]) -> list[CursorModifier]:
        self.add_page()

        page = memory[0]
        for i in range(len(page)):
            line = page[i]
            body = []

            for j in range(len(line)):
                # get previous cell cursor
                cursor = self.cm_reducer.reduce(self.modifiers)
                context = Context(i, j, memory, CONFIG, cursor)

                new_cms = self.cm_factory.resolve(context)
                self.modifiers.extend(new_cms)
                self.modifiers = self.cm_processor.process(self.modifiers)

                # get current cell cursor
                cursor = self.cm_reducer.reduce(self.modifiers)
                context = Context(i, j, memory, CONFIG, cursor)

                # get new cells
                cells = self.cell_factory.create_cells(context)

                if not cells:
                    continue

                body.extend(cells)

            self._print_line(body, line)

    def _print_line(self, cells: list[Cell], memory_line: list[str]) -> None:
        cells = self._justify_line(cells, memory_line)
        for cell in cells:
            cursor = cell.cursor
            self.set_font(cursor.family, cursor.style, cursor.size)
            self.set_text_color(*cursor.colour)
            self.set_fill_color(*cursor.fill)
            self.set_draw_color(*cursor.fill)

            self.cell(
                w=cell.width,
                h=cell.height,
                txt=cell.text,
                ln=cell.has_break,
                fill=cell.has_fill,
            )

    def _justify_line(self, cells: list[Cell], memory_line: list[str]) -> list[Cell]:
        width = self.w - self.l_margin - self.r_margin
        clean_line_w = 0
        for cell in cells:
            cursor = cell.cursor
            self.set_font(cursor.family, cursor.style, cursor.size)
            cell.width = self.get_string_width(cell.text)
            if cell.text != " ":
                clean_line_w += cell.width

        char_check = any([char in memory_line for char in ["/", "#"]])
        if memory_line.count(" ") and not char_check:
            space_width = (width - clean_line_w) / memory_line.count(" ")
            for cell in cells:
                if cell.text == " ":
                    cell.width = space_width

        return cells
