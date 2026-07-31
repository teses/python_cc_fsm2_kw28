


# MOdule

https://docs.python.org/3.14/library/sqlite3.html

```pip install pysqlite3```

# Struktur

projekt
├── datenbank.py                # Klasse für den Datenbankzugriff
├── service.py                  # Serviceklassen für die Datenschnittstelle
└── tests/
    └── test_service.py         # Integrationstest

# Tests ausführen

```
c:\Python\Python313\python.exe -m unittest discover -v -s "testing\unittest_selenium"
```