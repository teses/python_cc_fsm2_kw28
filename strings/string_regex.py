"""

    re.findall()    # Alle Treffer als Liste
    re.search()     # einen Treffer
    re.fullmatch()  # Validierung
    re.sub()        # ersetzen

"""

import re

text = "Artikel A123 kostet 49 Euro und Artikel B456 kostet 99 Euro"
text = "Artikel A123 kostet 49 Euro und Artikel B456 kostet 99 euro"
text = "Artikel A123 kostet 49 Euro und Artikel B456 kostet 99 €"
text = "Artikel A123 kostet 49 Euro und Artikel B456 kostet 99 € und Artikel 123 kosten 10 Euro"

# Alle Zahlen extrahiert
print(re.findall(r"[0-9]+", text))

# Alle Artikelnummern nach dem Format
# Ein Großbuchstabe von A-Z gefolgt von ein oder mehreren Ziffern von 0-9
print(re.findall(r"[A-Z][0-9]+", text))

# die preise extrahieren
print(re.findall(r" ([0-9]+)", text))
# das muster ist besser und sicherer
erg = re.findall(r"(\d+)\s+(Euro|euro|€|EUR)", text)
print([x[0] for x in erg])  # mit list comprehesions in einer zeile möglich
