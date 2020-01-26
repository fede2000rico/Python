#Esercizi base con i dizionari
#In pratica sostituisce una parola con il rispettivo elemento

diz={'cane':'bau','gatto':'miao','uno':1,2:'due'}

#Stampa la sostituzione
print("Esempio 1:")
print(diz['cane']) #bau
print(diz[2]) #due

#Verifica se esiste la chiave di ricerca ["da tradurre, non tradotta"]
print("\nEsempio 2:")
print(2 in diz) #true
print('bau' in diz) #false

#Restituisce ed elimina l'elemento corrispondente
print("\nEsempio 3:")
print(diz.pop('cane')) #bau
print(diz) #{'gatto': 'miao', 'uno': 1, 2: 'due'}

#Incrementa un valore int corrispondente all'elemento
print("\nEsempio 4:")
diz['uno']+=2
print(diz) #{'gatto': 'miao', 'uno': 3, 2: 'due'}
