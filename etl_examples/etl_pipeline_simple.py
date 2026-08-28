"""
 Ein ETL Prozess - Dies nennen wir Pipeline

 E - Extrahieren
 T - Transformieren
 L - Laden
"""
import pandas as pd
from sqlalchemy import create_engine

################################################################################################
# Pandas ausgabe einstellen
################################################################################################
# pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", 100)
pd.set_option("display.width", None)
# pd.set_option("display.max_colwidth", None)

################################################################################################
# Einstellungen für das Script
################################################################################################
SOURCE_FILE = "../data/sales_varianz.csv"
TABLE_NAME = "sales_varianz"

################################################################################################
# Database Connection
################################################################################################
db_connection = create_engine(
    "mysql+pymysql://root:@localhost:3306/comcave_etl",
    echo=True
)

################################################################################################
# ETL-Funktionen
################################################################################################
# Daten einlesen
def extract() -> pd.DataFrame:
    print("extract wird aufgerufen")
    df = pd.read_csv(SOURCE_FILE)

    return df


# Daten werden bereinigt, geändert oder umgeformt
def transform(data: pd.DataFrame) -> pd.DataFrame:
    print("transform wird aufgerufen")

    # Spaltennamen cleanen
    data.columns = data.columns.str.lower()

    # Spaltennamen umbenennen
    data = data.rename(columns={"preis": "preis_netto"})

    # Spalten erzeugen
    data["preis_brutto"] = data["preis_netto"] * 1.19

    # Datumfelder konvertieren
    data["datum"] = pd.to_datetime(
        data["datum"],
        errors="coerce", # coerce macht ungültige Daten zu NaT.
        format="mixed",
        dayfirst=True
    )

    #print(data.dtypes)
    #print(data)
    #print(data.to_string())
    return data


# Daten in das Ziel laden
def load(data: pd.DataFrame):
    print("load wird aufgerufen")
    count = data.to_sql(
        TABLE_NAME,
        con=db_connection,
        if_exists="replace",  # replace , append
        index=False
    )
    print(f"importiert: {count}")


# Pipeline
def pipeline():
    data = extract()
    data = transform(data)
    load(data)

# start
pipeline()





