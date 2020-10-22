# Get the tools for graphics
from tkinter import *
#from PIL import Image
#from OS import *
import os 

# Graphics Setup
baseValue    = 100
windowWidth  = baseValue*6
windowHeight = baseValue*4

root = Tk()
canvas = Canvas(root, width=windowWidth, height=windowHeight)
canvas.pack()
carWidth   = windowWidth*(1/6)
carHeight  = windowHeight*(1/4)


#loop to stop and start the graphics
lis = [1, 2, 3, 4, 5, 6, 7] 
i = 0
  
while(i > len(lis)):
    # Cars (Boxes)
  

#redCarXStart  = windowWidth*(1/2) - carWidth*(1/2)  # Center of X-Axis
      redCarXStart  = 260  # Center of X-Axis
#redCarYStart  = windowHeight*(2/3)
      redCarYStart  = 125
      redCarXEnd    = redCarXStart+carWidth
      redCarYEnd    = redCarYStart+carHeight
      this_dir = os.path.dirname(__file__) 
      redcar2 = os.path.realpath("{0}/Senior_Design_ECOCAR_UI/Car 1.gif".format(this_dir))
      #redcar2= PhotoImage(file =r"https://github.com/NathanRoseCE/Senior_Design_ECOCAR_UI/raw/feature/GUI/Car 1.gif")
      #redcar2= PhotoImage(file =r"C:\Users\chan9\Desktop\Car 1.gif")
#image = canvas.create_image(50, 50, anchor=NE, image=filename)

#canvas.create_image(redCarXStart, redCarYStart, redCarXEnd, redCarYEnd, image=redcar2,anchor=NW)
      canvas.create_image(redCarXStart, redCarYStart,image=redcar2,anchor=NW)


# Information Border
      infoBorderYStart = windowHeight*(1/10)
      infoBorder = canvas.create_rectangle(0, 0, windowWidth, infoBorderYStart, fill="red")

# Solid Yellow Lines
      solidYellowLineLeftXOffest = redCarXStart-carWidth*(1/2)
      solidYellowLineLeft = canvas.create_line(solidYellowLineLeftXOffest, infoBorderYStart, solidYellowLineLeftXOffest, windowHeight, fill="yellow")
  
      solidYellowLineRightXOffest = redCarXStart+carWidth*(3/2)
      solidYellowLineRight = canvas.create_line(solidYellowLineRightXOffest, infoBorderYStart, solidYellowLineRightXOffest, windowHeight, fill="yellow")

# Pedestrian Image

#diameter=carwidth
#pedestrianXStart = redCarXStart-carWidth*2
#pedestrianYStart = redCarYStart-carHeight*(1/2)-diameter*(1/2)
#pedestrianYStart = redCarYStart-carHeight*(1/2)
#pedestrian= PhotoImage(file =r"C:\Users\chan9\Desktop\SE 300\pedestrian.gif")
#canvas.create_image(pedestrianXStart,pedestrianYStart ,image=pedestrian)


# Information Text

      speed          = canvas.create_text(windowWidth*(1/2), windowHeight*(1/20), text="Speed (MPH):\n"+"242")
      redCarDistance = canvas.create_text(redCarXStart+carWidth*(1/2), redCarYStart-carHeight*(1/2), text="Distance (M):\n"+"2")

      this_dir = os.path.dirname(__file__) 
      blackcar = os.path.realpath("{0}/Senior_Design_ECOCAR_UI/Car 2.gif".format(this_dir))
#blackcar= PhotoImage(file =r"https://github.com/NathanRoseCE/Senior_Design_ECOCAR_UI/raw/feature/GUI/Car 2.gif")
#blackcar= PhotoImage(file =r"C:\Users\chan9\Desktop\Car 2.gif")
#blackCar = canvas.create_image(redCarXStart, redCarYStart-carHeight*2, redCarXEnd, redCarYEnd-carHeight*2, fill="black")

#canvas.create_image(redCarXStart, redCarYStart-carHeight*2, redCarXEnd, redCarYEnd-carHeight*2, image=blackcar,anchor=NW)
      canvas.create_image(redCarXStart, redCarYStart-carHeight*2,image=blackcar,anchor=NW)
  
      #def left(event):
      #x=-30
      #y=0
      #canvas.move(blackcar, x, y)
  
    #def right(event):
      #x=30
      #y=0
      #canvas.move(blackcar, x, y)

    #def up(event):
      #x=0
      #y=-30
      #canvas.move(blackcar, x, y)

    #def down(event):
      #x=0
      #y=-10
      #canvas.move(blackcar, x, y)
      
      root.bind("<Left>",left)
      root.bind("<Right>",right)
      root.bind("<Up>",up)
      root.bind("<Down>",down)
  # Display the graphics
      root.mainloop()

      i += 2
