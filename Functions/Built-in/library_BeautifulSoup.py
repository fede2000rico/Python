#Esercizio standard per clonare ed analizzare siti web

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

#Stampa ogni elemento all'interno di text
for elem in text:
  print(elem.text)
