import urllib
from bs4 import BeautifulSoup
url='https://book.douban.com/top250?icn=index-book250-all'
def getdata(url):
    res=urllib.request.urlopen(url)
    html=res.read().decode()
    return html

def parsedata(html):
    soup=BeautifulSoup(html,'html.parser')
    booklist=soup.find('p12')
    print(booklist)
#print(getdata(url))
parsedata(getdata(url))