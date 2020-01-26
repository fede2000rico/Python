#Funzioni per controllare i valori nulli
list=[1,0,2]
set={1,'due',3}

#Esiste un elemento NON nullo?
print("Funzione any:")
print(any(list)) #true
print(any([0,0,0])) #false

#Tutti gli elementi sono NON nulli?
print("\nFunzione all:")
print(all(list)) #false
print(all(set)) #true
