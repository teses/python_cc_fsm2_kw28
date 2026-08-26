

class Besucher:
    def __init__(self, typ: str):
        self.typ = typ

    def isExpressEingang(self, isWerktag: bool) -> bool:
        if self.typ == "STANDARD":
            return False
        elif self.typ == "PREMIUM":
            return isWerktag
        elif self.typ == "VIP":
            return True
        elif self.typ == "KINDER":
            return True
        else:
            raise ValueError(f"Unbekannter Besuchertyp: {self.typ}")

    def calculatePreis(self, basisPreis: float) -> float:
        if self.typ == "STANDARD":
            return basisPreis
        elif self.typ == "PREMIUM":
            return basisPreis * 0.95
        elif self.typ == "VIP":
            return basisPreis * 0.9
        else:
            raise ValueError(f"Unbekannter Besuchertyp: {self.typ}")





# Beispiel:
b1 = Besucher("STANDARD")
print(b1.isExpressEingang(True))

b2 = Besucher("PREMIUM")
print(b2.isExpressEingang(False))

b3 = Besucher("VIP")
print(b3.isExpressEingang(True))

############
b1 = Besucher("STANDARD")
print(b1.calculatePreis(100))

b2 = Besucher("PREMIUM")
print(b2.calculatePreis(100))

b3 = Besucher("VIP")
print(b3.calculatePreis(100))




# print(besucher.calculatePreis(100.0))  # Gibt 95.0 aus