import copy
from fpdf import FPDF
from config import BOLDED_LIST, CONFIG
from classes import Cursor, Cell

from helpers import (
    clear_line,
    get_cursor_fill,
    get_previous_cursor,
    next_chars_matches,
    previous_chars_matches,
    set_cursor_pros,
)


class PDF(FPDF):
    cursor = Cursor(
        CONFIG["default"]["font"],
        CONFIG["default"]["style"],
        CONFIG["default"]["size"],
        CONFIG["default"]["colour"],
        CONFIG["default"]["fill"],
    )

    def header(self) -> None:
        self.set_font(
            CONFIG["header"]["font"],
            CONFIG["header"]["style"],
            CONFIG["header"]["size"],
        )
        self.set_draw_color(*CONFIG["header"]["colour"])
        self.set_text_color(*CONFIG["header"]["colour"])
        self.set_fill_color(*CONFIG["header"]["fill"])
        width = self.fw - self.l_margin - self.r_margin
        height = CONFIG["header"]["height"]
        page_no_width = self.get_string_width(f"{self.page_no()}")
        subject_width = self.get_string_width(self.subject)
        line_start = self.r_margin
        line_end = self.fw - self.r_margin

        self.cell(width, height, "", 0, 1)
        self.cell(width, height, "", 0, 1)
        self.cell(width, height, "", 0, 1)
        self.dashed_line(line_start, self.y, line_end, self.y, 3, 3)
        self.cell(width, height, "", 0, 1)
        self.cell(page_no_width, height, f"{self.page_no()}")
        self.cell(width - page_no_width - subject_width, height, "", 0)
        self.cell(subject_width, height, self.subject, 0, 1)
        self.cell(width, height, "", 0, 1)
        self.dashed_line(line_start, self.y, line_end, self.y, 3, 3)
        self.cell(width, height, "", 0, 1)

    def footer(self) -> None:
        line_start = self.r_margin
        line_end = self.fw - self.r_margin
        bottom = self.fh - 75

        self.set_draw_color(*CONFIG["header"]["colour"])
        self.dashed_line(line_start, bottom, line_end, bottom, 3, 3)

    def print_page(self, page: list[str], memory: list[list[str]]) -> None:
        self.add_page()
        width = self.fw - self.l_margin - self.r_margin
        body = self._page_body(page)
        for i in range(len(body)):
            body_line = body[i]
            for j in range(len(body_line)):
                cell = body_line[j]
                prev_cursor = get_previous_cursor(body, i, j, self.cursor)
                cursor = self._style_cursor(cell, memory, prev_cursor)
                cell.set_cursor(cursor)

        for i in range(len(body)):
            body_line = body[i]
            memory_line = memory[0][i]

            # fix italics spacing
            clean_line_w = 0
            for cell in body_line:
                if cell.j in [-1, 100, 101]:
                    continue

                if cell.text == " ":
                    continue

                if "I" in cell.cursor.style:
                    cell.width = cell.width - 0.8

                clean_line_w = clean_line_w + cell.width

            # justify line
            if memory_line.count(" ") and "<<" not in memory_line:
                space_width = (width - clean_line_w) / memory_line.count(" ")
                for cell in body_line:
                    if cell.text != " ":
                        continue

                    cell.width = space_width

            for cell in body_line:
                cursor = cell.cursor
                self.set_font(cursor.font, cursor.style, cursor.size)
                self.set_text_color(*cursor.colour)
                self.set_fill_color(*cursor.fill)
                self.set_draw_color(*cursor.fill)

                self.cell(
                    w=cell.width,
                    h=cell.height * cell.height_muliplier,
                    txt=cell.text,
                    ln=cell.has_br,
                    fill=cell.has_fill,
                )
        else:
            self.cursor = cell.cursor

    def _page_body(self, lines: list[str]) -> list[list[Cell]]:
        body = []
        width = self.fw - self.l_margin - self.r_margin
        d_height = CONFIG["default"]["height"]
        t_height = CONFIG["title"]["height"]
        th_multip = CONFIG["title"]["height_muliplier"]
        for i in range(len(lines)):
            body_line = []
            line = lines[i]

            try:
                next_line = lines[i + 1]
            except IndexError:
                next_line = None

            if "##" in line:
                # add line high before heading if not 1st line on the page
                if i > 0:
                    cell = Cell(i, -1, "", 0, t_height, th_multip, True, False)
                    body_line.append(cell)

                clean_line = clear_line(line)
                cell = Cell(i, 0, clean_line, width, t_height, th_multip, True)
                body_line.append(cell)

                # add line high after heading
                if "##" not in next_line:
                    cell = Cell(i, 101, "", width, t_height, th_multip, True)
                    body_line.append(cell)

                body.append(body_line)
                continue

            for j in range(len(line)):
                # skip special chars
                if line[j] in [">", "<", "_", "#"]:
                    continue

                # add rest of char
                char_w = self.get_string_width(line[j])
                cell = Cell(i, j, line[j], char_w, d_height, has_fill=True)
                body_line.append(cell)

            # break line at the end
            cell = Cell(i, 100, "", 0, d_height, has_br=True)
            body_line.append(cell)

            body.append(body_line)

        return body

    def _style_cursor(
        self,
        cell: Cell,
        memory: list[list[str]],
        previous_cursor: Cursor,
    ) -> Cursor:
        cursor = copy.copy(previous_cursor)

        if cell.j in [-1, 100, 101]:
            return cursor

        # add header styling
        if "##" in memory[0][cell.i]:
            return set_cursor_pros(cursor, CONFIG["title"])

        # reset for new role
        if previous_chars_matches([">>"], cell, memory):
            roles = CONFIG["roles"].keys()
            cursor.role, dark_count = next_chars_matches(roles, cell, memory)
            cursor = set_cursor_pros(cursor, CONFIG["default"])
            cursor.dark_count = dark_count + 1
            cursor.fill = get_cursor_fill(cursor, CONFIG["roles"])

        if not cursor.is_italic and cursor.fill == [255]:
            cursor.fill = get_cursor_fill(cursor, CONFIG["roles"])

        # Check for `(` and `)`
        if cell.text in ["(", ")"]:
            cursor = set_cursor_pros(cursor, CONFIG["bold"])
            cursor.bold_count = 1

            return cursor

        # check bold counter and reset if necessary
        if cursor.bold_count != 0:
            cursor.bold_count = cursor.bold_count - 1
            if cursor.bold_count == 0:
                cursor.is_bold = False
                if cursor.is_italic:
                    cursor = set_cursor_pros(cursor, CONFIG["italic"])
                else:
                    cursor = set_cursor_pros(cursor, CONFIG["default"])
                    cursor.fill = get_cursor_fill(cursor, CONFIG["roles"])

        # check italic counter and reset if necessary
        if cursor.italic_count != 0:
            cursor.italic_count = cursor.italic_count - 1
            if cursor.italic_count == 0:
                cursor.is_italic = False
                if cursor.is_bold:
                    cursor = set_cursor_pros(cursor, CONFIG["bold"])
                else:
                    cursor = set_cursor_pros(cursor, CONFIG["default"])
                cursor.fill = get_cursor_fill(cursor, CONFIG["roles"])

        # Check for italic end
        if cursor.is_italic:
            match, _ = next_chars_matches(["__", ")"], cell, memory, False)
            if match:
                cursor.italic_count = 1

        # Check for italic start
        if not cursor.is_italic:
            if previous_chars_matches(["__", "("], cell, memory):
                cursor = set_cursor_pros(cursor, CONFIG["italic"])
                cursor.is_italic = True
                cursor.italic_count = -1

        # Bold words
        if not cursor.is_bold:
            match, bold_count = next_chars_matches(BOLDED_LIST, cell, memory)
            if match:
                cursor.style = CONFIG["bold"]["style"]
                cursor.bold_count = bold_count

        if not cursor.is_italic:
            if previous_chars_matches(["__", ")"], cell, memory):
                cursor.fill = [255]

            matches, _ = next_chars_matches(["__", "("], cell, memory, False)
            if matches:
                cursor.fill = [255]

        # check dark counter
        if cursor.dark_count != 0:
            cursor.dark_count = cursor.dark_count - 1
            if cursor.dark_count == 0:
                cursor.fill = [255]

        return cursor
