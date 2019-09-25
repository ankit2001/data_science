from urllib.request import urlopen
from urllib.error import HTTPError , URLError
from bs4 import BeautifulSoup
def getKnow(url):
    try:
        html=urlopen(url)
        obj=BeautifulSoup(html,"lxml")
        know=obj.h1
    except AttributeError:
        return None
    except URLError:
        return None  
    return know     
know=getKnow("http://pythonscraping.com/pages/page1.html")  
if know==None:
    print("title could not be found") 
else:
    print(know)     
