from fpdf import FPDF


class RechnungPDF(FPDF):

    def __init__(self):
        super().__init__("P", "mm", "A4")
        self.set_auto_page_break(False)

    def header(self):
        # Kopfzeile "Anhang"
        #self.set_fill_color(230, 230, 230)
        #self.set_draw_color(160, 160, 160)
        #self.rect(20, 14, 190, 7, style="DF")

        #self.set_font("Helvetica", "", 7)
        #self.set_text_color(100, 100, 100)
        #self.set_xy(190, 15)
        #self.cell(17, 5, "Anhang", align="R")

        self.set_text_color(0, 0, 0)

    def footer(self):
        # Seitenzahl
        self.set_font("Helvetica", "", 8)
        self.set_xy(190, 285)
        self.cell(15, 5, str(self.page_no()), align="R")


pdf = RechnungPDF()
pdf.add_page()

# ------------------------------------------------------------
# Rahmen der Rechnung
# ------------------------------------------------------------

# pdf.set_draw_color(100, 100, 100)
# pdf.rect(20, 24, 190, 242)

# ------------------------------------------------------------
# Logo
# ------------------------------------------------------------

# Einfaches Logo als Text
pdf.set_xy(28, 34)

pdf.set_fill_color(80, 70, 70)
pdf.rect(28, 34, 88, 20, "F")

pdf.set_text_color(255, 255, 255)
pdf.set_font("Helvetica", "B", 18)
pdf.set_xy(30, 38)
pdf.cell(48, 8, "Print")

pdf.set_text_color(210, 210, 210)
pdf.set_xy(75, 38)
pdf.cell(25, 8, "Top")

pdf.set_text_color(220, 220, 220)
pdf.set_font("Helvetica", "B", 9)
pdf.set_xy(100, 42)
pdf.cell(15, 5, "GmbH")

pdf.set_text_color(0, 0, 0)

# ------------------------------------------------------------
# Absender
# ------------------------------------------------------------

pdf.set_font("Helvetica", "", 8)

pdf.set_xy(28, 58)
pdf.cell(
    100,
    4,
    "PrintTop GmbH, Schöne Aussicht 1, 60314 Frankfurt"
)

# ------------------------------------------------------------
# Kunde
# ------------------------------------------------------------

pdf.set_font("Helvetica", "", 10)

pdf.set_xy(28, 70)
pdf.multi_cell(
    70,
    5,
    "IT-Solution GmbH\n"
    "Hauptstraße 36\n"
    "01219 Dresden"
)

# ------------------------------------------------------------
# Rechte Informationsspalte
# ------------------------------------------------------------

pdf.set_xy(130, 70)

pdf.set_font("Helvetica", "", 9)

pdf.multi_cell(
    70,
    4.5,
    "Ihr Zeichen / Ansprechpartner\n"
    "fs | Frank Schürr\n\n"
    "Unser Zeichen / Ansprechpartner\n"
    "1234-1 | Rolf Lorey\n\n"
    "E-Mail\n"
    "rolf.lorey@printtop.de\n\n"
    "Telefon | Fax\n"
    "035207 1234-5678\n"
    "035207 1234-5679\n\n"
    "Datum\n"
    "tt.mm.jjjj"
)

# ------------------------------------------------------------
# Rechnungsnummern
# ------------------------------------------------------------

pdf.set_font("Helvetica", "B", 8)

daten = [
    ("Kundennummer:", "4723"),
    ("Angebot-Nummer:", "130187"),
    ("Lieferschein-Nummer:", "4723-19"),
    ("Rechnungs-Nummer:", "100709"),
]

y = 126

for bezeichnung, wert in daten:
    pdf.set_xy(29, y)
    pdf.cell(42, 4, bezeichnung)

    pdf.set_font("Courier", "", 9)
    pdf.cell(30, 4, wert)

    pdf.set_font("Helvetica", "B", 8)

    y += 4

# ------------------------------------------------------------
# Bestellung / Lieferung
# ------------------------------------------------------------

pdf.set_xy(29, 146)

pdf.set_font("Helvetica", "B", 8)

pdf.cell(
    170,
    5,
    "Ihre Bestellung vom tt.mm.jjjj, unsere Lieferung vom tt.mm.jjjj"
)

# ------------------------------------------------------------
# Überschrift
# ------------------------------------------------------------

pdf.set_xy(29, 157)

pdf.set_font("Helvetica", "B", 16)
pdf.cell(60, 8, "Rechnung")

# ------------------------------------------------------------
# Positionstabelle
# ------------------------------------------------------------

x = 29
y = 166

# Spaltenbreiten
spalten = [14, 27, 78, 15, 33]

# Kopfzeile
pdf.set_font("Helvetica", "B", 8)
pdf.set_draw_color(130, 130, 130)

headers = [
    "Pos.",
    "Artikel-Nr.",
    "Bezeichnung",
    "Menge",
    "Einzelpreis\n(EUR)"
]

for i, breite in enumerate(spalten):
    pdf.rect(x, y, breite, 13)

    pdf.set_xy(x, y + 2)

    pdf.multi_cell(
        breite,
        4,
        headers[i],
        align="C"
    )

    x += breite

# Gesamtpreis-Spalte
# Die Vorlage hat die Gesamtpreis-Spalte als letzte Spalte
pdf.rect(196, y, 28, 13)

pdf.set_xy(196, y + 2)
pdf.multi_cell(
    28,
    4,
    "Gesamtpreis\n(EUR)",
    align="C"
)

# ------------------------------------------------------------
# Position
# ------------------------------------------------------------

y += 13
x = 29

werte = [
    ("1", 14, "L"),
    ("810715", 27, "L"),
    ("Print Fusion 3D", 78, "L"),
    ("3", 15, "C"),
    ("4.450,00", 33, "R"),
]

pdf.set_font("Courier", "", 9)

for text, breite, align in werte:
    pdf.rect(x, y, breite, 8)
    pdf.set_xy(x + 2, y + 2)
    pdf.cell(breite - 4, 4, text, align=align)
    x += breite

pdf.rect(196, y, 28, 8)
pdf.set_xy(196, y + 2)
pdf.cell(26, 4, "13.350,00", align="R")

# ------------------------------------------------------------
# Summenblock
# ------------------------------------------------------------

y = 187

# Linke Seite leer lassen
# Rechter Summenbereich
x = 145
w_label = 38
w_value = 41

pdf.set_font("Helvetica", "", 8)

summen = [
    ("Rabatt  (6 %)", "- 801,00"),
    ("Nettopreis", "12.549,00"),
    ("MwSt.  (19 %)", "2.384,31"),
]

for label, value in summen:

    pdf.rect(x, y, w_label, 7)
    pdf.rect(x + w_label, y, w_value, 7)

    pdf.set_xy(x + 2, y + 1.5)
    pdf.cell(w_label - 4, 4, label, align="R")

    pdf.set_xy(x + w_label + 2, y + 1.5)
    pdf.cell(w_value - 4, 4, value, align="R")

    y += 7

# Rechnungsbetrag
pdf.set_font("Helvetica", "B", 8)

pdf.rect(x, y, w_label, 8)
pdf.rect(x + w_label, y, w_value, 8)

pdf.set_xy(x + 2, y + 2)
pdf.cell(w_label - 4, 4, "Rechnungsbetrag", align="R")

pdf.set_xy(x + w_label + 2, y + 2)
pdf.cell(w_value - 4, 4, "14.933,31", align="R")

# ------------------------------------------------------------
# Zahlungshinweis
# ------------------------------------------------------------

pdf.set_font("Helvetica", "", 8)

pdf.set_xy(29, 208)

pdf.multi_cell(
    160,
    4,
    "Die Rechnung ist unter Abzug von 2 % Skonto bis zum tt.mm.jjjj zahlbar.\n"
    "Ab dem tt.mm.jjjj tritt ohne weitere Nachricht Verzug ein."
)

# ------------------------------------------------------------
# Grußformel
# ------------------------------------------------------------

pdf.set_xy(29, 224)

pdf.cell(100, 4, "Mit freundlichen Grüßen")

pdf.set_xy(29, 229)
pdf.cell(100, 4, "PrintTop GmbH")

# Unterschrift
pdf.set_font("Courier", "", 14)
pdf.set_xy(30, 237)
pdf.cell(40, 7, "i. A. Lorey")

# ------------------------------------------------------------
# Fußbereich
# ------------------------------------------------------------

pdf.set_draw_color(255, 255, 255)

pdf.set_font("Helvetica", "B", 7)

# Sitz der Gesellschaft
pdf.set_xy(29, 253)
pdf.cell(45, 4, "Sitz der Gesellschaft")

pdf.set_font("Helvetica", "", 7)
pdf.set_xy(29, 257)
pdf.multi_cell(
    45,
    3.5,
    "Schöne Aussicht 1\n"
    "60314 Frankfurt"
)

# Bankverbindung
pdf.set_font("Helvetica", "B", 7)
pdf.set_xy(76, 253)
pdf.cell(55, 4, "Bankverbindung")

pdf.set_font("Helvetica", "", 7)
pdf.set_xy(76, 257)
pdf.multi_cell(
    55,
    3.5,
    "Frankfurter Sparkasse\n"
    "BIC: HELADEF1822\n"
    "IBAN: DE17 5005 0201 0000 0123 45"
)

# Geschäftsführer
pdf.set_font("Helvetica", "B", 7)
pdf.set_xy(130, 253)
pdf.cell(40, 4, "Geschäftsführer")

pdf.set_font("Helvetica", "", 7)
pdf.set_xy(130, 257)
pdf.multi_cell(
    40,
    3.5,
    "Verena Luzern\n"
    "Dr. Roxanne Byte"
)

# Amtsgericht
pdf.set_font("Helvetica", "B", 7)
pdf.set_xy(170, 253)
pdf.cell(30, 4, "Amtsgericht")

pdf.set_font("Helvetica", "", 7)
pdf.set_xy(170, 257)
pdf.multi_cell(
    30,
    3.5,
    "Frankfurt\n"
    "HRB 987654"
)

# USt-ID
pdf.set_font("Helvetica", "B", 7)
pdf.set_xy(201, 253)
pdf.cell(20, 4, "UST-Id")

pdf.set_font("Helvetica", "", 7)
pdf.set_xy(201, 257)
pdf.cell(25, 4, "DE12345678")

# ------------------------------------------------------------
# Ausgabe
# ------------------------------------------------------------

pdf.output("rechnung.pdf")