from configparser import ConfigParser
from tkinter import Tk, Label, Text, END, DISABLED, Button
from Desktop.scrap.Scrap import Scrap

class Restart :

    def resave(self, product, newPrice, newTitle, url):
        config = ConfigParser()
        config.read('WishList.ini')
        config.remove_section(product)
        config.add_section(product)
        config.set(product,'url',url)
        config.set(product,'title',newTitle)
        config.set(product,'price',newPrice)
        with open('WishList.ini', 'w') as configfile:
            config.write(configfile)

    def onRemove(self, product, total, counter, listOfProducts, previousWindow):
        config = ConfigParser()
        restartObj = Restart()
        with open('WishList.ini', 'r+') as f:
            config.read_file(f)
            config.remove_section(product)
            f.seek(0)
            config.write(f)
            f.truncate()
        f.close()
        restartObj.restartWidow(counter, total, listOfProducts, previousWindow)

    def fetch(self, product):
        config = ConfigParser()
        print(config.read('WishList.ini'))
        url = config.get(product, 'url')
        title = config.get(product, 'title')
        price = config.get(product, 'price')
        return url, title, price

    def restartWidow(self, counter, total, listOfProducts, previousWindow):

        if(previousWindow is not None):
            previousWindow.destroy()

        if(counter == total):
            return

        restartObj = Restart()


        product = listOfProducts[counter]
        url, title, price = restartObj.fetch(product)

        newTitle, newPrice = Scrap.onScrap(url)
        counter = counter + 1
        restartObj.resave(product, newPrice, newTitle, url)

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
          command= lambda : restartObj.onRemove(product, counter, total, listOfProducts, mainWindow)  )
        butRemove.place(x=60, y=210)

        butNext = Button(mainWindow,text="Next",height=2,width=20,
          font = ("arial",50,"bold"),command= lambda : restartObj.restartWidow(counter, total, listOfProducts, mainWindow) )
        butNext.place(x=360,y=210)

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


restartObj = Restart()
config = ConfigParser()
print(config.read('WishList.ini'))
listOfProducts = config.sections()
total = len(listOfProducts)
counter=0
restartObj.restartWidow(counter, total, listOfProducts, None)