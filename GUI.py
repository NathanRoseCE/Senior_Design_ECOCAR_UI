
from tkinter import*
#from PIL import Image
#from OS import *

class Test:
    def __init__(self,master,photo,photo2):
        baseValue    = 100
        windowWidth  = baseValue*6
        windowHeight  = baseValue*4
        carWidth   = windowWidth*(1/6)
        carHeight  = windowHeight*(1/4)
        redCarXStart  = 260
        redCarYStart  = 125
        redCarXEnd    = redCarXStart+carWidth
        redCarYEnd    = redCarYStart+carHeight
        self.master=master
        canvas=Canvas(master)
        canvas.grid(row = 600, column = 400)
        self.photo = PhotoImage(file = './Car 1.gif')
        canvas.create_image(redCarXStart,redCarYStart,image=self.photo)
        self.photo2 = PhotoImage(file = './Car 2.gif')
        canvas.create_image(redCarXStart,redCarYStart,image=self.photo2)
        infoBorderYStart = windowHeight*(1/10)
        infoBorder = canvas.create_rectangle(0, 0, windowWidth, infoBorderYStart, fill="red")
        solidYellowLineLeftXOffest = redCarXStart-carWidth*(1/2)
        solidYellowLineLeft = canvas.create_line(solidYellowLineLeftXOffest, infoBorderYStart, solidYellowLineLeftXOffest, windowHeight, fill="yellow")
        solidYellowLineRightXOffest = redCarXStart+carWidth*(3/2)
        solidYellowLineRight = canvas.create_line(solidYellowLineRightXOffest, infoBorderYStart, solidYellowLineRightXOffest, windowHeight, fill="yellow")
        speed          = canvas.create_text(windowWidth*(1/2), windowHeight*(1/20), text="Speed (MPH):\n"+"242")
        redCarDistance = canvas.create_text(redCarXStart+carWidth*(1/2), redCarYStart-carHeight*(1/2), text="Distance (M):\n"+"2")
        
root = Tk()
test = Test(root,600,400)
root.mainloop()

def del_rect():
    canvas.delete(self.photo)

            
