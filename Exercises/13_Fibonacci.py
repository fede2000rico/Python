'''
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number
of numbers in the sequence to generate.(Hint: The Fibonnaci sequence is a sequence of numbers where the
next number in the sequence is the sum of the previous two numbers in the sequence.
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
'''

limit=15 #Al posto di chiedere all'utente

fibonacci_seq=[1]

fibonacci_seq.append(fibonacci_seq[0]) #Il primo numero va ripetuto

for k in range(2,limit):
    #aggiunge l'elemento dato dalla somma dei due precedenti
    fibonacci_seq.append(fibonacci_seq[k-2]+fibonacci_seq[k-1])

#Output
print(fibonacci_seq)
print(len(fibonacci_seq))
