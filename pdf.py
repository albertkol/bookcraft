import copy

from fpdf import FPDF

from config import CONFIG
from helpers import (
    get_cursor_fill,
    get_previous_cursor,
    next_chars_matches,
    previous_chars_matches,
    same_style,
    set_cursor_pros,
)
from models import Cell, Cursor, Page


class PDF(FPDF):
    def header(self) -> None:
        self._set_style("template")
        width = self.fw - self.l_margin - self.r_margin
        height = CONFIG.TEXT["template"]["height"]
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

        self._set_style("template")
        self.dashed_line(line_start, bottom, line_end, bottom, 3, 3)

    def print_page(self, page: Page, memory: list[Page]) -> None:
        self.add_page()
        # width = self.fw - self.l_margin - self.r_margin
        # body = self._page_body(page)
        # for i in range(len(body)):
        #     body_line = body[i]
        #     for j in range(len(body_line)):
        #         cell = body_line[j]
        #         prev_cursor = get_previous_cursor(body, i, j, self.cursor)
        #         cursor = self._style_cursor(cell, memory, prev_cursor)
        #         cell.set_cursor(cursor)

        # new_body = []
        # for i in range(len(body)):
        #     body_line = body[i]
        #     memory_line = memory[0][i]

        #     # fix italics spacing
        #     clean_line_w = 0
        #     new_cell = None
        #     new_body_line = []
        #     for cell in body_line:
        #         if cell.j in [-1, 100, 101]:
        #             if new_cell:
        #                 clean_line_w = clean_line_w + new_cell.width
        #                 new_body_line.append(new_cell)
        #                 new_cell = None

        #             new_body_line.append(cell)
        #             continue

        #         if cell.text == " ":
        #             if new_cell:
        #                 clean_line_w = clean_line_w + new_cell.width
        #                 new_body_line.append(new_cell)
        #                 new_cell = None

        #             new_body_line.append(cell)
        #             continue

        #         if not new_cell:
        #             new_cell = copy.copy(cell)
        #             continue

        #         if not same_style(new_cell, cell):
        #             clean_line_w = clean_line_w + new_cell.width
        #             new_body_line.append(new_cell)
        #             new_cell = copy.copy(cell)
        #             continue

        #         new_cell.text = new_cell.text + cell.text
        #         cursor = new_cell.cursor
        #         self.set_font(cursor.font, cursor.style, cursor.size)
        #         new_cell.width = self.get_string_width(new_cell.text)

        #     # justify line
        #     char_check = any([char in memory_line for char in ["<<", "##"]])
        #     if memory_line.count(" ") and not char_check:
        #         space_width = (width - clean_line_w) / memory_line.count(" ")
        #         for cell in new_body_line:
        #             if cell.text != " ":
        #                 continue

        #             cell.width = space_width

        #     new_body.append(new_body_line)

        # for new_body_line in new_body:
        #     for cell in new_body_line:
        #         cursor = cell.cursor
        #         self.set_font(cursor.font, cursor.style, cursor.size)
        #         self.set_text_color(*cursor.colour)
        #         self.set_fill_color(*cursor.fill)
        #         self.set_draw_color(*cursor.fill)

        #         if CONFIG["black_and_white"] or not CONFIG["roles_colouring"]:
        #             self.set_fill_color(255)
        #             self.set_draw_color(255)

        #         if CONFIG["black_and_white"]:
        #             self.set_text_color(000)

        #         self.cell(
        #             w=cell.width,
        #             h=cell.height * cell.height_muliplier,
        #             txt=cell.text,
        #             ln=cell.has_br,
        #             fill=cell.has_fill,
        #         )
        # else:
        #     self.cursor = cell.cursor

    # def _page_body(self, lines: list[str]) -> list[list[Cell]]:
    #     body = []
    #     width = self.fw - self.l_margin - self.r_margin
    #     d_height = CONFIG["default"]["height"]
    #     t_height = CONFIG["title"]["height"]
    #     th_multip = CONFIG["title"]["height_muliplier"]

    #     for i in range(len(lines)):
    #         body_line = []
    #         line = lines[i]

    #         # add line high before heading if not 1st line on the page
    #         if "##" in line and i > 0:
    #             cell = Cell(i, -1, "", 0, t_height, th_multip, True, False)
    #             body_line.append(cell)

    #         for j in range(len(line)):
    #             # skip special chars
    #             if line[j] in [">", "<", "_", "#"]:
    #                 continue

    #             # add rest of char
    #             char_w = self.get_string_width(line[j])
    #             cell = Cell(i, j, line[j], char_w, d_height, has_fill=True)
    #             body_line.append(cell)

    #         # break line at the end
    #         cell = Cell(i, 100, "", 0, d_height, has_br=True)
    #         body_line.append(cell)

    #         if "##" in line:
    #             try:
    #                 next_line = lines[i + 1]
    #             except IndexError:
    #                 next_line = None

    #             # add line high after heading
    #             if "##" not in next_line:
    #                 cell = Cell(i, 101, "", width, t_height, th_multip, True)
    #                 body_line.append(cell)

    #         body.append(body_line)

    #         cell_array = []

    #         rules = [
    #             CellCreationRule(
    #                 CharEqualsSpecification("#"),
    #                 CreateMultipleCellsAction("#", 3),
    #             ),
    #             CellCreationRule(CharEqualsSpecification("_"), None),
    #         ]

    #         for string in strings:
    #             for char in string:
    #                 for rule in rules:
    #                     if rule.specification.is_satisfied(char):
    #                         action = rule.action
    #                         if action is not None:
    #                             cells = action.perform_action(char)
    #                             cell_array.extend(cells)
    #                         break
    #                 else:
    #                     cell_array.append(Cell(char))

    #         return cell_array
    #     return body

    # def _style_cursor(
    #     self,
    #     cell: Cell,
    #     memory: list[list[str]],
    #     previous_cursor: Cursor,
    # ) -> Cursor:
    #     cursor = copy.copy(previous_cursor)

    #     if cell.j in [-1, 100, 101]:
    #         return cursor

    #     # add header styling
    #     if "##" in memory[0][cell.i]:
    #         return set_cursor_pros(cursor, CONFIG["title"])

    #     # reset for new role
    #     if previous_chars_matches([">>"], cell, memory):
    #         cursor.role = ""
    #         roles = CONFIG["roles"].keys()
    #         cursor.role, dark_count = next_chars_matches(roles, cell, memory)
    #         cursor = set_cursor_pros(cursor, CONFIG["default"])
    #         cursor.dark_count = dark_count + 1 if CONFIG["dark_roles"] else 0
    #         cursor.fill = get_cursor_fill(cursor, CONFIG["roles"])

    #     if not cursor.is_italic and cursor.fill == [255]:
    #         cursor.fill = get_cursor_fill(cursor, CONFIG["roles"])

    #     # Check for `(` and `)`
    #     if cell.text in ["(", ")"]:
    #         cursor = set_cursor_pros(cursor, CONFIG["bold"])
    #         cursor.bold_count = 1

    #         return cursor

    #     # check bold counter and reset if necessary
    #     if cursor.bold_count != 0:
    #         cursor.bold_count = cursor.bold_count - 1
    #         if cursor.bold_count == 0:
    #             cursor.is_bold = False
    #             if cursor.is_italic:
    #                 cursor = set_cursor_pros(cursor, CONFIG["italic"])
    #             else:
    #                 cursor = set_cursor_pros(cursor, CONFIG["default"])
    #                 cursor.fill = get_cursor_fill(cursor, CONFIG["roles"])

    #     # check italic counter and reset if necessary
    #     if cursor.italic_count != 0:
    #         cursor.italic_count = cursor.italic_count - 1
    #         if cursor.italic_count == 0:
    #             cursor.is_italic = False
    #             if cursor.is_bold:
    #                 cursor = set_cursor_pros(cursor, CONFIG["bold"])
    #             else:
    #                 cursor = set_cursor_pros(cursor, CONFIG["default"])
    #             cursor.fill = get_cursor_fill(cursor, CONFIG["roles"])

    #     # Check for italic end
    #     if cursor.is_italic:
    #         match, _ = next_chars_matches(["__", ")"], cell, memory, False)
    #         if match:
    #             cursor.italic_count = 1

    #     # Check for italic start
    #     if not cursor.is_italic:
    #         if previous_chars_matches(["__", "("], cell, memory):
    #             cursor = set_cursor_pros(cursor, CONFIG["italic"])
    #             cursor.is_italic = True
    #             cursor.italic_count = -1

    #     # Bold words
    #     if not cursor.is_bold:
    #         match, bold_count = next_chars_matches(BOLDED_LIST, cell, memory)
    #         if match:
    #             cursor.style = CONFIG["bold"]["style"]
    #             cursor.bold_count = bold_count

    #     if not cursor.is_italic:
    #         if previous_chars_matches(["__", ")"], cell, memory):
    #             cursor.fill = [255]

    #         matches, _ = next_chars_matches(["__", "("], cell, memory, False)
    #         if matches:
    #             cursor.fill = [255]

    #     # check dark counter
    #     if cursor.dark_count != 0:
    #         cursor.dark_count = cursor.dark_count - 1
    #         if cursor.dark_count == 0:
    #             cursor.fill = [255]

    #     return cursor

    def _set_style(self, style_name: str) -> None:
        self.set_font(*list(CONFIG.TEXT[style_name]["cursor"].values())[:3])
        self.set_draw_color(*CONFIG.TEXT[style_name]["cursor"]["colour"])
        self.set_text_color(*CONFIG.TEXT[style_name]["cursor"]["colour"])
        self.set_fill_color(*CONFIG.TEXT[style_name]["cursor"]["fill"])
