"""
    Script zum demonstrieren des exitcodes
	Nach dem Aufruf des Scriptes aus der Konsole, kann man mit
	echo %ERRORLEVEL% unter windows, den exit status feststellen

	0 - Kein Fehler
	> 1 - Fehler

	https://learn.microsoft.com/de-de/windows/win32/debug/system-error-codes--0-499-
"""

x = 1
print("hallo")

try:
    if (x < 0):
        raise Exception("x ist kleiner als 0")
except Exception as error:
    print("error")
    exit(1)
finally:
    print("dies ist der finally Block")

print("ende...")
exit(0)

