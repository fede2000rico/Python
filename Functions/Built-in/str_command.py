#Estrazione di un comando da una stringa
str='2*2'

#Valuta l'operazione contenuta nella stringa
print("Eval:")
print(eval(str))

#Esegue un'operazione nella stringa
print("\nExec:")
str='a='+str #a=2*2
exec(str)
print(a) #4
