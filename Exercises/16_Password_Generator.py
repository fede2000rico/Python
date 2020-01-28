'''
Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix
of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new
password every time the user asks for a new password. Include your run-time code in a main method.
'''

import string,random #Librerie per alfabeto, simboli e generazione random

#Creo una lista con tutti i caratteri possibili
list_char=[elem for elem in string.ascii_letters + string.digits + string.punctuation]

#Genero una sequenza di n elementi random scelti in una lista
list_password=random.sample(list_char,24)
password=''

#Trasformo la lista in stringa e stampo
for k in list_password:
    password+=k


print(password)
