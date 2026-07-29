import unittest
from testing.unittests.lesson3.rechner import Rechner

class TestRechner(unittest.TestCase):

    def setUp(self):
        self.rechner = Rechner()

    def test_addieren(self):
        ergebnis = self.rechner.addieren(1, 2)
        self.assertEqual(ergebnis, 3)

    def test_addieren2(self):
        ergebnis = self.rechner.addieren(1.5, 2.3)
        self.assertEqual(ergebnis, 3.8)

    def test_addieren3(self):
        ergebnis = self.rechner.addieren(1.55555, 2.33333)
        self.assertAlmostEqual(ergebnis, 3.88888, places=5)

    def test_datatypes(self):
        ergebnis = self.rechner.addieren(2, 3)
        self.assertEqual(ergebnis, 5)
        self.assertEqual(str(type(ergebnis)), "<class 'int'>")

        ergebnis2 = self.rechner.addieren(3.3, 7.8)
        self.assertEqual(ergebnis2, 11.1)
        self.assertEqual(str(type(ergebnis2)), "<class 'float'>")

    def test_addieren_history(self):
        rechner = Rechner()

        ergebnis = rechner.addieren(2, 3)
        ergebnis2 = rechner.addieren(3.3, 7.8)

        # länge testen der history
        self.assertEqual(len(rechner.history), 2)

        self.assertIn("2 + 3 = 5", rechner.history)
        self.assertIn("3.3 + 7.8 = 11.1", rechner.history)


