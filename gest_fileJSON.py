# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 21:32:45 2020

@author: andrea_sergiacomi

gestione file JSON
"""

import json as jj
dati = jj.load(open("esempi2.json")) # i dati nel file vengono trasformati in un dizionario
print(dati, '\n')
lista = dati["Tabella"]["Riga"] # prendo solo le Righe della Tabella e creo invece una lista
print(lista, '\n')
# aggiungo un nuovo record Cliente con chiavi e valori
dati["Tabella"]["Riga"].append({'data': '2019-06-18T00:00:00.000', 'Cliente': 'Mario Rossi', 'descrizioneTipoSoggetto': 'Privato', 'DescTipoProd': 'Bene', 'denominazioneProdotto': 'smartphone', 'importo': '500', 'Fornitore': 'Samsung'})
print(dati, '\n')
# creo nuovo file json (con una Riga – Cliente in più) --- w sta per write / indentazione con 4 spazi
with open("output1.json", "w") as outfile:
    jj.dump(dati, outfile, indent=4)
