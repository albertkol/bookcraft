from helpers import get_files
from pdf import PDF
from config import CONFIG


pdf = PDF("P", "pt", "legal")

# Adding the fonts
for font in CONFIG["fonts"]:
    pdf.add_font(font["name"], font["style"], font["path"], True)

# Set margins
pdf.set_top_margin(0)
pdf.set_left_margin(CONFIG["margin_size"])
pdf.set_right_margin(CONFIG["margin_size"])
pdf.set_auto_page_break(1, CONFIG["margin_size"] - 25)
pdf.c_margin = 0

for book_title in get_files(CONFIG["path"]):
    book_path = CONFIG["path"] + "/" + book_title
    pages = get_files(book_path)
    pdf.set_subject(book_title)
    pdf.set_font("Merriweather", "", 18)
    for page_index in range(1, len(pages) + 1):
        memory = []
        path = f"{book_path}/page-{page_index}.txt"
        with open(path, "rb") as fh:
            page = fh.read().decode("latin-1")

        # set memory for the page
        memory.append(page)
        if page_index < len(pages):
            memory_index = page_index + 1
            path = f"{book_path}/page-{memory_index}.txt"
            with open(path, "rb") as fh:
                memory.append(fh.read().decode("latin-1"))

        memory = [memory_page.split("\n") for memory_page in memory]
        page = page.split("\n")

        pdf.print_page(page, memory)

    if pages:
        pdf.output(f"output/{book_title}.pdf", "F")
