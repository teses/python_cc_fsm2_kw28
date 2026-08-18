"""

Implementieren Sie eine Klasse Radio mit folgenden Attributen:

- eingeschaltet, wenn ein Radio an oder aus ist.
- lautstaerke, wie laut spielt das Radio Musik? (Die Lautstärke soll nur im Bereich von 0 bis 10 liegen.)
- frequenz, die die Frequenz des gewählten Senders angibt (Erlaubter Frequenzbereich ist zwischen 85.0 und 110.0).

Klasse
- Radio()

Konstruktor
- __init__(bool istAn, int lautstaerke, float frequenz)

Zu der Klasse Radio sollen folgende Methoden implementiert werden:

- lauter(), leiser(): Diese Methoden sollen die Lautstärke ändern (nur möglich im Zustand an).
- an(), aus(): Diese Methoden sollen den Zustand des Attributs eingeschaltet ändern.
- __str__() Diese Methode soll Informationen über den internen Zustand als String zurückgeben. Es soll eine Zeichenkette der Form „Radio an: Freq=98.4, Laut=2“ zurückgeben.
- waehleSender(float frequenz) Diese Methode soll eine Frequenz speichern. Ist die gewählte Frequenz außerhalb der erlaubten Frequenzbereichs, so soll die Frequenz 99.9 gewählt werden.

Alle Methoden sollen mit print() ausgeben was sie machen



"""