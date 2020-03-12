from tkinter import Tk, Button, BOTH, Entry, Label
from Desktop.main_window.MainWindow import MainWindow

from  Desktop.restart_window.Restart import Restart


class StartWindow :

    def startWindow(self):
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
                "bold"), command = lambda  : mainWindowObj.onMainWindow(urlInput.get(),window))
        buttonScrap.place(x=110, y=190)
        window.mainloop()

if __name__ == '__main__':
    # mainObj = StartWindow()
    # mainObj.startWindow()
    o = Restart()
    o.restartWidow()


#https://www.amazon.in/Lenovo-Legion-Graphics-Windows-81SY00CKIN/dp/B07W6H9YM9/ref=asc_df_B07W6H9YM9/?tag=googleshopdes-21&linkCode=df0&hvadid=396987761655&hvpos=&hvnetw=g&hvrand=2940887166003077401&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9040243&hvtargid=pla-813523435408&psc=1&ext_vrnc=hi
