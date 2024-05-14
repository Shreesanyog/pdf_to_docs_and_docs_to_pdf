from pdf2docx import Converter
old_pdf="Resume_old.pdf"
new_doc="new.docx"
obj=Converter(old_pdf)
obj.convert(new_doc)
obj.close()

# from docx2pdf import convert
# convert("new.docx","new_pdf.pdf")