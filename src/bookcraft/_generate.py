from bookcraft.book import Book
from bookcraft.cell.CellFactory import CellFactory
from bookcraft.config import load_config
from bookcraft.cursor.CursorModifierFactory import CursorModifierFactory
from bookcraft.cursor.CursorModifierProcessor import CursorModifierProcessor
from bookcraft.cursor.CursorModifierReducer import CursorModifierReducer
from bookcraft.helpers import get_files

_SWITCH_MAP = {
    "craft": "c-",
    "craft-dark": "c-dark-",
    "ra": "ra-",
    "ra-dark": "ra-dark-",
}


def generate(
    books_path: str,
    settings_path: str,
    fonts_path: str,
    keywords_path: str,
    output_path: str,
    mode: str = "craft",
) -> None:
    if mode not in _SWITCH_MAP:
        raise ValueError(
            f"Unknown mode '{mode}'. Choose from: {', '.join(_SWITCH_MAP)}"
        )

    switch = _SWITCH_MAP[mode]
    config = load_config(books_path, settings_path, fonts_path, keywords_path, switch)

    book = Book(config)
    book.set_title(config.settings.title.text)
    book.set_book_font(config.fonts)

    for chapter in config.settings.books:
        if config.is_dark:
            book.page_background = (18, 18, 18)

        book.set_path(books_path + chapter.path)
        book.configure_margins(config.page)
        book.set_subject(chapter.title)
        book.set_cm_factory(CursorModifierFactory())
        book.set_cell_factory(CellFactory())
        book.set_cm_processor(CursorModifierProcessor())
        book.set_cm_reducer(CursorModifierReducer())
        book.set_pages(get_files(books_path + chapter.path))

    book.build(output_path)
