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

dictionary={R:1,S:2,P:3} #Dizionario per convertire le scelte

while(newgame):
    print("Player1 choose R-P-S:") #Scelta giocatore 1
    choice1=input() #Lettura tastiera

    print("Player2 choose R-P-S:") #Scelta giocatore 2
    choice2=input() #Lettura tastiera
