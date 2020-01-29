'''
Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to
largest) and another number. The function decides whether or not the given number is inside the list and returns
(then prints) an appropriate boolean.
'''

#Funzione che controlla l'esistenza e ritorna un valore booleano
def check(num, list):
    if(num in list):
        return True
    else:
        return False

mylist=[1,2,3,4,5,6,7,8,9,0]
num=int(input()) #Input utente

print(check(num,mylist))
