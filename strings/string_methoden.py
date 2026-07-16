##############################################
# String Manipulation
##############################################
meinString = "    hello mein, World!-------"
# meinString = " Motorradhelme  "
# meinString = "Heinz Ketchup"
# meinString = "Hein Ketchup"
# meinString = "Vance &amp; Hince"
# meinString = "ITEMNUMBER"

# Methoden zum manipulieren
print(meinString.upper()) # großschreiben
print(meinString.lower()) # kleinschreiben
print(meinString.capitalize()) #  ersten Buchstaben groß
print(meinString.title()) # jeden ersten Buchstaben groß

# strip() - Trim von beiden Seiten
# lstrip() - Trim von links
# rstrip() - Trim von rechts


print(meinString.strip()) # entfernt leerzeichen vorne und hinten
print(meinString.strip("-")) # entfernt bindestriche vorne und hinten
print(meinString.strip().strip("-"))

# replace()
print(meinString.replace("World", "Mars"))

print(meinString.center(100, "#"))

##############################################
# String zerlegen - split
##############################################
zeichenkette = "Apfel,Birne,Banane"
zeichenketteAlsArray = zeichenkette.split(",")
print(zeichenketteAlsArray, type(zeichenketteAlsArray))


#############################################
# Prüffunktionen
##############################################
print(meinString.find("l")) # findet die position des ersten vorkommen eines zeichens

#
space = " " # schauen ob es ein leerzeichen ist
print(space.isspace())

##
datei = "bild.jpg"
print(datei.startswith("bild"))   # True
print(datei.endswith(".jpg"))     # True


Test = "id_123"
print(Test, "isalnum",Test.isalnum())
print(Test,"isdecimal",Test.isdecimal())
print(Test,"isdigit", Test.isdigit())
print(Test,"isnumeric",Test.isnumeric())
print(Test,"isidentifier",Test.isidentifier())
print(Test,"isalpha",Test.isalpha())


