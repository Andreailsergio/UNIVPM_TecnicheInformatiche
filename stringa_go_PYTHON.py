# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 13:40:41 2020

@author: andrea_sergiacomi
"""

go = "it's PYTHON time"
print(go[10])
print(go[10] == go[-6])

# SLICING (estrarre parti di stringa)
# it’s  (con spazio finale)
print(go[0:5:1])
# YHNt (fino al 14° carattere, escluso)
print(go[6:14:2])
# it's PYTHON time (tutta la stringa al contrario) emit NOHTYP s'ti
print(go[-1:-17:-1])
# (col -1 vado all’indietro) P s
print(go[5:2:-1])

# lunghezza stringhe: PYTHON ha 6 caratteri – empty string 0
print(len("PYTHON"))
print(len(''))

# maiuscolo, minuscolo, prima lettera maiuscola, inverto maius minusc
print(go)
print(go.upper())
print(go.lower())
print(go.swapcase())
prin(go.capitalize())
