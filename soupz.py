import bs4 as bs
import urllib.request
#This is the source URL that we are going to be extracting data from
source = urllib.request.urlopen('http://127.0.0.1:5500/test.html').read()

#This is the soup. The soup is the product which we create by adding
soup = bs.BeautifulSoup(source, "lxml")

def result():
    print(soup.div)