

from fpdf import FPDF


# PDF-Dokument erstellen
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.set_font("helvetica", style="B", size=16)
pdf.set_margins(
    left=20,
    top=20,
    right=20
)

# Zelle - die danach den x cursor wieder nach links automatisch mit  new_x="LEFT"
text1 = "Dies ist der erste Textblock. Er enthält mehrere Zeilen und wird automatisch umgebrochen."
pdf.multi_cell(w=100, h=6, text=text1, border=1, align='L', new_x="LEFT")

# Zelle - die danach den x cursor wieder nach links setzt manuell
text2 = "Dies ist der zweite Textblock. Auch dieser wird umgebrochen und erscheint unter dem ersten."
pdf.multi_cell(w=100, h=6, text=text2, border=1, align='L')
pdf.set_x(pdf.l_margin)

# Text
text2 = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua."
pdf.multi_cell(w=100, h=6, text=text2, border=1, align='L', new_x="LEFT")

# leere zeilenzelle
pdf.ln()

# Text mit voller breite
text2 = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua."
pdf.multi_cell(w=100, h=6, text=text2, border=1, align='L', new_x="LEFT")



# PDF speichern
pdf_path = "simple.pdf"
pdf.output(pdf_path)

