import unittest


class TestBeispiel(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print("Einmal vor allen Tests")

    @classmethod
    def tearDownClass(self):
        print("Verbindung schließen")

    def setUp(self):
        print("Vor jedem Test")

    def tearDown(self):
        print("Nach jedem Test")

    def test1(self):
        print("test1()")
        self.assertTrue(True)

    def test2(self):
        print("test2()")
        self.assertEqual(3, 3)
