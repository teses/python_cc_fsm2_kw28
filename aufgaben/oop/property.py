"""
Aufgabe

Erstelle eine Klasse RechnungsPosition, die folgende Attribute hat:
    beschreibung (str) – was verkauft wird
    menge (int) – Anzahl der Artikel
    preis_netto (float) – Preis pro Stück ohne Steuer
    mwst_satz (float) – Mehrwertsteuersatz in Prozent

Implementiere berechnete Properties:
    gesamt_netto = menge * preis_netto
    steuerbetrag = gesamt_netto * (mwst_satz / 100)
    gesamt_brutto = gesamt_netto + steuerbetrag

Baue eine Validierung ein:
    menge muss > 0 sein
    preis_netto darf nicht negativ sein
    MwSt-Satz darf nicht negativ sein!

"""



# Erwartete Nutzung
# Beispiel: 3 Bücher à 12.50 €, 7 % MwSt.
pos = RechnungsPosition("Buch", 3, 12.50, 7)

# public properties
print(pos.beschreibung)   # "Buch"
print(pos.menge)
print(pos.preis_netto)
print(pos.mwst_satz)

# Fehlermeldung
#pos.menge = -1
#pos.preis_netto = -1
#pos.mwst_satz = -1

#  berechnete Properties
print(pos.gesamt_netto)   # 37.5
print(pos.steuerbetrag)   # 2.625
print(pos.gesamt_brutto)  # 40.125