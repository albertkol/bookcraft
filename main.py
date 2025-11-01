from classes.book import Book
from classes.cell.CellFactory import CellFactory
from classes.config import CONFIG
from classes.cursor.CursorModifierFactory import CursorModifierFactory
from classes.cursor.CursorModifierProcessor import CursorModifierProcessor
from classes.cursor.CursorModifierReducer import CursorModifierReducer
from classes.helpers import get_files

book = Book()
book.set_title(CONFIG.SETTINGS["title"]["text"])
book.set_book_font(CONFIG.FONTS)
for book_title in CONFIG.SETTINGS["books"]:
    book.set_path(CONFIG.BOOKS_PATH + book_title)
    book.set_margin(CONFIG.PAGE)
    book.set_subject(book_title)
    book.set_cm_factory(CursorModifierFactory())
    book.set_cell_factory(CellFactory())
    book.set_cm_processor(CursorModifierProcessor())
    book.set_cm_reducer(CursorModifierReducer())
    book.set_pages(get_files(CONFIG.BOOKS_PATH + book_title))

book.build()
