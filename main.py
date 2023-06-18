from config import CONFIG
from helpers import get_files, get_pages
from pdf import PDF

pdf = PDF(unit="pt", format="Legal")

# Adding the fonts
[pdf.add_font(**font, uni=True) for font in CONFIG.FONTS]

# Set margins
pdf.set_top_margin(0)
pdf.set_left_margin(CONFIG.PAGE["margin_size"])
pdf.set_right_margin(CONFIG.PAGE["margin_size"])
pdf.set_auto_page_break(True, CONFIG.PAGE["bottom_margin"])
pdf.c_margin = 0

# books = [p for p in get_files("./books/") if p != "Test"]
books = ["Test"]
for book_title in books:
    books_path = CONFIG.BOOKS_PATH + book_title
    pages = get_files(books_path)
    pdf.set_subject(book_title)
    pdf.set_font(**CONFIG.DEFAULT_FONT)
    for page_index in range(1, len(pages) + 1):
        page = get_pages(books_path, page_index)
        memory = get_pages(books_path, page_index, 2)

        pdf.print_page(page=page, memory=memory)

    pdf.output(f"output/{book_title}.pdf", "F")
