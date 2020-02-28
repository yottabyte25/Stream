import bs4 as bs
import urllib.request

source = urllib.request.urlopen('http://127.0.0.1:5500/test.html').read()
soup = bs.BeautifulSoup(source, "lxml")

search = input("Enter a variable to search: ")
if search.lower() == "div" :
    print(soup.div)
elif search.lower() == "p" :
    print(soup.p)
elif search.lower() == "style":
    print(soup.style)
elif search.lower() == "h1":
    print(soup.h1)
elif search.lower() == "h2":
    print(soup.h2)
elif search.lower() == "head":
    print(soup.head)