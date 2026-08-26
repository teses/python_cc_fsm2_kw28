"""
    Dies ist eine bessere Lösung, weil es einen abstrakten Besucher gibt, der durch Abstrakte Methoden
    die Implementierung in den Unterklassen erzwingt.

    So wird Polymorphy korrekt umgesetzt

"""

from abc import ABC, abstractmethod

class Besucher(ABC):

    @abstractmethod
    def isExpressEingang(self, isWerktag: bool) -> bool:
        pass

    @abstractmethod
    def calculatePreis(self, basisPreis: float) -> float:
        pass


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