"""
    String slicing
    Strings werden intern als Objekt behandelt !!!!!!
    Eine Property ist der Wert der als Array hinterlegt ist
"""
string = "Hallo, Welt!"

# Direkter Zugriff über den Index
print(string[0])
print(string[7])

# direkter Zugriff negativ position von hinten
print(string[-2]) # der 2te von hinten


# substring -> slicing
print(string[0:6])
print(string[:6]) # wird vor den doppelpunkt die zahl weggelassen ist es wie eine 0
print(string[5:]) # slice zum ende

# negativ => range von hinten
print(string[-5:])
print(string[-5:-2])

# der dritte wert nach den : steht für die Schrittweite
print(string[::3])

# reverse String
bitfolge = "11110000"
print(bitfolge[::-1])

## was alles geht (-;
string = "ABCDEFGHIJ"
print(string[8:1:-2])