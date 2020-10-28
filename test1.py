import os


from tkinter import *
import video

def mainExecution():
	pass

def exitFunc():
    root.destroy()


vp = video.VideoPlayer()

root = Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (w, h))
root.configure(background='black')

exitButton = Button(root, text="Exit", command=exitFunc, fg='white', bg='black')
exitButton.place(x=25,y=380)

yeetButton = Button(root, text="vid", command=vp.videoPlayerPlay, fg='white', bg='black')
yeetButton.place(x=100,y=380)

root.mainloop()
