'''
Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on
the New York Times homepage.
'''
from urllib.request import urlopen
url ='http://www.python.org/'
for line in urlopen(url):
    text=line.decode('utf-8')
    if('<title>' in text):
        print(text)
