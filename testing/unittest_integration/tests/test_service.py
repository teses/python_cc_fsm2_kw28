
# cd "D:\OneDrive\Kurse\COMCAVE\COMCAVE - 2026KW28 - FSM 2\Teilnehmer\python_cc_fsm2_kw28"
# .venv\Scripts\activate
# .venv\Scripts\python.exe -m unittest "testing\unittest_integration\tests\test_service.py"


 
import unittest
import os
import time
from testing.unittest_integration.datenbank import Datenbank
from testing.unittest_integration.services import KundenService


class TestKundenService(unittest.TestCase):


    def setUp(self):
        self.db_datei = r"data/test.db"

        self.db = Datenbank(self.db_datei)
        self.db.erstelle_tabelle()

        self.service = KundenService(self.db)
        #time.sleep(5)


    def tearDown(self):
        self.db.schließen()

        if os.path.exists(self.db_datei):
            os.remove(self.db_datei)


    # -----------------------------
    # Datenbank zu Beginn leer
    # -----------------------------
    def test_datenbank_ist_anfangs_leer(self):
        kunden = self.service.kunden_liste()
        self.assertEqual(kunden, [])

    # -----------------------------
    # Einen Kunden speichern
    # -----------------------------
    def test_einen_kunden_anlegen(self):
        self.service.neuer_kunde("Thomas")

        kunden = self.service.kunden_liste()

        self.assertEqual(kunden, ["Thomas"])


    # -----------------------------
    # Mehrere Kunden speichern
    # -----------------------------
    def test_mehrere_kunden_anlegen(self):
        self.service.neuer_kunde("Anna")
        self.service.neuer_kunde("Peter")
        self.service.neuer_kunde("Thomas")

        kunden = self.service.kunden_liste()

        self.assertEqual(
            kunden,
            ["Anna","Peter","Thomas" ]
        )


    # -----------------------------
    # Doppelte Namen zulassen
    # -----------------------------
    def test_doppelte_namen(self):
        self.service.neuer_kunde("Thomas")
        self.service.neuer_kunde("Thomas")

        kunden = self.service.kunden_liste()

        self.assertEqual(
            kunden,
            ["Thomas", "Thomas"]
        )

    # -----------------------------
    # Sonderzeichen
    # -----------------------------
    def test_sonderzeichen(self):
        self.service.neuer_kunde("Müller")
        self.service.neuer_kunde("Jörg")
        self.service.neuer_kunde("李小龙")

        kunden = self.service.kunden_liste()

        self.assertEqual(
            kunden,
            ["Jörg", "Müller", "李小龙"]
        )

    # -----------------------------
    # Leeren Namen speichern
    # -----------------------------
    def test_leerer_name(self):
        self.service.neuer_kunde("")

        kunden = self.service.kunden_liste()

        self.assertEqual(kunden, [""])


    # -----------------------------
    # Sehr langer Name
    # -----------------------------
    def test_langer_name(self):
        name = "A" * 500

        self.service.neuer_kunde(name)

        kunden = self.service.kunden_liste()

        self.assertEqual(kunden[0], name)


     # -----------------------------
    # Anzahl prüfen
    # -----------------------------
    def test_anzahl_kunden(self):
        self.service.neuer_kunde("Thomas")
        self.service.neuer_kunde("Anna")

        kunden = self.service.kunden_liste()

        self.assertEqual(len(kunden), 2)


     # -----------------------------
    # Reihenfolge prüfen
    # -----------------------------
    def test_reihenfolge(self):
        namen = [
            "Anna",
            "Peter",
            "Sabine",
            "Thomas",
        ]

        for name in namen:
            self.service.neuer_kunde(name)

        self.assertListEqual(
            self.service.kunden_liste(),
            namen
        )