# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 20:11:45 2020

@author: andrea_sergiacomi
"""
# puntamento in memoria ad oggetti per variabili immutabili (numeri interi)
a=1
print("ID a")
print(id(a))
b=a #stessa cosa se pongo b=1
print("ID b - dopo b=a")
print(id(b))
a=2
print("ID a modificato - dopo a=2")
print(id(a))
print("b continua a valere: ", b)


# puntamento in memoria ad oggetti per variabili mutabili (lista)
genius = ["einstein","galileo"]
print("\nID GENIUS")
print(id(genius))
smart = genius
print("ID SMART - dopo smart=genius")
print(id(smart))
genius.append("shakespeare")
print("SMART è un alias e CONTIENE come GENIUS", smart) # smart è un ALIAS di genius - mantiene stesso ID ovvero puntano allo stessa location in memoria
print("GENIUS:", genius, "\n")


# ALIASING di oggetti mutevoli introduce cambiamenti anche se le variabili sono definite nel corpo principale e in una funzione (come parametro)
def add_word(d, word, definition):
        """
        PARAMETRI:
        d -> dizionario
        word -> stringa
        definition -> stringa
        VALORE DI RITORNO: nessuno
        SCOPO: Aggiunge nel dizionario parola (chiave) e definizione (valore). Se la parola esiste già appende una nuova ulteriore definizione
        """
        if word in d:
            d[word].append(definition)
        else:
            d[word] = [definition]

words={}
add_word(words, "box", "combattimento")
add_word(words, "box", "contenitore")
add_word(words, "boss", "capo")
print(words, "\n")


# per fare una copia di oggetti pesanti, come liste e dizionari, creando un nuovo oggetto anzichè usare aliasing
# o creo una nuova lista/dizionario contenente gli stessi elementi dell'altro oggetto (COPIA ESPLICITA)
personaggi = list(genius)
print("ID PERSONAGGI dopo copia esplicita lista")
print(id(personaggi))
# o uso il comando COPY
celebrità = genius.copy()
print("ID CELEBRITA' dopo comando copy")
print(id(celebrità), "\n")


# SORTED - crea automaticamente una copia ma ordinata della lista
kid_ages = [2, 1, 4]
sorted_ages = sorted(kid_ages)
print("original KID_AGES", kid_ages)
print("SORTED_AGES", sorted_ages, "\n")


# GESTIRE MODIFICHE A DIZIONARI O LISTE DENTRO I CICLI
# esempio “rimuovere tutti gli elementi con valore 1 da dizionari o liste”
print("MODIFICHE A DIZIONARI O LISTE DENTRO I CICLI")
# DIZIONARIO
# togliere commenti per eseguire
#Dsongs = {"Wannabe":1, "Roar":1, "Let It Be":5, "Red Corvette":4}
#for s in Dsongs.keys():
#     if Dsongs[s] == 1:
#       Dsongs.pop(s)
# ERRORE: Python non permette di cambiarne dimensione al DIZIONARIO mentre si sta iterando sull’oggetto

# LISTA
Lsongs = [1, 1, 5, 4]
for s in Lsongs:
	if s == 1:
		Lsongs.remove(s)
print(Lsongs)
# RISULTATO ERRATO [1, 5, 4]: alla seconda iterazione, dopo aver rimosso il primo 1, si è all’indice 1 che contiene 5: il secondo 1 non viene rimosso

Lsongs2 = [1, 1, 5, 4]
songs_copy = Lsongs2.copy()
Lsongs2 = []
for s in songs_copy:
	if s != 1:
		Lsongs2.append(s)
print(Lsongs2, "\n")
# METODO CORRETTO: procedo al contrario
# copio in una nuova struttura, svuoto la lista originaria, ci appendo – a partire dai dati nella copia - solo gli item che rispettano i requisiti, cioè diversi da 1