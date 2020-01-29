'''
Create a program that will play the “cows and bulls” game with the user. The game works like this:

Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
For every digit that the user guessed correctly in the correct place, they have a “cow”.
For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess,
tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over.
Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.

Say the number generated by the computer is 1038. An example interaction could look like this:

  Welcome to the Cows and Bulls Game!
  Enter a number:
  >>> 1234
  2 cows, 0 bulls
  >>> 1256
  1 cow, 1 bull
  ...
Until the user guesses the number.
'''

num=[1,2,3,4]

def read():
    print("Inserire un numero a 4 cifre:")
    user_input=int(input())
    user_num=[]
    for k in range(0,4): #4 escluso
        user_num.append(user_input%10)
        user_input=user_input//10

    user_num.reverse()
    return user_num

check=1 #Valore sentinella
while(check):
    #Set dati iniziali
    user_num=read()
    cows=0
    bulls =0

    #Verifica se sono uguali
    for i in range(0,4): #4 escluso
        #Verifica se è presente nella lista ma in un'altra posizione
        if(user_num[i]==num[i]):
            cows+=1
        #Verifica che siano presenti nel numero da indovinare in ripetizioni uguali
        elif(user_num[i]!=num[i] and user_num[i] in num and num.count(num[i])==user_num.count(user_num[i])):
            bulls+=1

    #Se il risultato è corretto, altrimenti...
    if(cows==4):
        check=0
        print("Corretto!")
    else:
        print("Ritenta!")
    #Stampa i risultati
    print(cows,bulls)
