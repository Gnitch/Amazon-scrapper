import re
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

class Scrap :

    @staticmethod
    def onScrap(url):
        try :
            title = ""
            price = ""
            url = urlopen(url)
            bs = BeautifulSoup(url,'html.parser')
            title = bs.find('span',{'id' : 'productTitle'}).get_text().strip()
            price = bs.find('span',{'id' : re.compile('priceblock*') }).get_text()
            price = price[2:len(price)]
            return title, price
        except HTTPError as e :
            print(e)
            return None, None


