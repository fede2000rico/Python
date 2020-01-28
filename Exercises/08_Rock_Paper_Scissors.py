'''
Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner,
and ask if the players want to start a new game)

Remember the rules:
    Rock beats scissors
    Scissors beats paper
    Paper beats rock
'''

newgame=1 #Variabile per continuare il gioco

dictionary={'R':1,'S':2,'P':3} #Dizionario per convertire le scelte

while(newgame):
    print("Player1 choose R-P-S:") #Scelta giocatore 1
    choice1=input() #Lettura tastiera

    print("Player2 choose R-P-S:") #Scelta giocatore 2
    choice2=input() #Lettura tastiera

    #CONFRONTO DI OGNI POSSIBILE GIOCATA
    if(dictionary[choice1]==1):
        if(dictionary[choice2]==1):
            print("Draft")
        if(dictionary[choice2]==2):
            print("Player1 win")
        if(dictionary[choice2]==3):
            print("Player2 win")

    if(dictionary[choice1]==2):
        if(dictionary[choice2]==1):
            print("Player1 win")
        if(dictionary[choice2]==2):
            print("Draft")
        if(dictionary[choice2]==3):
            print("Player2 win")

    if(dictionary[choice1]==3):
        if(dictionary[choice2]==1):
            print("Player1 win")
        if(dictionary[choice2]==2):
            print("Player2 win")
        if(dictionary[choice2]==3):
            print("Draft")

    #OPERAZIONI CHE INTERROMPONO IL CICLO IN CASO DI RISPOSTA NEGATIVA
    print("Want to play again? Y or N")
    if(input()=='N'):
        newgame=0
