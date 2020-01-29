'''
Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article on This
website: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.

The article is long, so it is split up between 4 pages. Your task is to print out the text to the screen so that
you can read the full article without having to click any buttons.

(Hint: The post here describes in detail how to use the BeautifulSoup and requests libraries through the solution
of the exercise posted here.)

This will just print the full text of the article to the screen. It will not make it easy to read, so next exercise
we will learn how to write this text to a .txt file.
'''
#IMPORTO LIBRERIE NECESSARIE
import requests
from bs4 import BeautifulSoup

#SET DEL SITO WEB CHE VOGLIO ANALIZZARE
base_url = "https://www.practicepython.org/"

#"CHIEDO" UNA COPIA DELL'HTML
r = requests.get(base_url)

#Creo una soup
soup = BeautifulSoup(r.text, "html.parser")

#Seleziono il blocco dell'html
text = soup.select("a")

#Apro il file di scrittura
file=open('C:/Users/fede2/OneDrive/Documenti/GitHub/Python/Exercises/data_file/19_data.txt','w')

#Stampa ogni elemento all'interno di text
for elem in text:
    file.write(elem.text +'\n')
    print(elem.text)

file.close()
