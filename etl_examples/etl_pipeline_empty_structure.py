"""
 Ein ETL Prozess - Dies nennen wir Pipeline

 E - Extrahieren
 T - Transformieren
 L - Laden
"""
import pandas as pd

# Daten einlesen
def extract() -> pd.DataFrame:
    print("extract wird aufgerufen")


# Daten werden bereinigt, geändert oder umgeformt
def transform(data: pd.DataFrame) -> pd.DataFrame:
    print("transform wird aufgerufen")
    return data


# Daten in das Ziel laden
def load(data: pd.DataFrame):
    print("load wird aufgerufen")


def pipeline():
    data = extract()
    data = transform(data)
    load(data)


pipeline()





