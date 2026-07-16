import re

# Es dürfen nur Emails mit der Endung meinefirma.de matchen


emails = [
    "test@meinefirma.de",  # ok
    "TEST@meinefirma.de",  # ok
    "test123@meinefirmade",  # ok
    "v.nachname@meinefirma.de", # ok
    "v-nachname@meinefirma.de", # ok
    "v_nachname@meinefirma.de", # ok
    "nicht gut@meinefirma.de", # falsch
    "nicht @meinefirma.de",  # falsch
    "ok@meinefirma.de " , # falsch
    " ok@meinefirma.de " , # falsch
    "thomas:eses@meinefirma.de " , # falsch
]


     