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