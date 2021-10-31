# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 19:02:37 2020

@author: andrea_sergiacomi
"""

# creo un dizionario – prima vuoto – nota le parentesi grafe – non c’è un ordine se non quello di inserimento
grocery = {}
grocery = {"milk":1, "eggs":12, "bread":2}
grocery["bacon"]=44 
# aggiunge in coda chiave e valore 
# (o modifica il valore di una chiave se già esistente, perché il DIZIONARIO è mutabile, ma la KEY è unica e immutabile)
print(grocery)
print(len(grocery)) # 4
removed=grocery.pop("bacon")  # POP rimuove chiave e valore
print(removed) # 44 (ma può memorizzare il valore che aveva la chiave rimossa)
grocery["eggs"]= grocery["eggs"]-2 # sottrae 2 uova dal valore
print(grocery) # {'milk': 1, 'eggs': 10, 'bread': 2}
print(grocery.keys()) # restituisce solo le chiavi: dict_keys(['milk', 'eggs', 'bread'])
# grocery.keys è una specie di lista
for one_item in grocery.keys():
	print(one_item)
# ma posso crearmi una vera e propria lista di chiavi con un casting
all_items = list(grocery.keys())
# analogamente c’è il comando VALUES 
all_items_values = list(grocery.values())
print(all_items_values)
