#lets start
from urllib.request import urlopen
from bs4 import  BeautifulSoup
html=urlopen("http://pythonscraping.com/pages/page1.html")
pointer=BeautifulSoup(html.read(),"lxml")
print(pointer.h1)