"""
    Datei mit der Testklasse
"""
import unittest
from testing.unittest_suit.functions import addiere

class TestFunctions(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(addiere(2, 3), 5)

