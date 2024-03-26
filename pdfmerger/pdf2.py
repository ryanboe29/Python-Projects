import PyPDF2

template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))  #this merges the pages unlike PyPDF2.PdfFileMerger() which takes them and puts them one after another
    output.addPage(page)

    with open('watermarked_ouput.pdf', 'wb') as file:
        output.write(file)