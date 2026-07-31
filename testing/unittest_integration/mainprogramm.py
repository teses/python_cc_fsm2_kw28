

from datenbank import Datenbank


####  Test 
dbfile =  r"data/sqlite_testdb.db"
db = Datenbank(dbfile)
db.erstelle_tabelle()

# neuer Kunde
db.kunde_speichern("Thomas")

# 
res = db.alle_kunden()
print(res)

# 
db.schließen()