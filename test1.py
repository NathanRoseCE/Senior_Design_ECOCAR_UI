import os

import threading
from threading import Thread
from tkinter import *
import video
root = Tk()
def mainExecution():
	root = Tk()
	print("HMM")
	vp = video.VideoPlayer()
	w, h = root.winfo_screenwidth(), root.winfo_screenheight()
	root.overrideredirect(1)
	root.geometry("%dx%d+0+0" % (w, h))
	root.configure(background='black')

	exitButton = Button(root, text="Exit", command=exitFunc, fg='white', bg='black')
	exitButton.place(x=25,y=380)

	yeetButton = Button(root, text="vid", command=vp.videoThread, fg='white', bg='black')
	yeetButton.place(x=100,y=380)

	root.mainloop()

def exitFunc():
    root.destroy()



print("1")

execute = Thread(target=mainExecution)
print("1")
#execute.setDaemon(True)
print("1")
execute.start()

