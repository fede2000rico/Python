'''
Write a program (using functions!) that asks the user for a long string containing multiple words.
Print back to the user the same string, except with the words in backwards order. For example, say I
type the string:

  My name is Michele
Then I would see the string:

  Michele is name My
shown back to me.
'''

string="Ciao come stai ? io tutto ok" #Al posto di chiederla

list=string.split(" ") #Salva tutti gli elementi separati da spazi in una lista
print(list)

list.reverse() #Inverto l'ordine della lista
print(list)
