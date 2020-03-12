from configparser import ConfigParser
from tkinter import Tk, Label, Text, END, DISABLED, Button

from Desktop.scrap.Scrap import Scrap

class Restart :

    def onRemove():
        config = ConfigParser()
        with open('WishList.ini', 'r+') as f:
            config.read_file(f)
            config.remove_section('wishlist')
            f.seek(0)
            config.write(f)
            f.truncate()

    def fetch(self):
        config = ConfigParser()
        print(config.read('WishList.ini'))
        url = config.get('wishlist', 'url')
        title = config.get('wishlist', 'title')
        price = config.get('wishlist', 'price')
        return url, title, price

    def restartWidow(self):
        restartObj = Restart()
        url, title, price = restartObj.fetch()
        newTitle, newPrice = Scrap.onScrap(url)

        mainWindow = Tk()
        mainWindow.geometry("750x280")
        mainWindow.title("Wishlist")
        labelOld = Label(mainWindow, text="Previous:", font=("arial", 50, "bold"))
        labelOld.place(x=5, y=20)
        labelTitle = Label(mainWindow, text="Title:", font=("arial", 50, "bold"))
        labelTitle.place(x=5, y=50)
        text = Text(mainWindow, height=4, width=41)
        text.place(x=2, y=85)
        text.insert(END, title)
        text.config(state=DISABLED)
        labelPrice = Label(mainWindow, text="Price(Rs.):", font=("arial", 50, "bold"))
        labelPrice.place(x=5, y=160)
        text = Text(mainWindow, height=2, width=15)
        text.place(x=110, y=160)
        text.insert(END, price)
        text.config(state=DISABLED)
        butRemove = Button(mainWindow, text="Remove From List", height=2, width=20, font=("arial", 50, "bold"),
                           command=self.onRemove)
        butRemove.place(x=60, y=210)

        sep = ('|' + '\n') * 20
        labelSeparate = Label(mainWindow, text=sep)
        labelSeparate.place(x=350, y=20)

        labelNew = Label(mainWindow, text="New:", font=("arial", 50, "bold"))
        labelNew.place(x=400, y=20)
        labelTitle = Label(mainWindow, text="Title:", font=("arial", 50, "bold"))
        labelTitle.place(x=405, y=50)
        text = Text(mainWindow, height=4, width=41)
        text.place(x=401, y=85)
        text.insert(END, newTitle)
        text.config(state=DISABLED)
        labelPrice = Label(mainWindow, text="Price(Rs.):", font=("arial", 50, "bold"))
        labelPrice.place(x=405, y=160)
        text = Text(mainWindow, height=2, width=15)
        text.place(x=515, y=160)
        text.insert(END, newPrice)
        text.config(state=DISABLED)

        mainWindow.mainloop()




