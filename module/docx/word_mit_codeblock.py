
from docx import Document
from docx.shared import Pt, RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def code_block(doc, text):
    p = doc.add_paragraph()

    # Hintergrundfarbe setzen
    pPr = p._p.get_or_add_pPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:fill"), "EEEEEE")
    pPr.append(shd)

    run = p.add_run(text)
    run.font.name = "Consolas"
    run.font.size = Pt(9)

    return p


from docx import Document

# Neues Word-Dokument erstellen
doc = Document()

# Titel
doc.add_heading("Codeblock", level=0)

code = """
import unittest

class TestRechner():
    pass
"""

code_block(doc, code)


doc.save("word_mit_code.docx")