


from docx import Document

# Neues Word-Dokument erstellen
#doc = Document()

# von Vorlage
doc = Document("Vorlage.docx")

# Helper: alle styles
for style in doc.styles:
    print(style.type, style.name)

