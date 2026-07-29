"""

    Ein Python script bei dem der doctest runner automatisch aufgerufen wird,
    wenn das Script direkt gestartet wird

"""

def quadrat(x):
    """
    Berechnet das Quadrat einer Zahl.
    Beispiele:
    >>> quadrat(4)
    16
    >>> quadrat(-3)
    9
    >>> quadrat(0)
    0
    """
    return x * x


def fehlerhafte_funktion(x):
    """
    >>> fehlerhafte_funktion(2)
    4
    """
    return x + 1 # Oops, sollte x * 2 sein!



#print(__name__)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)  # Führt alle Tests aus

