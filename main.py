from classes.book import Book
from classes.cell.CellFactory import CellFactory
from classes.config import CONFIG
from classes.cursor.CursorModifierFactory import CursorModifierFactory
from classes.cursor.CursorModifierProcessor import CursorModifierProcessor
from classes.cursor.CursorModifierReducer import CursorModifierReducer
from classes.helpers import get_files

# books = ["Test"]
books = [p for p in get_files(CONFIG.BOOKS_PATH) if p != "Test"]

book = Book().set_title("Craft")
for book_title in books:
    book.set_path(CONFIG.BOOKS_PATH + book_title)
    book.set_book_font(CONFIG.FONTS)
    book.set_margin(CONFIG.PAGE)
    book.set_subject(book_title)
    book.set_cm_reducer(CursorModifierReducer())
    book.set_cm_processor(CursorModifierProcessor())
    book.set_cm_factory(CursorModifierFactory())
    book.set_cell_factory(CellFactory())
    book.set_pages(get_files(CONFIG.BOOKS_PATH + book_title))

book.build()
