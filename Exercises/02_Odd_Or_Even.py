'''
Ask the user for a number. Depending on whether the number is even or odd,
print out an appropriate message to the user.
Hint: how does an even / odd number react differently when divided by 2?
'''

print("Inserire un numero:")
num=input() #Lettura tastiera

num=int(num) #Conversione

if (num%2==0):
    if (num%4==0):
        print("Divisibile per 4!")
    else:
        print("Divisibile per 2!")

else:
    print("Non divisibile per 2!")
