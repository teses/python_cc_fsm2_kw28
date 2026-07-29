


from docx import Document

# Neues Word-Dokument erstellen
doc = Document()

# Titel
doc.add_heading("Titel", level=0)
doc.add_heading("Titel Level 1", level=1)
doc.add_heading("Titel Level 2", level=2)
doc.add_heading("Titel Level 3", level=3)

#
doc.add_paragraph("Title", style='Title')
doc.add_paragraph("Subtitle", style='Subtitle')
doc.add_paragraph("Headline 1", style='Heading 1')
doc.add_paragraph("Headline 2", style='Heading 2')
doc.add_paragraph("Headline 3", style='Heading 3')
doc.add_paragraph("Headline 4", style='Heading 4')
doc.add_paragraph("Headline 5", style='Heading 5')

#
doc.add_paragraph("Auflistung 1", style='List Bullet')
doc.add_paragraph("Auflistung 2", style='List Bullet')
doc.add_paragraph("Auflistung 3", style='List Bullet')
doc.add_paragraph("Auflistung 3.1", style='List Bullet 2')
doc.add_paragraph("Auflistung 3.1.1", style='List Bullet 3')

# normaler Absatz
doc.add_paragraph(
    "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua."
)


doc.save("generate_word_document.docx")
