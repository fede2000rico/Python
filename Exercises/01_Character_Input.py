'''
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.
'''

from datetime import datetime
print("Inserisci la tua data di nascita:")

age=input() #Legge da tastiera

age=int(age) #Convarte in intero

age=datetime.now().year-age #Trova l'anno di nascita

print("Nel " + str(age+100) + " avrai 100 anni!")
