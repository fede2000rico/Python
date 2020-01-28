'''
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
and makes a new list of only the first and last elements of the given list. For practice,
write this code inside a function.
'''

a = [5, 10, 15, 20, 25]

def list_cut(mylist):
    res=[]
    res.append(mylist[0]) #aggiunge il primo elemento che è fisso
    res.append(mylist[len(mylist)-1]) #Aggiunge l'ultimo elemento in funzione della lunghezza
    return res

print(list_cut(a)) #Lancia la funzione e ne stampa il risultato
