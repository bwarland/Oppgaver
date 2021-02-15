

from urllib.request import urlopen
from bs4            import BeautifulSoup

html=urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
KBacon=BeautifulSoup(html)

for link in KBacon.findAll("a"):
    if 'href' in link.attrs:
        print(link.attrs['href'])
