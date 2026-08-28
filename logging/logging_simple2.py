"""

https://peps.python.org/pep-0282/

"""

import logging
import time

#############################################################
# Logger
logging.basicConfig(
    level    = logging.INFO,
    format   = "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers = [
        logging.FileHandler("logfile1.log.txt", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('app')


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