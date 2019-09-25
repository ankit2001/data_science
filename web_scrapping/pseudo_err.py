from urllib.request import urlopen
from bs4 import BeautifulSoup
try:
    html=urlopen("http://pythonscraping.com/pages/page1.html")
    obj=BeautifulSoup(html.read(),"lxml")
    b_content=obj.nonExistingTag.anotherTag
except AttributeError as e:
    print("Tag was not found")
else:
    if b_content==None:
        print("Tag was not found")
    else:
        print(b_content)        