# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 11:42:50 2020

@author: andrea_sergiacomi
"""

grocery = {}
grocery = {"milk":1, "eggs":12, "bread":2}
# aggiunge chiave-valore o cambia valore se chiave esistente
grocery["bacon"]=44
grocery["bread"]=3
# oppure anche 
grocery["bacon"]=grocery["bacon"]-4
print(grocery)
print(len(grocery), "\n")

# POP rimozione chiave-valore - con mantenimento nella variabile del valore della chiave rimossa
removed=grocery.pop("bacon")
print(removed)
print(grocery, "\n")

# solo le chiavi
print(grocery.keys())
for one_item in grocery.keys():
    print(one_item)
all_items = list(grocery.keys()) # diventa una lista
print(type(all_items), "\n")

# solo i valori - analogamente
all_items_values = list(grocery.values())
print(all_items_values, "\n")
