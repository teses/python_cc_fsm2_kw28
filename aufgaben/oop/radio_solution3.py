class Radio:

    def __init__(self, istAn=False, lautstaerke=5, frequenz=99.9):
        self.eingeschaltet = istAn
        self.lautstaerke = lautstaerke
        self.frequenz = frequenz


    @property
    def frequenz(self):
        return self.__frequenz


    @frequenz.setter
    def frequenz(self, frequenz):
        if 85.0 <= frequenz <= 110.0:
            self.__frequenz = frequenz
        else:
            self.__frequenz = 99.9
            raise ValueError(f"Ungültige Frequenz {frequenz}, setze auf 99.9")


    @property
    def lautstaerke(self):
        return self.__lautstaerke

    @lautstaerke.setter
    def lautstaerke(self, lautstaerke):
        if 0 <= lautstaerke <= 10:
            self.__lautstaerke = lautstaerke
        else:
            self.__lautstaerke = 5
            raise ValueError(f"Ungültige Lautstärke {lautstaerke}, setze auf 5")




    def an(self):
        self.eingeschaltet = True
        print("Radio eingeschaltet")


    def aus(self):
        self.eingeschaltet = False
        print("Radio ausgeschaltet")


    def lauter(self):
        if self.eingeschaltet:
            if self.lautstaerke < 10:
                self.lautstaerke += 1
                print(f"Lautstärke erhöht: {self.lautstaerke}")
            else:
                print("Maximale Lautstärke erreicht!")
        else:
            print("Radio ist aus, Lautstärke nicht veränderbar.")


    def leiser(self):
        if self.eingeschaltet:
            if self.lautstaerke > 0:
                self.lautstaerke -= 1
                print(f"Lautstärke verringert: {self.lautstaerke}")
            else:
                print("Minimale Lautstärke erreicht!")
        else:
            print("Radio ist aus, Lautstärke nicht veränderbar.")


    def waehleSender(self, frequenz):
        if 85.0 <= frequenz <= 110.0:
            self.frequenz = frequenz
            print(f"Sender gewählt: {self.frequenz} MHz")
        else:
            self.frequenz = 99.9
            print(f"Ungültige Frequenz, setze auf Standard 99.9 MHz")


    def __str__(self):
        zustand = "an" if self.eingeschaltet else "aus"
        return f"Radio {zustand}: Freq={self.frequenz}, Laut={self.lautstaerke}"




radio = Radio(istAn=True, lautstaerke=9, frequenz=180.1)

