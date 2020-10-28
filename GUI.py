
import threading
import time
import sys
from Tkinter import*
#from PIL import Image
#from OS import *
sys.path.append("Senior_Design_ECOCAR_UI/ROSData.py")
from threading import Thread
#from ROSData import *
      
class Test:

    def Hide(self):
        self.canvas.itemconfig(self.img1, state='hidden')
      
    def Show(self):
        self.canvas.itemconfig(self.img1, state='normal')
      
    def __init__(self,master,photo,photo2):
        baseValue    = 200
        windowWidth  = baseValue*6
        windowHeight  = baseValue*4
        carWidth   = windowWidth*(1/6)
        carHeight  = windowHeight*(1/4)
        redCarXStart  = 260
        redCarYStart  = 125
        redCarXEnd    = redCarXStart+carWidth
        redCarYEnd    = redCarYStart+carHeight
        self.master=master
        self.canvas=Canvas(master)
        self.canvas.pack()
        self.canvas.grid(row = 3000, column = 4000)
        self.photo = PhotoImage(file = './cars1.gif')
        self.img1=self.canvas.create_image(redCarXStart,redCarYStart,image=self.photo)
        #canvas.itemconfig(img1, state='hidden')
        #img1 = PhotoImage(file = './cars1.gif')
        #canvas.create_image(redCarXStart, redCarYStart,image=img1)   
        blackCar = PhotoImage(file = './car 2.gif')
        self.canvas.create_image(redCarXStart, redCarYStart-carHeight*2,image=blackCar)
        #canvas.itemconfigure(id, state='hidden')
        #canvas.delete(img1)
        #self.photo = PhotoImage(file = './car 2.gif')
        #canvas.create_image(redCarXEnd,redCarYEnd,image=self.photo)
        infoBorderYStart = windowHeight*(1/10)
        infoBorder = self.canvas.create_rectangle(0, 0, windowWidth, infoBorderYStart, fill="green")
        solidYellowLineLeftXOffest = redCarXStart-carWidth*(1/2)
        solidYellowLineLeft = self.canvas.create_line(solidYellowLineLeftXOffest, infoBorderYStart, solidYellowLineLeftXOffest, windowHeight, fill="black")
        solidYellowLineRightXOffest = redCarXStart+carWidth*(3/2)
        solidYellowLineRight = self.canvas.create_line(solidYellowLineRightXOffest, infoBorderYStart, solidYellowLineRightXOffest, windowHeight, fill="black")
        speed          = self.canvas.create_text(windowWidth*(1/2), windowHeight*(1/20), text="Speed (MPH):\n"+"242")
        redCarDistance = self.canvas.create_text(redCarXStart+carWidth*(1/2), redCarYStart-carHeight*(1/2), text="Distance (M):\n"+"2")
        
    #def run():
     #   x=-10
      #  y=0
       # self.canvas.move(img1,x,y)
       # x=10
       # y=0
       # self.canvas.move(img1,x,y)
       # x= 0
       # y=-10
       # self.canvas.move(img1,x,y)
       # x= 0
       # y=10
       # self.canvas.move(img1,x,y)
          

root = Tk()
test = Test(root,76000,14000)
#root.bind("<Left>", left)
#root.bind("<Right>", right)
#root.bind("<Up>", up)
#root.bind("<Down>", down)
execute = Thread( target=root.mainloop)
execute.setDaemon(True)
execute.start()
time.sleep(5)
test.Hide()
time.sleep(2)
test.Show()
root.mainloop()






		

            
