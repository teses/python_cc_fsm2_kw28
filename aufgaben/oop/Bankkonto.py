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

    def __init__(self, kontoinhaber: str, kontostand: float, pin: str):
        self.kontoinhaber = kontoinhaber  # öffentlich
        self._kontostand = kontostand  # geschützt (protected)
        self.__pin = pin  # privat (private)

    def zeige_kontoinfos(self):
        print(f"Konto von {self.kontoinhaber} | Kontostand: {self._kontostand} €")

    def __pruefe_pin(self, pin: str) -> bool:
        return self.__pin == pin

    def abheben(self, betrag: float, pin: str):
        # PIN-Prüfung(private)
        if not self.__pruefe_pin(pin):
            print("Fehler: Falsche PIN! Abhebung abgebrochen.")
            return

        # Prüfung, ob genug Geld vorhanden ist
        if betrag > self._kontostand:
            print(f"Fehler: Unzureichender Kontostand! (Angefordert: {betrag} €, Verfügbar: {self._kontostand} €)")
            return

        # Abhebung
        self._kontostand -= betrag
        print(f"Erfolgreich {betrag} € abgehoben. Neuer Kontostand: {self._kontostand} €")


# Testcode
if __name__ == "__main__":
    # Konto erstellen
    konto = BankKonto("Anna", 1000, "1234")

    # Informationen anzeigen
    konto.zeige_kontoinfos()

    # Versuch 1: Falscher PIN
    konto.abheben(100, "0000")

    # Versuch 2: Zu viel Geld abheben
    konto.abheben(1500, "1234")

    # Versuch 3: Erfolgreiche Abhebung
    konto.abheben(200, "1234")

    # Kontostand nach Abhebung prüfen
    konto.zeige_kontoinfos()