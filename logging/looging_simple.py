"""

https://peps.python.org/pep-0282/

"""

import logging
import time

#
logger = logging.getLogger("app")
logger.setLevel(logging.ERROR)  # DEBUG, INFO, WARNING, ERROR, CRITICAL
formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

# konsolen log
consoleLogger = logging.StreamHandler()
consoleLogger.setFormatter(formatter)
logger.addHandler(consoleLogger)

# Datei log
fileLogger = logging.FileHandler("logfile.log.txt", encoding="utf-8")
fileLogger.setFormatter(formatter)
logger.addHandler(fileLogger)

#############################################################

logger.debug("Hallo ich bin eine debug meldung")
time.sleep(0.5)
logger.info("CSV-Datei wird eingelesen")
time.sleep(0.5)
logger.warning("Datensatz ohne Preis gefunden")
time.sleep(0.5)
logger.error("Fehler beim Schreiben in die Datenbank")
time.sleep(0.5)
logger.info("ETL-Prozess erfolgreich beendet")
time.sleep(0.5)
logger.critical("Absoluter Abbruch")

