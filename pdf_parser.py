def parse_pdf_pages(pages):
    result = []

    for page in pages:
        if page == "":
            result.append("\n--- PAGE BREAK ---\n")
        else:
            result.append(page)

    return "" .join(result)

pages = [
    "Page 1 content",
    "",
    "Page 2 content"
]

print(parse_pdf_pages(pages))
