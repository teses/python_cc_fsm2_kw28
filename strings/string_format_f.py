"""
    String formatierung mit dem f-Operator

    {variable:format}

"""


name = "Max"
city = "Würzburg"
alter = 49

# f-string
satzmaske = f"{name} wohnt in {city} und ist {alter} Jahre alt"

# negativbeispiel mit concatenation
#satzmaske = str(name) + " wohnt in "+str(city)+" und ist "+str(alter)+" Jahre alt"
print(satzmaske)

#
price = 9.99875
txt = f"The price is {price:.2f} dollars"
print(txt)

## rechtsbündig darstellen
zahlen = [100,99,4]
for zahl in zahlen:
    print(f"{zahl:>8.2f}" )

#
price = 100
tax = 0.19
print(f"{price + (price * tax)}")

# achtung nicht als zahlenformatierer verwenden und damit weiter rechnen
Zahl = 100
meine_neue_zahl = f"{Zahl:>8.2f}"
print(Zahl, meine_neue_zahl, type(meine_neue_zahl))

#
alter = 20
status = f"Du bist: {'Erwachsen' if alter >= 18 else 'Minderjährig'}   "
#status = "Erwachsen" if alter >= 18 else "Minderjährig"
print(status)
print(f"Status: {'Volljährig' if alter >= 18 else 'Minderjährig'}")

# dictionary
person = {"name": "John", "age": 19}
print(f"{person['name']} is {person['age']} years old.")


# mit methodenaufruf
string = "Hello this is my World"
print(f"{string.title()}")

