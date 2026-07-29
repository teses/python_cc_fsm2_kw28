
import unittest
from test_rechner import TestRechner
from test_functions import TestFunctions

# TestLoader erzeugen
loader = unittest.TestLoader()

# Suite erstellen
suite = unittest.TestSuite()

# Alle Tests der Klasse hinzufügen
suite.addTests(loader.loadTestsFromTestCase(TestRechner))
suite.addTests(loader.loadTestsFromTestCase(TestFunctions))


# Suite ausführen
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
