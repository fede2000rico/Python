#Funzione per capire se una funzione è presente nel built-in

#Esempio 1
print(callable(sum)) #La funzione è presente nel built-in, quindi posso chiamarla

#Dichiaro una lista di numeri arbitraria e ne stampo la somma
num=[1,5,3]
print(sum(num))


#Esempio 2
print(callable(num.sort)) #La funzione relativa alla lista è presente nel built-in, quindi posso chiamarla

#Ordino la lista e la stampo
num.sort()
print(num)
