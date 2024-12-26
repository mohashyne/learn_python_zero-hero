def convert():
    # Convert PDF to text
    pdf_path = 'sample.pdf'
    text_path = 'sample.txt'
    pdf = PdfFileReader(pdf_path)
    with open(text_path, 'w') as text_file:
        for page_num in range(pdf.getNumPages()):
            text_file.write(pdf.getPage(page_num).extract_text())

    return text_path