#HTTPError and URLError
from urllib.request import urlopen 
from bs4 import BeautifulSoup
from urllib.error import HTTPError , URLError 
try:
	html=urlopen("http://pythonscraping.com/pages/page1.html")
	pointer=BeautifulSoup(html.read(),"lxml")
	print(pointer.h1)
except HTTPError as e:
    print(e)
except URLError as e:
    print("url not found")
except:
    print("some unknown error")         	
