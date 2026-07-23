


sitzplan = [
    ["Anna", "Albert", "Cem", "Diana", "Elif"],
    ["Felix", "Greta", "Hassan", "Isabel", "Jonas"],
    ["Kaan", "Lena", "Mert", "Nina", "Oskar"],
    ["Paul", "Quentin", "Rita", "Sofia", "Tom"]
]

# Finde alle Schüler, deren Name mit "A" beginnt.
namen_mit_a = []
for reihe in sitzplan:
    for platz in reihe:
        if platz.startswith("A"):
            namen_mit_a.append(platz)


print(namen_mit_a)