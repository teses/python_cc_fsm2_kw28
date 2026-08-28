"""

https://peps.python.org/pep-0282/

Module

pip install mysql-connector-python


Tabelle

CREATE TABLE logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    log_level VARCHAR(20) NOT NULL,
    logger_name VARCHAR(100),
    message TEXT,
    created_at DATETIME NOT NULL
);


"""

import logging
import time
import mysql.connector

#############################################################
# Eigene MySQL Handler Klasse



class MySQLHandler(logging.Handler):

    def __init__(self, host, database, user, password):
        super().__init__()
        self.connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        self.cursor = self.connection.cursor()


    def emit(self, record):
        try:
            sql = """
                    INSERT INTO logs
                        (log_level, logger_name, message, created_at)
                    VALUES
                        (%s, %s, %s, NOW())
                """

            values = (
                record.levelname,
                record.name,
                record.getMessage()
            )

            self.cursor.execute(sql, values)
            self.connection.commit()

        except Exception:
            self.handleError(record)




    def close(self):
        if self.cursor:
            self.cursor.close()

        if self.connection:
            self.connection.close()

        super().close()






#############################################################
# Logger
logging.basicConfig(
    level    = logging.INFO,
    format   = "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers = [
        MySQLHandler(user="root", password="", host="127.0.0.1", database="comcave_etl"),
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