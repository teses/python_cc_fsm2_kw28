"""
    Datei mit der Business Klasse - Funktionaler Code
"""

class Rechner:
    """Einfache Rechner-Klasse für Tests"""
    def __init__(self):
        self.history = []

    def addieren(self, a, b):
        ergebnis = a + b
        self.history.append(f"{a} + {b} = {ergebnis}")
        return ergebnis

    def dividieren(self, a, b):
        if b == 0:
            raise ValueError("Division durch Null")
        ergebnis = a / b
        self.history.append(f"{a} / {b} = {ergebnis}")
        return ergebnis


