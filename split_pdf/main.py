import math

from PyPDF2 import PdfFileReader, PdfFileWriter

file_name = "test.pdf"
pdf = PdfFileReader(file_name)

page_number = pdf.getNumPages()
frame = math.ceil(page_number / 4)
for i in range(frame):
    pdf_writer = PdfFileWriter()
    for j in range(4):
        added_page_number = 4 * i + j
        if added_page_number < page_number:
            pdf_writer.addPage(pdf.getPage(added_page_number))
    output_filename = '{}.pdf'.format(i)
    with open(output_filename, 'wb') as out:
        pdf_writer.write(out)
        print('Created ' + str(i))
