"""
    Einfache Datentypen
    Python ist nicht typisiert.
    skalare Datentypen sind intern aber als Objekt abgebildet


"""
##########################################################################
#  Datentypen
##########################################################################
# Dynamisch typisiert:
testNumber = 5       # int
testDecimal = 3.5    # float
testString = "123"   # str
testBool = True      # bool (True, False)
testNone = None      # None

print("testNumber", testNumber, type(testNumber))
print("testDecimal", testDecimal, type(testDecimal))
print("testString", testString, type(testString))
print("testBool", testBool, type(testBool))
print("testNone", testNone, type(testNone))

# Mit einfache Typisierung
testNumber: int = 5       # int
testDecimal: float = 3.5    # float
testString: str = "123"   # str
testBool: bool = True      # bool (True, False)
testNone: None = None      # None


##########################################################################
#  Benennung von Variablen
##########################################################################
# nicht gut
mengederdateien = 20
menGeDerdaTeien = 30

# Camel Case - gut
mengeDerDateien = 30

# Pascal Case - Gut
MengeDerDateien = 20

# snake Case - gut
menge_der_dateien = 20

# am besten nur folgende zeichen verwenden [a-z, A-Z, 0-9, _]
du_bist_ein_wert = "hallo"
zahl22 = 100

# nicht erlaubt sind zahlen am Anfang
# 1hallo = "hallo"  # geht nicht

# Abkürzungen sparsam einsetzen
data_str = "Hallo"
articleDescr = "Beschreibung"

# standartabkürzungen
i = 0

# Python ist case sensitiv!!
VariableA = "Hallo"
variableA = "Welt"
print(VariableA)
print(variableA)

