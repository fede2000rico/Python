#Esercizi con le liste basici
mylist=[1,2,3,5,7,4,'a','b','c','ciao']

#Funzione index restituisce l'indice della prima occorrenza della ricerca
print("Esempio 1:")
mylist.index(4)
print(mylist.index(4)) #5
print(mylist[6]) #a
print(mylist[0:3]) #1, 2, 3 [indice 3 escluso]

#Verifica se un elemento è presente nella lista
print("\nEsempio 2:")
check='ciao' in mylist
print(check) #True

#Funzione reverse, inverte l'ordine della lista
print("\nEsempio 3:")
mylist.reverse()
print(mylist)

#Funzione per restituire ed eliminare l'ultimo elemento della lista
mylint.pop()
