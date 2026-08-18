

class Radio:

    def __init__(self, ist_an, lautstaerke, frequenz):
        self.eingeschaltet = ist_an

        if 0 <= lautstaerke <= 10:
            self.lautstaerke = lautstaerke
        else:
            self.lautstaerke = 0

        if 85.0 <= frequenz <= 110.0:
            self.frequenz = frequenz
        else:
            self.frequenz = 99.9

        print("Radio wurde erstellt")


    def lauter(self):
        if self.eingeschaltet:
            if self.lautstaerke < 10:
                self.lautstaerke += 1
                print("Radio wird lauter")
            else:
                print("Maximale Lautstärke erreicht")
        else:
            print("Radio ist ausgeschaltet")


    def leiser(self):
        if self.eingeschaltet:
            if self.lautstaerke > 0:
                self.lautstaerke -= 1
                print("Radio wird leiser")
            else:
                print("Minimale Lautstärke erreicht")
        else:
            print("Radio ist ausgeschaltet")


    def an(self):
        self.eingeschaltet = True
        print("Radio wird eingeschaltet")


    def aus(self):
        self.eingeschaltet = False
        print("Radio wird ausgeschaltet")


    def waehleSender(self, frequenz):
        if 85.0 <= frequenz <= 110.0:
            self.frequenz = frequenz
            print("Sender wurde gewechselt")
        else:
            self.frequenz = 99.9
            print("Frequenz ungültig, Sender wurde auf 99.9 gesetzt")


    def __str__(self):
        if self.eingeschaltet:
            zustand = "an"
        else:
            zustand = "aus"

        return f"Radio {zustand}: Freq={self.frequenz}, Laut={self.lautstaerke}"

# Zum testen:


radio = Radio(ist_an=True, lautstaerke=9, frequenz=100.1)
radio.an()
radio.aus()

#radio.waehleSender(188.1)


print("-"*30, radio)




# radio = Radio(True, 2, 98.4)
#
# print(radio)
#
# radio.lauter()
# print(radio)
#
# radio.leiser()
#
# radio.waehleSender(105.5)
# print(radio)
#
# radio.aus()
# radio.lauter()
#
print(radio)