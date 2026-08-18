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


class Radio:
    """
    Eine Klasse zur Darstellung eines Radios.

    >>> radio = Radio()
    >>> radio.istAn
    False
    >>> radio.lautstaerke
    5
    >>> radio.frequenz
    99.9

    >>> radio.an()
    Radio eingeschaltet
    >>> radio.istAn
    True

    >>> radio.lauter()
    Radio wird lauter gestellt
    >>> radio.lautstaerke
    6

    >>> radio.lautstaerke = 10
    >>> radio.lauter()
    Radio kann nicht lauter werden

    >>> radio.lautstaerke=6
    >>> radio.leiser()
    Radio wird leiser gestellt
    >>> radio.lautstaerke
    5

    >>> radio.lautstaerke = 0
    >>> radio.leiser()
    Radio kann nicht leiser werden

    >>> radio.waehleSender(98.4)
    Sender auf 98.4 gestellt
    >>> radio.frequenz
    98.4

    >>> radio.waehleSender(85.0)
    Sender auf 85.0 gestellt
    >>> radio.frequenz
    85.0

    >>> radio.waehleSender(110.0)
    Sender auf 110.0 gestellt
    >>> radio.frequenz
    110.0

    >>> radio.waehleSender(120.0)
    Frequenz außerhalb des erlaubten Bereichs, Sender auf 99.9 gestellt
    >>> radio.frequenz
    99.9

    >>> radio.waehleSender(80.0)
    Frequenz außerhalb des erlaubten Bereichs, Sender auf 99.9 gestellt
    >>> radio.frequenz
    99.9

    >>> radio.aus()
    Radio ausgeschaltet
    >>> radio.istAn
    False


    """
    def __init__(self, istAn: bool = False, lautstaerke: int =5, frequenz: float=99.9):
        self.istAn=istAn
        self.lautstaerke=lautstaerke
        self.frequenz=frequenz


    def __str__(self):
        if self.istAn:
            zustand = "an"
        else:
            zustand = "aus"

        out = f"Radio {zustand}: Freq={self.frequenz}, Laut={self.lautstaerke}"

        return out

    def an(self):
        self.istAn = True
        print("Radio eingeschaltet")
        return

    def aus(self):
        self.istAn = False
        print("Radio ausgeschaltet")
        return

    def lauter(self):
        if(self.istAn):
            if(self.lautstaerke<10):
                self.lautstaerke +=1
                print("Radio wird lauter gestellt")
            else:
                print("Radio kann nicht lauter werden")
        else:
            print("Radio ist aus")
        return

    def leiser(self):
        if(self.istAn):
            if(self.lautstaerke>0):
                self.lautstaerke -=1
                print("Radio wird leiser gestellt")
            else:
                print("Radio kann nicht leiser werden")
            pass
        else:
            print("Radio ist aus")
        return

    def waehleSender(self,frequenz:float):
        if self.istAn:
            if (85.0 <= frequenz <= 110.0):
                self.frequenz = frequenz
                print(f"Sender auf {frequenz} gestellt")
            else:
                self.frequenz = 99.9
                print("Frequenz außerhalb des erlaubten Bereichs, Sender auf 99.9 gestellt")
        else:
            print("Radio ist aus")

# Implementierung

radio = Radio()
radio.an()
radio.aus()

radio.waehleSender(188.1)


print("-"*30, radio)




# print("===== TEST 1: Radio erstellen =====")
# radio = Radio()
# print(radio)
#
#
# print("===== TEST 2: Radio anschalten =====")
# radio.an()
# print(radio)
#
#
# print("===== TEST 3: Lauter =====")
# radio.lauter()
# print(radio)
# radio.lauter()
# print(radio)
#
#
# print("===== TEST 4: Lautstärke auf Maximum =====")
# radio.lautstaerke = 10
# radio.lauter()
# print(radio)
#
#
# print("===== TEST 5: Leiser =====")
# radio.leiser()
# print(radio)
#
#
# print("===== TEST 6: Lautstärke auf Minimum =====")
# radio.lautstaerke = 0
# radio.leiser()
# print(radio)
#
# print("===== TEST 7: Radio ausschalten =====")
# radio.aus()
# radio.lauter()
# radio.leiser()
# print(radio)
#
# print("===== TEST 8: Radio wieder anschalten =====")
# radio.an()
# print(radio)
#
# print("===== TEST 9: Sender wählen =====")
# radio.waehleSender(98.4)
# print(radio)
#
# print("===== TEST 10: Ungültige Frequenz =====")
# radio.waehleSender(120.0)
# print(radio)
#
# print("===== TEST 11: Grenzwerte Frequenz =====")
# radio.waehleSender(85.0)
# print(radio)
#
# radio.waehleSender(110.0)
# print(radio)
#
#
#
# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()