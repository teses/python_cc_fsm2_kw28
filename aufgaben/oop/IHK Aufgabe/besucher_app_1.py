"""

    Bei dieser Lösung sind zwar die Methoden calculatePreis() und isExpressEingang() in jeder Klasse vorhanden.
    Sie sind aber laut Definition nicht korrekt Polymorph.

    Zudem ist es nicht so ideal, das der StandartBesucher nur "Besucher" heißt
    und die anderen Arten davon erben und die Methoden überschreiben.

    -> Nicht richtig aber auf den weg
"""

class Besucher:
    def calculatePreis(self, basisPreis: float) -> float:
        return basisPreis

    def isExpressEingang(self, isWerktag: bool) -> bool:
        return False

class StandardBesucher(Besucher):

    def isExpressEingang(self, isWerktag: bool) -> bool:
        return False

    def calculatePreis(self, basisPreis: float) -> float:
        return basisPreis

class PremiumBesucher(Besucher):
    def calculatePreis(self, basisPreis: float) -> float:
        return basisPreis * 0.95

    def isExpressEingang(self, isWerktag: bool) -> bool:
        return isWerktag

class VIPBesucher(Besucher):
    def calculatePreis(self, basisPreis: float) -> float:
        return basisPreis * 0.9

    def isExpressEingang(self, isWerktag: bool) -> bool:
        return True


# alte implementierung
# b1 = Besucher("STANDARD")
# b2 = Besucher("PREMIUM")
# b3 = Besucher("VIP")

# neue implementierung
b1 = StandardBesucher()
b2 = PremiumBesucher()
b3 = VIPBesucher()

# Tests
print(b1.isExpressEingang(True))   # False
print(b2.isExpressEingang(True))   # True
print(b2.isExpressEingang(False))  # False
print(b3.isExpressEingang(False))  # True


print(b1.calculatePreis(100))      # 100.0
print(b2.calculatePreis(100))      # 95.0
print(b3.calculatePreis(100))      # 90.0


