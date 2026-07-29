"""
    assert ist eine Anweisung in Python, mit der überprüft wird, ob eine Bedingung wahr ist.

    Ist die Bedingung False, wird eine AssertionError-Ausnahme ausgelöst.

    assert ist eine Überprüfungsfunktion
    Wenn Wahr => passiert nichts
    Wenn Falsch => passiert ein AssertionError (Fehlermeldung) Programm stürzt ab

    Daher niemals für Validierung von Benutzereingaben benutzen!!!
"""

# assert  1 + 1 == 4


#assert  1 + 1 == 3, "Meine Eigene Meldung"


erg = 1 + 1 == 3
print(erg)
assert erg

