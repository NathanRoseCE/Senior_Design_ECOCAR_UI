import os
import threading
import tkMessageBox
from Tkinter import *
from threading import Thread

def mainExecution():


def exitFunc():
    root.destroy()


root = Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (w, h))
root.configure(background='black', cursor="none")

exitButton = Button(root, text="Exit", command=exitFunc, font=('Spantaran', 18), fg='white', bg='black')
exitButton.place(x=25,y=380)


execute = Thread( target=mainExecution)
execute.setDaemon(True)
execute.start()
root.mainloop()
