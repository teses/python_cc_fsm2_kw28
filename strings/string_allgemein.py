"""
    Strings - Eines der wichtigsten

    String Manipulation
    Da die Variablen im Hintergrund objekte sind gibt es viele eingebaute Methoden.

"""
# String Verkettung (Konkatenation) concatenation
meinText1 = "Hallo"
meinText2 = "Welt"

print(meinText1 + " " + meinText2)

"""
    Escaping - Maskierung
    Escape Zeichen \
    
    Problem:
        Hans sagt: "Hallo"
    
    unser Problem liegt in XML/HTML
        <a href="http://www...">Link</a>
    
    
    \t \r \n - ASCI-Steuerzeichen   \r\n - Eselsbrücke "return"
"""

satz = "Hans sagt: \"Hallo\""
print(satz)

satz = "mit einfachen 'Hallo'"
print(satz)

test = 'Hallo ein Satz: "einfach" weiter'
print(test)

test = 'Hallo ein Satz: \'einfach\' weiter'
print(test)

test = "\"hallo ein satz\" weil 'der ist einfach'"
print(test)

# Wenn in der Variable doppelte Anführungsstriche vorkommen
# lohnt es sich den String in einfache Anführungsstriche zu packen
html = '<a href="http://www...">Link</a>'



# achtung hier
pfad = "c:\windows\tmp"
print(pfad)
# Lösung
pfad = "c:\\windows\\tmp"
print(pfad)

# Bessere Lösung raw string
pfad = r"c:\windows\tmp"
print(pfad)


##############################################################################
## Mit Steuerzeichen
# Zeilenumbruch
mehrzeilen = "Hallo\r\nWelt"
print("mehrzeilen", mehrzeilen)

# Tabulator
variable = "Max sagt:\tTest"
print(variable)

# bitte vermeiden
gedicht = '''Rosen sind rot,
Veilchen sind blau,
Python macht Spaß,
das weißt du genau!'''
print(gedicht)

gedicht = """
    Ein mehrzeiliger Kommentar
    Dieser kann mehrere Zeilen haben
"""
print(gedicht)
