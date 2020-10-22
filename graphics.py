# Get the tools for graphics
from tkinter import *

# Graphics Setup
baseValue    = 100
windowWidth  = baseValue*3
windowHeight = baseValue*4

root = Tk()
canvas = Canvas(root, width=windowWidth, height=windowHeight)
canvas.pack()

# Shapes (x1, y1, x2, y2)

# Cars (Boxes)
carWidth   = windowWidth*(1/6)
carHeight  = windowHeight*(1/4)

redCarXStart  = windowWidth*(1/2) - carWidth*(1/2)  # Center of X-Axis
redCarYStart  = windowHeight*(2/3)
redCarXEnd    = redCarXStart+carWidth
redCarYEnd    = redCarYStart+carHeight
redCar = canvas.create_rectangle(redCarXStart, redCarYStart, redCarXEnd, redCarYEnd, fill="red")

blackCar = canvas.create_rectangle(redCarXStart, redCarYStart-carHeight*2, redCarXEnd, redCarYEnd-carHeight*2, fill="black")

yellowCar = canvas.create_rectangle(redCarXStart+carWidth*2, redCarYStart, redCarXEnd+carWidth*2, redCarYEnd, fill="yellow")

# Lines

# Information Border
infoBorderYStart = windowHeight*(1/10)
infoBorder = canvas.create_rectangle(0, 0, windowWidth, infoBorderYStart, fill="red")

# Solid Yellow Lines
solidYellowLineLeftXOffest = redCarXStart-carWidth*(1/2)
solidYellowLineLeft = canvas.create_line(solidYellowLineLeftXOffest, infoBorderYStart, solidYellowLineLeftXOffest, windowHeight, fill="yellow")

solidYellowLineRightXOffest = redCarXStart+carWidth*(3/2)
solidYellowLineRight = canvas.create_line(solidYellowLineRightXOffest, infoBorderYStart, solidYellowLineRightXOffest, windowHeight, fill="yellow")

# Pedestrian Image

diameter = carWidth
pedestrianXStart = redCarXStart-carWidth*2
pedestrianYStart = redCarYStart-carHeight*(1/2)-diameter*(1/2)
pedestrian = canvas.create_oval(pedestrianXStart, pedestrianYStart, pedestrianXStart+diameter, pedestrianYStart+diameter)


# Information Text

speed          = canvas.create_text(windowWidth*(1/2), windowHeight*(1/20), text="Speed (MPH):\n"+"242")
redCarDistance = canvas.create_text(redCarXStart+carWidth*(1/2), redCarYStart-carHeight*(1/2), text="Distance (M):\n"+"2")




# Display the graphics
root.mainloop()
