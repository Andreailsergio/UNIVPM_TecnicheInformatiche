# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 21:02:35 2020

@author: andrea_sergiacomi
"""

while True:
        pwd=input("Crea una password: ")
        # verifica le condizioni
        longer_than_6 = (len(pwd)>=6)
        has_capital=False
        has_digit=False
        for ch in pwd:
            if ch in "0123456789":
                has_digit=True
            if ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                has_capital=True
        # informare l'utente che la sua password non incontra i requisiti
        if not longer_than_6:
            print("deve avere 6 o più caratteri")
        if not has_capital:
            print("deve avere almeno una lettera maiuscola")
        if not has_digit:
            print("deve avere almeno una cifra")
        # condizioni per richiedere una nuova e diversa password
        if not longer_than_6 or not has_capital or not has_digit:
            continue
        break
print("Ottima password")