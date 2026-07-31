import unittest


class TestMathematik(unittest.TestCase):
    """Test-Klasse für mathematische Funktionen"""

    @classmethod
    def setUpClass(cls):
        print("Einmal vor allen Tests")
        cls.test_zahlen = [1, 2, 3, 4, 5]
        cls.leere_liste = []

    def test_listen_operationen(self):
        """Test von Listen-Operationen"""
        self.assertIn(3, self.test_zahlen)
        self.assertNotIn(10, self.test_zahlen)


    def test_listen_operationen2(self):
        """Test von Listen-Operationen"""
        self.assertFalse(len(self.leere_liste) > 0)
        self.assertTrue(len(self.test_zahlen) == 5)

if __name__ == "__main__":
    unittest.main()