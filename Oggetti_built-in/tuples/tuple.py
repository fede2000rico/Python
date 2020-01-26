#Le tuple sono come le liste, ma possono contenere un qualsiasi oggetto al loro interno.
#MA NON SONO MODIFICABILI
tup=(1,'due',[1,'lista'],2,'due')
print(tup.index('due')) #1
print(tup.count('due')) #2

print(tup)

#Darà errore perche NON è modificabile
#tup.extend([5])
