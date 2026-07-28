import random


woerter = [
    "python",
    "computer",
    "programmieren",
    "variable",
    "schleife",
    "funktion"
]

hangman_bilder = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]


gesuchtes_wort = random.choice(woerter)

geratene_buchstaben = set()

fehler = 0
maximale_fehler = len(hangman_bilder) - 1


print("Willkommen bei Hangman!")
print("Errate das gesuchte Wort.")


while fehler < maximale_fehler:

    print(hangman_bilder[fehler])

    sichtbares_wort = ""

    for buchstabe in gesuchtes_wort:
        if buchstabe in geratene_buchstaben:
            sichtbares_wort += buchstabe + " "
        else:
            sichtbares_wort += "_ "

    print("Wort:", sichtbares_wort)
    print("Geratene Buchstaben:", sorted(geratene_buchstaben))
    print(f"Fehler: {fehler}/{maximale_fehler}")

    if "_" not in sichtbares_wort:
        print("\nGlückwunsch! Du hast das Wort erraten.")
        print("Das Wort war:", gesuchtes_wort)
        break

    eingabe = input("\nBitte einen Buchstaben eingeben: ").lower()

    if len(eingabe) != 1:
        print("Bitte genau einen Buchstaben eingeben.")
        continue

    if not eingabe.isalpha():
        print("Bitte nur einen Buchstaben eingeben.")
        continue

    if eingabe in geratene_buchstaben:
        print("Diesen Buchstaben hast du bereits ausprobiert.")
        continue

    geratene_buchstaben.add(eingabe)

    if eingabe in gesuchtes_wort:
        print("Richtig!")
    else:
        print("Leider falsch.")
        fehler += 1

else:
    print(hangman_bilder[fehler])
    print("\nDu hast leider verloren.")
    print("Das gesuchte Wort war:", gesuchtes_wort)