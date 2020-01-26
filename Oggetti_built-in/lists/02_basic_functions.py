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
print("\nEsempio 4:")
print(mylist.pop()) #1
print(mylist) #'ciao', 'c', 'b', 'a', 4, 7, 5, 3, 2

#Aggiunge in coda
print("\nEsempio 5:")
mylist.append(0)
mylist.extend([1,9])
mylist = mylist + ['prova']
print(mylist) #'ciao', 'c', 'b', 'a', 4, 7, 5, 3, 2, 0, 1, 9, 'prova'
