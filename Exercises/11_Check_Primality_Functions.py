'''
Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.).
You can (and should!) use your answer to Exercise 4 to help you.
Take this opportunity to practice using functions, described below.
'''

num=36

divisors=[] #Lista dei divisori

#Aggiunge ala lista tutti i divisori
for k in range(2,num+1):
    if(num%k==0):
        divisors.append(k)

#Se è presente solo "se stesso" nella lista allora è primo, altrimenti no
if(len(divisors)==1):
    print("Il numero e' primo")
else:
    print("Il numero non e' primo")