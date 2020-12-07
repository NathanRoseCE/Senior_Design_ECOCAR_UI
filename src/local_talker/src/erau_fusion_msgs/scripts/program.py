import os
import threading
import tkMessageBox
import video
from tkinter import *
from threading import Thread

def mainExecution():
	pass

def exitFunc():
    root.destroy()

vp = video.VideoPlayer()

root = Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (w, h))
root.configure(background='black', cursor="none")

exitButton = Button(root, text="Exit", command=exitFunc, fg='white', bg='black')
exitButton.place(x=25,y=380)

yeetButton = Button(root, text="hecc", command=vp.videoPlayerPlay, fg='white', bg='black')
yeetButton.place(x=100,y=380)



execute = Thread( target=mainExecution)
execute.setDaemon(True)
execute.start()
root.mainloop()
