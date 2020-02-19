import bs4 as bs
import urllib.request
from tkinter import *

#initializing tkitner
source = urllib.request.urlopen('http://127.0.0.1:5500/test.html').read()
soup = bs.BeautifulSoup(source, "lxml")
root = Tk()

#title
root.title("Price Finder")

#window size
root.geometry("800x700")

#Search command
def search():
    G = print(soup.div)
    Gather = Label(root, text = G)
    Gather.grid()
#Label
L1 = Label(root, text = "Item", font = ("bold", 18), padx = 20, pady = 20)
E1 = Entry(root, width = 20, bd = 2)
B1 = Button(root, text = "Enter", font = ("bold", 14), height = 1, width = 4, command = search)

#grid
L1.grid(row = 0, column = 0)
E1.grid(row = 0, column = 1)
B1.grid(row = 0, column = 2)
#List box
Lb1 = Listbox(root, bd = 0, width = 40)
#grid
Lb1.grid(row = 3, column = 1)
#main loop that runs the game
root.mainloop()