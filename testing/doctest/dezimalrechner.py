


def byteCalculationDezimal(bytes: int) -> str:
    """

    >>> byteCalculationDezimal(900)
    '900 Bytes'
    >>> byteCalculationDezimal(1000)
    '1 kB'
    >>> byteCalculationDezimal(1024)
    '1,024 kB'
    >>> byteCalculationDezimal(10000)
    '10 kB'
    >>> byteCalculationDezimal(100000)
    '100 kB'
    >>> byteCalculationDezimal(1000000)
    '1 MB'
    >>> byteCalculationDezimal(1000001)
    '1 MB'
    >>> byteCalculationDezimal(1001000)
    '1,001 MB'
    >>> byteCalculationDezimal(1239000)
    '1,239 MB'
    >>> byteCalculationDezimal(1239900)
    '1,240 MB'
    >>> byteCalculationDezimal(1234400)
    '1,234 MB'
    >>> byteCalculationDezimal(1234567)
    '1,235 MB'
    >>> byteCalculationDezimal(1234567891)
    '1,235 GB'
    >>> byteCalculationDezimal(1234567891234)
    '1,235 TB'

    """
    ergebnis = bytes
    endung = "Bytes"

    if bytes >= 1000 ** 4:
        ergebnis = bytes / 1000 ** 4
        endung = "TB"
    elif bytes >= 1000 ** 3:
        ergebnis = bytes / 1000 ** 3
        endung = "GB"
    elif bytes >= 1000 ** 2:
        ergebnis = bytes / 1000 ** 2
        endung = "MB"
    elif bytes >= 1000 ** 1:
        ergebnis = bytes / 1000 ** 1
        endung = "kB"

    # kosmetik
    # auf drei stellen nach dem Komma runden aber auch 3 nullen lassen
    ergebnis = f"{ergebnis:.3f}"

    # Punkt gegen komma ersetzen
    ergebnis = ergebnis.replace(".", ",")

    # ,000 abschneiden
    ergebnis = ergebnis.replace(",000", "")

    # rückgabe
    return f"{ergebnis} {endung}"



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

