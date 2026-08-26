"""
Aufgabe

Erstelle eine Klasse BankKonto, die folgende Attribute und Methoden hat:

Attribute:
    kontoinhaber → der Name des Kontoinhabers (z. B. "Anna").
    _kontostand → speichert den Kontostand (z. B. 1000).
    __pin → speichert die Geheimzahl.

Methoden:
    zeige_kontoinfos() → gibt Name und Kontostand aus.
    __pruefe_pin(pin) → private Methode, die prüft, ob ein PIN korrekt ist.
    abheben(betrag, pin) → hebt Geld ab, aber nur wenn der PIN stimmt und genug Geld da ist.

Hinweis:
Die Methoden sollen immer ausgeben was sie tun.
Fehlermeldungen mit print() ausgeben
"""

class BankKonto:
    def __init__(self, inhaber, kontostand, pin):
        self.kontoinhaber = inhaber     # public
        self._kontostand = kontostand   # protected
        self.__pin = pin                # private

    def zeige_kontoinfos(self):
        print(f"Inhaber: {self.kontoinhaber}, Kontostand: {self._kontostand} €")

    def __pruefe_pin(self, pin):
        ist_korrekt = pin == self.__pin
        if ist_korrekt:
            print("PIN korrekt.")
        else:
            print("PIN falsch.")
        return ist_korrekt

    def abheben(self, betrag, pin):
        if not self.__pruefe_pin(pin):
            print("Falscher PIN!")
            return
        if betrag > self._kontostand:
            print("Nicht genug Guthaben!")
            return
        self._kontostand -= betrag
        print(f"{betrag} € abgehoben. Neuer Kontostand: {self._kontostand} €")


#############################################################################
# --- Test ---
konto = BankKonto("Anna", 1000, 1234)

# Public Zugriff
print(konto.kontoinhaber)   # geht

# Protected Zugriff (geht, aber sollte man vermeiden)
print(konto._kontostand)

# Private Zugriff (Fehler!)
# print(konto.__pin)

# Zugriff über Namens-Mangling (geht, aber nicht empfohlen)
print(konto._BankKonto__pin)

# Methoden testen
konto.zeige_kontoinfos()
konto.abheben(200, 1111)  # falscher PIN
konto.abheben(200, 1234)  # klappt

