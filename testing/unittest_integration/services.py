

from datenbank import Datenbank


class KundenService:

    def __init__(self, db):
        self.db = db


    def neuer_kunde(self, name):
        self.db.kunde_speichern(name)


    def kunden_liste(self):
        return self.db.alle_kunden()


    def kunden_details(self, id):
        return self.db.ein_kunde(id)