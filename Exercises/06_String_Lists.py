'''
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
'''

print("Inserire una parola:")

string=str(input()) #Lettura e cast esplicito

lenght=len(string)

for i in range(0,lenght):
    if(string[i]!=string[lenght-1-i]):
        i=lenght
        check=0
    else:
        check=1

if(check):
    print("La parola è palindroma!")
else:
    print("La parola non è palindroma!")
