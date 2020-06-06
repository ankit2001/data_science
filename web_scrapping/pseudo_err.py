#Attribute error
from urllib.request import urlopen 
from bs4 import BeautifulSoup as bs
html=urlopen("http://pythonscraping.com/pages/page1.html")
pointer=bs(html.read(),"lxml")
arr=None
try:
	arr=pointer.first.second_tag
except AttributeError as e:
    print("Tag not found or 2nd tag not found")
except:    
    if arr==None:
        print("Tag not found or 1st tag not found")
    else:
        print(arr)    
