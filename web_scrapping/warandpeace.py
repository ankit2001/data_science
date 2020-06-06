#Advanced-digging
from urllib.request import urlopen 
from bs4 import BeautifulSoup as bs
html=urlopen("http://pythonscraping.com/pages/warandpeace.html")
pointer=bs(html.read(),"lxml")
list_of_names=pointer.findAll('span',{"class":"green"})
print(pointer)
for names in list_of_names:
	print(names.get_text())
