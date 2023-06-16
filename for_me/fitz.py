import fitz

file = '11АТ.pdf'

pdf = fitz.Document(file)

for image in pdf.getPageImageList(0):
    xref = image[0]
    pix = fitz.Pixmap(pdf, xref)
    pix._writeIMG(filename='output.jpg', format='jpg')