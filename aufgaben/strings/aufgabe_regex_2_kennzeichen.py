
# Erkennung eines deutschen KFZ Kennzeichens
import re

kennzeichen = [
    "WÜ AB 12",  # falsch
    "B M 1",  # true
    "B MW 1",  # true
    "WES A 1000",  # true
    "WES A 1000E",  # true
    "DU ME 123" ,  # true
    "DU ME 123H",   # true
    " DU ME 123H ",   # falsch
    " DU ME 12-3H ",  # falsch
    " ABC A 123"      # falsch
]
