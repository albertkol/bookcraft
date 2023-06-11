from classes import Cell, Cursor


def clear_line(line: str, leave_spaces: bool = True) -> str:
    line = line.replace("##", "")
    line = line.replace(">>", "")
    line = line.replace("<<", "")
    line = line.replace("__", "")
    if not leave_spaces:
        line = line.replace(" ", "")

    return line


def previous_chars_matches(
    chars: list[str],
    cell: Cell,
    memory: list[list[str]],
) -> bool:
    j = cell.j
    match = None
    memory_line = memory[0][cell.i]
    for char in chars:
        start = j - len(char)

        try:
            match = char if char == memory_line[start:j] else None
        except IndexError:
            continue

        if match:
            break

    return match


def next_chars_matches(
    chars: list[str],
    cell: Cell,
    memory: list[list[str]],
    inclusive: bool = True,
) -> list[str, int]:
    i = cell.i
    j = cell.j
    match = None
    match_count = 0
    memory_line = memory[0][i]
    for char in chars:
        breaks_line = False
        start = j if inclusive else j + 1
        end = len(char) + start
        # do we have to look at next line
        if end > len(memory_line):
            breaks_line = True
            try:
                # we have to look at next line too
                memory_line = f"{memory[0][i]} {memory[0][i+1]}"
            except IndexError:
                try:
                    # we have to look at next page 1st line too
                    memory_line = f"{memory[0][i]} {memory[1][0]}"
                except IndexError:
                    # we hit the end of the book
                    continue

        try:
            match = char if char == memory_line[start:end] else None
        except IndexError:
            continue

        if match:
            break

    if match:
        match_count = len(match) - 1 if breaks_line else len(match)

    return match, match_count


def get_previous_cursor(
    body: list[list[Cell]],
    i: int,
    j: int,
    default_cursor: Cursor,
) -> Cursor:
    if (j - 1) >= 0:
        prev_cell: Cell = body[i][j - 1]
    elif (i - 1) >= 0:
        # go to previous line to get its last cell
        prev_cell: Cell = body[i - 1][-1]
    else:
        # there is no previous cell
        prev_cell = None

    previous_cursor = default_cursor
    if prev_cell and prev_cell.cursor:
        previous_cursor = prev_cell.cursor

    return previous_cursor


def set_cursor_pros(cursor: Cursor, config: dict) -> Cursor:
    cursor.font = config["font"]
    cursor.style = config["style"]
    cursor.size = config["size"]
    cursor.colour = config["colour"]
    cursor.fill = config["fill"]

    cursor.is_italic = True if "I" in cursor.style else False
    cursor.is_bold = True if "B" in cursor.style else False

    return cursor


def get_cursor_fill(cursor: Cursor, roles: dict) -> Cursor:
    is_dark = cursor.dark_count > 0

    if not cursor.role:
        return [255]

    if is_dark:
        return roles[cursor.role]["dark"]
    else:
        return roles[cursor.role]["light"]
