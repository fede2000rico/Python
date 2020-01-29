'''
Take the code from the How To Decode A Website exercise (if you didn’t do it or just want to play with
some different code, use the code from the solution), and instead of printing the results to a screen,
write the results to a txt file. In your code, just make up a name for the file you are saving to.
'''

#Esercizio 17 edit
from urllib.request import urlopen
url ='http://www.python.org/'

#Apro il file
file=open('C:/Users/fede2/OneDrive/Documenti/GitHub/Python/Exercises/data_file/21_data.txt','w')

for line in urlopen(url):
    text=line.decode('utf-8')
    if('<title>' in text):
        file.write(text)
