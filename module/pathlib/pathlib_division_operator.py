
from pathlib import Path


# __file__ enthält den Speicherort dieser Python-Datei.
# Mit .resolve().parent erhalten wir den Ordner, in dem die Datei liegt.
PROGRAMM_ORDNER = Path(__file__).resolve().parent

# Alle weiteren Dateien werden in diesem Ordner gesucht oder gespeichert.
#HIGHSCORE_DATEI = PROGRAMM_ORDNER / "highscore.json"

HIGHSCORE_DATEI = Path(PROGRAMM_ORDNER).joinpath("highscore.json")

print(HIGHSCORE_DATEI)