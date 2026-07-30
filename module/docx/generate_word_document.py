"""
Die Styles sind abhängig von der Vorlage
doc = Document()  => dies öffnet die vorhandene Standardvorlage
doc = Document("Vorlage.docx")
"""

import time
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt, RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

# Neues Word-Dokument erstellen
doc = Document()

####################################################################################
# Header und Footer holen
header = doc.sections[0].header
footer = doc.sections[0].footer

# header
header_paragraph = header.paragraphs[0]
header_paragraph.text = "Hallo"
header_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

# footer
footer_paragraph = footer.paragraphs[0]
footer_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
footer_paragraph.add_run("Seite ")

# PAGE Feld
fld = OxmlElement('w:fldSimple')
fld.set(qn('w:instr'), 'PAGE')
footer_paragraph._element.append(fld)

footer_paragraph.add_run(" von ")
# NUMPAGES (alle seiten) Feld
fld = OxmlElement('w:fldSimple')
fld.set(qn('w:instr'), 'NUMPAGES')
footer_paragraph._element.append(fld)

####################################################################################
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

doc.add_heading("Headline 1", 1)
doc.add_paragraph("Lorem ipsum normaler Text")
doc.add_paragraph("Lorem ipsum normaler Text mit abstand danach").paragraph_format.space_after = Pt(30)
doc.add_paragraph("Lorem ipsum normaler Text mit größeren Text").runs[0].font.size = Pt(20)
doc.add_paragraph("Lorem ipsum normaler Text mit größeren Text").runs[0].font.size = Pt(11)

# Text Fett - Größe -
p1 = doc.add_paragraph()
run = p1.add_run("Lorem ipsum normaler Text")
run.bold = True
run.italic = True
run.underline = True
run.font.size = Pt(20)
run.font.color.rgb = RGBColor(255, 0, 0)

####################################################################################
data = (
    (1, 'Geek 1'),
    (2, 'Geek 2'),
    (3, 'Geek 3')
)
# Creating a table object
table = doc.add_table(rows=1, cols=2)

# Adding heading in the 1st row of the table
row = table.rows[0].cells
row[0].text = 'Id'
row[1].text = 'Name'

# Adding data from the list to the table
for id, name in data:
    # Adding a row and then adding data in it.
    row = table.add_row().cells
    # Converting id to string as table can only take string input
    row[0].text = str(id)
    row[1].text = str(name)

"""
Table Grid → einfache Gitternetzlinien bei allen Zellen
Light Grid → helles Raster
Medium Grid 1/2/3 → mittel-dunkle Raster mit verschiedenen Schattierungen
Light List → Liste ohne dicke Umrandung
Medium List 1/2 → mittlere Listenformate
Light Shading → leichte Hintergrundschattierung
Dark List → dunkle Listentabelle
"""
# styling
table.style = 'Table Grid'










#stamp = int(time.time())
#doc.save(f"generate_word_document_{stamp}.docx")
doc.save(f"generate_word_document.docx")
