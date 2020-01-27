#Esercizio per lavorare con gli indici delle stringhe
s1='stringa di testo'

#Funzione che restituisce l'indice della prima occorrenza
print('Esempio 1:')
index=s1.index('i')
print(index)

#Funzione per ricavare il carattere in una certa posizione
print('\nEsempio 2:')
character=s1[3]
print(character)
character=s1[0:7] #7 escluso
print(character)

#Controlla se la stringa inizia con una sottostringa [BOOL]
print('\nEsempio 3:')
s1.startswith('str')
print(s1.startswith('str')) #true

#Funzione che conta il numero di occorrenze di una sottostringa
print('\nEsempio 4:')
s1.count('di')
print(s1.count('di')) #1

#Funzione che trasforma in maiuscolo tutte le iniziali
print('\nEsempio 5:')
s2=s1.title()
print(s2) #Stringa Di Testo

#Moltiplicazione di stringhe e concatenazione
print('\nEsempio 6:')
s1='ciao'
print(s1*3) #ciaociaociao

print(s1+'prova') #ciaoprova

print('44'+'33') #4433

print(int('44')+int('33')) #77
