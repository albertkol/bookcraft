from pdf import PDF
from config import CONFIG


lib_path = CONFIG["path"]
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

pages_in_memory = 2
pages = 5
book = "First Degree"
pdf.set_subject(book)
pdf.set_font("Merriweather", "", 18)
for page_index in range(1, pages + 1):
    memory = []
    path = f"{lib_path}{book}/page-{page_index}.txt"
    with open(path, "rb") as fh:
        page = fh.read().decode("latin-1")

        # set memory for the page
        memory.append(page)
        memory_index = page_index + 1
        for memory_index in range(memory_index, page_index + pages_in_memory):
            path = f"{lib_path}{book}/page-{memory_index}.txt"
            with open(path, "rb") as fh:
                memory.append(fh.read().decode("latin-1"))

        memory = [memory_page.split("\n") for memory_page in memory]
        page = page.split("\n")

        pdf.print_page(page, memory)

pdf.output("output/first.pdf", "F")
