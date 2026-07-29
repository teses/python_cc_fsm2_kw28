"""
    Unittest: Einfache Testklasse

"""

import unittest

# Die Testklasse muss von der Klasse unittest.TestCase erben
class TestLesson1(unittest.TestCase):


    # Die Testmethode muss mit test_* beginnen
    def test_case1(self):
        self.assertEqual(5, 5)

    def test_case2(self):
        self.assertEqual(5, 10) # Fehler

    def test_addition(self):
        """Test der Addition"""
        self.assertEqual(2 + 2, 4)
        self.assertEqual(10 + (-5), 5)
        self.assertEqual(0 + 0, 0)

    def test_division(self):
        """Test der Division"""
        self.assertEqual(10 / 2, 5)
        self.assertAlmostEqual(10 / 3, 3.333333, places=5) # eine stelle zu viel

        # Test für Exception
        with self.assertRaises(ZeroDivisionError):
            10 / 0


if __name__ == "__main__":
    unittest.main()


