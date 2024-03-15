#input
from PyPDF4 import PdfFileReader, PdfFileWriter

input_pdf = PdfFileReader("hogePDF.pdf",strict=False)
out_pdf = PdfFileWriter()

# 単位（1インチ = 72pt = 25.4mm）
unit = 72/25.4

# A4 = 210mm x 297mm
# A5 = 148mm x 210mm
# 紙の原点は左下、単位は[mm]
Left  = 98 #210/2-148/2
Right = 127 #210/2+148/2
Lower = 265 #297/2-210/2
Upper = 278 #297/2+210/2

# トリミング
for i in range(input_pdf.getNumPages()):
    page = input_pdf.getPage(i)
    lower_left = page.mediaBox.getLowerLeft()
    upper_right = page.mediaBox.getUpperRight()
    page.cropBox.lowerLeft = (Left*unit, Lower*unit)
    page.cropBox.upperRight = (Right*unit, Upper*unit)

    # 書き出しPDFに追加
    out_pdf.addPage(page)

with open("hogeAfterPDF.pdf", "wb") as fp:
    out_pdf.write(fp)