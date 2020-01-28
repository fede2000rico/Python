'''
Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 10.

Extras:

1. Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
'''

mylist = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

#DEFINIZIONE FUNZIONI
def mod1(mylist):
    for k in mylist:
        if(k<10):
            print(k)

    print("Done mod 1!")#Normal

def mod2(mylist): #Extra 1
    newlist=[]
    for k in mylist:
        if(k<10):
            newlist.append(k)

    print(newlist)
    print("Done mod 2!")


mod1(mylist) #Lancia la modalità 1

mod2(mylist) #Lancia la modalità 2
