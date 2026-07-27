@echo off

c:\Python\Python310\python.exe "exception_exitcode.py"

if %ERRORLEVEL% == 0 (
    echo "Erfolgreich beendet"
) else (
    echo "Programm mit Fehlern beendet"
)

pause
