import json


file = "../../data/krankenkassen.json"

# Datei einlesen - alter nicht effizienter weg
def getDataFromJsonFileOld(file):
    fh = open(file, "r")
    content = fh.read()
    if content != "" :
        data = json.loads(content) # in dictionary
    else :
        data = []
    fh.close()
    return data

# Datei einlesen - sauberer weg
def getDataFromJsonFile(file):
    with open(file, "r", encoding="utf-8") as datei:
        return json.load(datei)


krankenkassen = getDataFromJsonFile(file)
print(krankenkassen)


print(krankenkassen["features"][0]["properties"]["bezeichnung"])

# alle krankenkassen
for kk in krankenkassen["features"]:
    print(f"{kk['properties']['bezeichnung']}, {kk['properties']['strasse_name']}, {kk['properties']['postleitzahl']} {kk['properties']['kreis_name']}")




