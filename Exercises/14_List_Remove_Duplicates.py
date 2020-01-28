'''
Write a program (function!) that takes a list and returns a new list that contains all the elements
of the first list minus all the duplicates.
'''

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 1, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 6, 9, 10, 4, 11, 12, 13]

#Ciclo su ogni elemento e se duplicato allora lo elimina fino a lasciarne uno solo
for k in a:
	if(a.count(k)>1):
		while(a.count(k)!=1):
			a.remove(k)

#Ciclo su ogni elemento e se duplicato allora lo elimina fino a lasciarne uno solo
for k in b:
	if(b.count(k)>1):
		while(b.count(k)!=1):
			b.remove(k)

a.sort() #Ordina la lista
b.sort()
print(a)
print(b)
