#Advanced digging
from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen("http://pythonscraping.com/pages/warandpeace.html")
obj=BeautifulSoup(html,"lxml")
namelist=obj.findAll("span",{"class":"green"})
for name in namelist:
    print(name.get_text())