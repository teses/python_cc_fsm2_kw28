# Logging-Konzept

- den Ablauf des Programms nachvollziehbar machen
- Fehler und Exceptions dokumentieren
- wichtige Verarbeitungsschritte protokollieren
- bei der Fehlersuche unterstützen
- Informationen über die Anzahl verarbeiteter Datensätze liefern
- keine sensiblen Daten wie Passwörter oder Tokens speichern!!

# Log-Level

DEBUG
  ↓
INFO
  ↓
WARNING
  ↓
ERROR
  ↓
CRITICAL


| Level      | Verwendung                                                 | Beispiel                                    |
| ---------- | ---------------------------------------------------------- | ------------------------------------------- |
| `DEBUG`    | Detaillierte Informationen zur Entwicklung                 | SQL-Abfrage, einzelne Verarbeitungsschritte |
| `INFO`     | Normale Programminformationen                              | „1000 Datensätze eingelesen“                |
| `WARNING`  | Unerwartete Situation, Programm läuft weiter               | „5 Datensätze ohne Preis“                   |
| `ERROR`    | Fehler bei einer Verarbeitung                              | „CSV-Datei konnte nicht gelesen werden“     |
| `CRITICAL` | Schwerwiegender Fehler, Programm kann nicht weiterarbeiten | „Datenbankverbindung fehlgeschlagen“        |

# Logging Modul

Logging nach PEP282

https://peps.python.org/pep-0282/

# Installation

```pip install logging```  

----

# Klassenstruktur - UML

```mermaid
classDiagram

class Logger {
    +setLevel(level)
    +addHandler(handler)
    +debug(message)
    +info(message)
    +warning(message)
    +error(message)
    +critical(message)
}

class Record {
    +levelname
    +name
    +getMessage()
}


class Handler {
    +setFormatter(Formatter)
}
 
class Formatter {
    +format(record)
}

class MySQLHandler {
    +emit(record)
}

class StreamHandler {
    +emit(record)
}

class FileHandler {
    +emit(record)
}

Handler <|-- StreamHandler
Handler <|-- MySQLHandler
StreamHandler <|-- FileHandler 

Logger o-- Handler
Handler o-- Formatter 

```