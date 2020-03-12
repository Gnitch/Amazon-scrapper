from tkinter import DISABLED, Tk, Label, Text, END, Button
from Desktop.scrap.Scrap import Scrap
from  Desktop.restart_window.AddToList import Save

class MainWindow :

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
        saveObj = Save()
        buttonAdd = Button(newWindow, text="Add To List", height=2, width=12,font=("arial",
            50, "bold"), command=lambda : saveObj.onAdd(url, title, price) )
        buttonAdd.place(x=110, y=190)
        newWindow.mainloop()






