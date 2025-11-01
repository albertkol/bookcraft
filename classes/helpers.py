import os

from classes.models import Page


def get_files(path):
    files = []
    for entry in os.scandir(path):
        files.append(entry.name)
    return files


def get_page(books_path: str, page_index: int):
    path = f"{books_path}/page-{page_index}.txt"
    try:
        with open(path, "rb") as fh:
            return fh.read().decode("latin-1").split("\n")
    except FileNotFoundError:
        pass


def get_pages(path: str, index: int, how_many: int = 1):
    pages = []
    for index in range(index, index + how_many):
        page = get_page(path, index)
        if page is None:
            continue

        pages.append(page)

    if how_many == 1:
        return pages[0]

    return pages


def previous_chars_matches(
    chars: list[str],
    i: int,
    j: int,
    memory: list[Page],
) -> bool:
    match = None
    for char in chars:
        memory_line = memory[0][i]
        start = j - len(char)
        end = j
        # we have to look at next line
        if start < 0:
            try:
                # we have to look at next line too
                memory_line = f"{memory[0][i - 1]} {memory[0][i]}"
                new_j = len(memory[0][i - 1])
                start = new_j - len(char)
                end = new_j
            except IndexError:
                # we hit the end of the page
                continue

        try:
            match = char if char == memory_line[start:end] else None
        except IndexError:
            continue

        if match:
            break

    return match


def next_chars_matches(
    chars: list[str],
    i: int,
    j: int,
    memory: list[Page],
    inclusive: bool = True,
) -> list[str, int]:
    match = None
    match_count = 0
    for char in chars:
        memory_line = memory[0][i]
        breaks_line = False
        start = j if inclusive else j + 1
        end = len(char) + start
        # do we have to look at next line
        if end > len(memory_line):
            breaks_line = True
            try:
                # we have to look at next line too
                memory_line = f"{memory[0][i]} {memory[0][i + 1]}"
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
