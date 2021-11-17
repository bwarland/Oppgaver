# hentet i fra boken 

from urllib.request import urlopen       # find and open web page 
from bs4            import BeautifulSoup # search through HTML code
import re                                # pattern matching

html=urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
KBacon=BeautifulSoup(html)

for link in KBacon.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$")):
    if 'href' in link.attrs:
        print(link.attrs['href'])

    
