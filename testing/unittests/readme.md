# unittest

unittest ist das Standard-Testframework von Python. 

Es dient dazu, automatisch zu prüfen, ob Funktionen und Klassen korrekt arbeiten. 
Es basiert auf dem xUnit-Konzept (JUnit, NUnit usw.) und gehört zur Python-Standardbibliothek.

# Dokumentation 

https://docs.python.org/3/library/unittest.html

# Wichtige Assertions 

| Methode                   | Bedeutung                        |
|---------------------------|----------------------------------|
| `assertEqual(a, b)`       | Werte müssen gleich sein         |
| `assertNotEqual(a, b)`    | Werte dürfen nicht gleich sein   |
|---------------------------| -------------------------------  |
| `assertTrue(x)`           | Ausdruck muss True sein          |
| `assertFalse(x)`          | Ausdruck muss False sein         |
|---------------------------| -------------------------------- |
| `assertIs(a, b)`          | Dasselbe Objekt                  |
| `assertIsNot(a, b)`       | Nicht dasselbe Objekt            |
|---------------------------| -------------------------------- |
| `assertIsNone(x)`         | Muss None sein                   |
| `assertIsNotNone(x)`      | Muss nicht None sein             |
|---------------------------| -------------------------------- |
| `assertIn(a, liste)`      | Element enthalten                |
| `assertNotIn(a, liste)`   | Element nicht enthalten          |
|---------------------------| -------------------------------- |
| `assertGreater(a, b)`     | a > b                            |
| `assertLess(a, b)`        | a < b                            |
|---------------------------| -------------------------------- |
| `assertRaises(Exception)` | Ausnahme muss auftreten          |


# Test ausführen

## 1. in der IDE

in der IDE sollten die Tests direkt mit ein Play-Button aufrufbar sein.

## 2. `unittest` per Konsole starten mit `__main__`

wenn am Ende des Scriptes folgendes steht:

```
if __name__ == "__main__":
    unittest.main()
```

Dann wird der Test gestartet wenn man das Script auf der Konsole normal aufruft
```
python.exe scriptname_mit_tests.py
```

## 3. `unittest` per Konsole starten ohne `__main__`

Jetzt gibt es den main Bereich nicht am Ende des Scriptes.
Jetzt muss man python sagen das er das `unittest` Modul benutzen soll.

```
python.exe -m unittest scriptname_mit_tests.py
```

# Die Testausgabe etwas ausführlicher machen

`-v` für verbose

```
python.exe -m unittest -v scriptname_mit_tests.py
```

# Testsuite

Hirachie

```TestSuite -> TestKlasse -> TestMethode```















