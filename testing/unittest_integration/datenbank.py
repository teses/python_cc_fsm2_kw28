
import sqlite3



class Datenbank:

    def __init__(self, datei):
        self.conn = sqlite3.connect(datei)


    def erstelle_tabelle(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS kunden(
                id INTEGER PRIMARY KEY,
                name TEXT
            )
        """)
        self.conn.commit()

    
    def kunde_speichern(self, name):
        self.conn.execute(
            "INSERT INTO kunden(name) VALUES(?)",
            (name,)
        )
        self.conn.commit()

    def alle_kunden(self, order="name", sort="ASC"):
        cursor = self.conn.execute(f"SELECT name FROM kunden ORDER BY {order} {sort}")
        return [zeile[0] for zeile in cursor]


    def ein_kunde(self, id):
        cursor = self.conn.execute(
            "SELECT * FROM kunden WHERE id = ?",
            (id,)
        )
        return [zeile for zeile in cursor][0]
    
        
    def schließen(self):
        self.conn.close()

