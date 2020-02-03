'''
Python’s zip() function is defined as zip(*iterables). The function takes in iterables as arguments and
returns an iterator. This iterator generates a series of tuples containing elements from each iterable.
zip() can accept any type of iterable, such as files, lists, tuples, dictionaries, sets, and so on.
'''

#Definizione di liste
numbers=[1,2,3,4]
numbers2=[1,2,3]
letters=['a','b','c','d']

#Funzione zip, prima zippo e poi trasformo in lista
zipped=list(zip(numbers,letters))

#Stampo risultato
print(zipped) #[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
print('\n')


#Funzione zip, prima zippo e poi trasformo in lista
zipped=list(zip(numbers2,letters))

#Stampo risultato
print(zipped) #[(1, 'a'), (2, 'b'), (3, 'c')]
