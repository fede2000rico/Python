#I set sono dei contenitori non ordinati. Gli oggetti che contengono sono immutabili (quindi non può contenere liste)
#Sono come degli insiemi matematici (unione, intersezione,...)
s1={1,'uno',2,3,'quattro'}
s2={5,'uno'}

#Unione
print("Unione:")
print(s1 | s2) #{'quattro', 1, 2, 3, 'uno', 5}

#Intersezione
print("\nIntersezione:")
print(s1 & s2) #{'uno'}

#Differenza
print("\nDifferenza:")
print(s1-s2) #{1, 2, 3, 'quattro'}
