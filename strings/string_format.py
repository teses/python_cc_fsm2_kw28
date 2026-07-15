"""
format()

"""


vorname = "Max"
stadt = "Würzburg"
age = 49
satzmaske = "{name} wohnt in {city} und ist {alter} Jahre alt"
satzmaske = "{name} ist {alter} Jahre alt und wohnt in {city}"

ergebnis = satzmaske.format(
    name=vorname,
    city=stadt,
    alter=age
)
print(ergebnis)


# zuordnung nach nummer
satzmaske = "{0} wohnt in {1} und ist {2} Jahre alt"
ergebnis2 = satzmaske.format(vorname,stadt,age)
print(ergebnis2)

###########################################################
## rechtsbündig darstellen
zahlen = [100, 99, 4]
for zahl in zahlen:
    print(f"{zahl:>8.3f}") # f-string
    print("{zahl:>8.3f}".format(zahl=zahl)) # format()




