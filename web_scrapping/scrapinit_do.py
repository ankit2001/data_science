from urllib.request import urlopen 
from urllib.error import *
from bs4 import BeautifulSoup as bs
"""def get(url,first,sec):
    try:
        html=urlopen(url)
        pointer=bs(html.read(),"lxml")
        content=pointer.first.sec
        return content
    except URLError as e:
        print("url not found")
    except HTTPError as e:
        print(e)
    except AttributeError as e:
        print("tag not found")
    except:
        print("tag not found or some unexpected error")
        """

def get(url):
    try:
        html=urlopen(url)
        pointer=bs(html.read(),"lxml")

        content=pointer
        return content
    except URLError as e:
        print("url not found")
    except HTTPError as e:
        print(e)
    except AttributeError as e:
        print("tag not found")
    except:
        print("tag not found or some unexpected error")     
              
#info=get("http://pythonscraping.com/pages/page1.html","body","h1")
noew=get("http://pythonscraping.com/pages/page1.html")
print(noew)








