# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# metri quadri di case
kitchen=200
living_room=400
bedroom=300
bathroom=100
print("cucina, sala, camera e bagno misurano rispettivamente mq:")
print(kitchen, living_room, bedroom, bathroom)
print("il tipo della variabile bedroom")
print(type(bedroom))

# True or False (occhio alle maiuscole: contano!)
piùgrande=living_room>kitchen
print("la sala è più grande della cucina? Vero")
print("piùgrande=living_room>kitchen")
print("il tipo della variabile piùgrande")
print(type(piùgrande))
print("il valore della variabile piùgrande")
print(piùgrande)
house = kitchen + living_room + bedroom + bathroom
print("ora house - con cucina soggiorno camera e bagno - misura mq")
print(house)

# casting: conversione tipi (stringhe-interi, interi-float, …)
garage = '50'
print("il garage misura mq")
print(garage)
# house = house + garage 
# (darebbe errore)
house = house + int(garage)
print("house col garage misura mq")
print(house)

# False vale 0 True vale 1
piùgrande=int(piùgrande)
print("piùgrande booleano True - convertito in intero - vale")
print(piùgrande)
print("not(piùgrande) la negazione di vero è falso")
print(not(piùgrande))
print(int(not(piùgrande)))

# raddoppio le dimensioni di una casa
house = house*2
print("house raddoppiata")
print(house)

# calcolo le dimensioni complessive se costruisco 2 case
houses = house*2
print("identificativi delle varibili HOUSE e HOUSES")
print(id(house))
print(id(houses))
print("houses - la somma dei mq di 2 case")
print(houses)
