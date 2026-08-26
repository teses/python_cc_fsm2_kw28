

from abc import ABC, abstractmethod

class Besucher(ABC):

    @abstractmethod
    def isExpressEingang(self, isWerktag: bool) -> bool:
        pass

    @abstractmethod
    def calculatePreis(self, basisPreis: float) -> float:
        pass

    # factory
    @staticmethod
    def createBesucher(typ: str):
        if(typ=="STANDARD"):
            return StandardBesucher()
        elif(typ=="PREMIUM"):
            return PremiumBesucher()
        elif(typ=="VIP"):
            return VIPBesucher()


class StandardBesucher(Besucher):

    def isExpressEingang(self, isWerktag: bool) -> bool:
        return False

    def calculatePreis(self, basisPreis: float) -> float:
        return basisPreis

class PremiumBesucher(Besucher):

    def isExpressEingang(self, isWerktag: bool) -> bool:
        return isWerktag

    def calculatePreis(self, basisPreis) -> float:
        return round(basisPreis * 0.95, 2)


class VIPBesucher(Besucher):

    def isExpressEingang(self, isWerktag: bool) -> bool:
        return True

    def calculatePreis(self, basisPreis: float) -> float:
        return  round(basisPreis * 0.90, 2)



# alte implementierung
# b1 = Besucher("STANDARD")
# b2 = Besucher("PREMIUM")
# b3 = Besucher("VIP")

# neue implementierung ohne Factory
# b1 = StandardBesucher()
# b2 = PremiumBesucher()
# b3 = VIPBesucher()

# implementierung mit factory
typ = "PREMIUM"
b1 = Besucher.createBesucher(typ)
b2 = Besucher.createBesucher("STANDARD")
b3 = Besucher.createBesucher("VIP")


print(b1.isExpressEingang(True))   # False
print(b2.isExpressEingang(True))   # True
print(b2.isExpressEingang(False))  # False
print(b3.isExpressEingang(False))  # True


print(b1.calculatePreis(100))      # 100.0
print(b2.calculatePreis(100))      # 95.0
print(b3.calculatePreis(100))      # 90.0


