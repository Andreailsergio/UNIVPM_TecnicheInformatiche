# a_list è lo stesso oggetto - mutabile - anche dopo le aggiunte
a_list = ["milk", "eggs", "bread"]
print(id(a_list))
a_list.append("bacon") # inserisce elemento in coda
print(id(a_list))
# b e c sono liste diverse anche se hanno stesso contenuto
b_list = ["cramberries", "chicken"]
c_list = ["cramberries", "chicken"]
print(b_list == c_list)
print(b_list is c_list, "\n")

# fondere più liste
a_list.extend(b_list+c_list)
print(a_list, "\n")

# lunghezza - elemento iesimo - conteggio elementi - prima posizione dell'elemento
print(len(a_list))
print(a_list[0])
print(a_list.count('cramberries'))
print(a_list.index('cramberries'), "\n")

# cancellare l'ultimo elemento
a_list.pop()
print(a_list)
# cancellare l'elemento al 7° posto (con indice 6)
a_list.pop(6)
print(a_list, "\n")

# inserire elemento in seconda posizione (tra milk ed eggs)
a_list.insert(1, "potatoes")
print(a_list, "\n")

# sostituire il valore del primo elemento (da milk a croissant)
a_list[0]="croissant"
print(a_list, "\n")

# conversione stringa in lista
stringa_alimenti="ketchup,mayonnaise,ginger,pepper"
d_list=stringa_alimenti.split(",")
print(d_list)
print(type(d_list), "\n")

# lista di alimenti in ordine alfabetico crescente - e poi invertiti
a_list=a_list+d_list # inserisce tutti gli elementi della lista D in coda ad A
print(a_list, "\n")
a_list.sort()
print(a_list, "\n")
a_list.reverse()
print(a_list, "\n")

# lista di liste
e_list=[["gin", "tonic water"], ["vodka", "martini"], ["rhum", "coke"]]
print(e_list)
