from configparser import ConfigParser
from tkinter import DISABLED, Tk, Label, Text, END, Button, Entry, BOTH
import random
from Desktop.scrap.Scrap import Scrap


class MainWindow :

    def onAddNew(self, previousWindow):
        previousWindow.destroy()
        window = Tk()
        window.geometry("300x300")
        window.title("Welcome")
        labelScrapper = Label(window, text="Amazon Web Scrapper",
            bg='red', font=("arial", 60, "bold"))
        labelScrapper.pack(fill=BOTH)
        urlInput = Entry(window, width=26)
        urlInput.place(x=65, y=130)
        mainWindowObj = MainWindow()
        buttonScrap = Button(window, text="Scrap", height=2, width=8, font=("arial", 50,
                "bold"), command = lambda  : self.onMainWindow(urlInput.get(),window))
        buttonScrap.place(x=110, y=190)
        window.mainloop()

    def onAdd(self, url, title, price):
        id = random.randint(999,999999999)
        prodId = 'Product'+'#'+ str(id)
        print(prodId)
        config = ConfigParser()
        config.add_section(prodId)
        config.set(prodId,'url',url)
        config.set(prodId,'title',title)
        config.set(prodId,'price',price)
        with open('WishList.ini', 'a') as file :
            config.write(file)


    def onMainWindow(self,url,previousWindow):
        title, price = Scrap.onScrap(url)
        previousWindow.destroy()
        newWindow = Tk()
        newWindow.geometry("300x300")
        newWindow.title("Product Details")
        labelTitle = Label(newWindow, text="Title:", font=("arial", 50, "bold"))
        labelTitle.place(x=5, y=20)

        textTitle = Text(newWindow, height=4, width=41)
        textTitle.place(x=0, y=35)
        textTitle.insert(END, title)
        textTitle.config(state=DISABLED)

        labelPrice = Label(newWindow, text="Price(Rs.):", font=("arial", 50, "bold"))
        labelPrice.place(x=5, y=100)

        textPrice = Text(newWindow, height=2, width=15)
        textPrice.place(x=110, y=100)
        textPrice.insert(END, price)
        textPrice.config(state=DISABLED)
        buttonAdd = Button(newWindow, text="Add Product To List", height=2, width=20,font=("arial",
            50, "bold"), command=lambda : self.onAdd(url, title, price) )
        buttonAdd.place(x=20, y=150)
        buttonAddNew = Button(newWindow, text="Add New Product", height=2, width=22,font=("arial",
            50, "bold"), command=lambda : self.onAddNew(newWindow) )
        buttonAddNew.place(x=20, y=198)

        newWindow.mainloop()






