"""Working with PDF files."""

# Install PyPDF2: pip install PyPDF2

import PyPDF2

# Paths to the PDF files
first_file = "Section-5/8-pdf/pyschology.pdf"
second_file = "Section-5/8-pdf/invoice.pdf"

# Open the first PDF file
with open(first_file, "rb") as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)
    print(f"Number of pages in {first_file}: {len(reader.pages)}")  # 306

# Open the second PDF file
with open(second_file, "rb") as pdf_file_two:
    reader_two = PyPDF2.PdfReader(pdf_file_two)
    print(f"Number of pages in {second_file}: {len(reader_two.pages)}")  # 1
    
    # Uncomment the block below to extract and print content from the second file
    # Iterate through the pages and print their content
    # for page_number, page in enumerate(reader_two.pages, start=1):
    #     print(f"Page {page_number}:")
    #     print(page.extract_text())
    #     print("-" * 40)

# Rotate the first page of the first PDF file
with open(first_file, "rb") as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)
    writer = PyPDF2.PdfWriter()

    page = reader.pages[0]  # Get the first page
    rotated_page = page.rotate(90)  # Rotate the page by 90 degrees

    writer.add_page(rotated_page)

    # Write the rotated page to a new PDF file
    with open("rotated.pdf", "wb") as rotated_file:
        writer.write(rotated_file)

    print("Rotated page saved as 'rotated.pdf'")



"""Merging multiple PDF files."""


# List of PDF files to merge
pdf_files = [
    "Section-5/8-pdf/pyschology.pdf",
    "Section-5/8-pdf/invoice.pdf",
]

# Create a PdfWriter object
writer = PyPDF2.PdfWriter()

# Loop through each file and add its pages to the writer
for pdf_file in pdf_files:
    with open(pdf_file, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            writer.add_page(page)  # Add each page to the writer

# Save the merged PDF to a new file
output_file = "merged.pdf"
with open(output_file, "wb") as merged_file:
    writer.write(merged_file)

print(f"Merged PDF saved as '{output_file}'")
