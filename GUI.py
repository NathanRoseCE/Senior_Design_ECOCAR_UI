
import threading
import time
import sys
from Tkinter import*
from PIL import Image, ImageTk
#from PIL import Image
#from OS import *
sys.path.append("Senior_Design_ECOCAR_UI/ROSData.py")
from threading import Thread
from ROSData import *
from tester import SimulateData      

class Obstacle_GUI:
	def __init__(self, master, oid):
		self.oid = oid
		self.image = Image.open('./Car1.gif')
		self.hidden=False
		self.master= master
		self.label = Label(self.master)
	#end  __init__
	
	def update(self, x, y, xPixels, yPixels):
		#ensure proper image is loaded(rn its only cars)
		if not self.hidden:
			self.label.destroy()
			self.photoImage = ImageTk.PhotoImage(self.image.resize((int(xPixels), int(yPixels)))) 
			self.label = Label(self.master, image=self.photoImage) 
			self.label.place( relx = x, rely = y, anchor='center')
		pass
	#end prep
	def hide():
		self.hidden = True
		self.label.destroy()
	#end hide
	
	def show():
		self.hidden = False
	#end show
	
def Lane_GUI:
	def __init__(self, master, lanePosition):
		self.lanePosition = lanePosition
		self.image = Image.open('./Car1.gif')
		self.hidden=False
		self.master= master
		self.label = Label(self.master)
	#end  __init__
	
	def update(self, x, y, xPixels, yPixels):
		#ensure proper image is loaded(rn its only cars)
		if not self.hidden:
			self.label.destroy()
			self.photoImage = ImageTk.PhotoImage(self.image.resize((int(xPixels), int(yPixels)))) 
			self.label = Label(self.master, image=self.photoImage) 
			self.label.place( relx = x, rely = y, anchor='center')
		pass
	#end prep
	def hide():
		self.hidden = True
		self.label.destroy()
	#end hide
	
	def show():
		self.hidden = False
	#end show
class GUI:

	def hide(self):
		self.EcoCarLabel.destroy()
		self.hidden = True
      
	def show(self):
		self.hidden = False
      
	def __init__(self, master, xMin, xMax, yMin, yMax, showYDistance = 10):
		# set up some vars
		self.xMin = xMin
		self.xMax = xMax
		self.yMin = yMin 
		self.yMax = yMax
		self.showYDistance = showYDistance
		self.data = ROSData()
		self.hidden = False
		self.obstacleGUIs = {}
		
		#set up canvas
		self.master=master
		self.canvas=Canvas(master)
		self.canvas.pack()
    	#display ecoCar
		self.ECOCarImage = Image.open('./Car2.gif')
		self.EcoCarLabel = Label(self.master) 
		self.updateECOCarImage()
    	
    	#OLD
		baseValue    = 1000
		windowWidth  = baseValue*6
		windowHeight  = baseValue*4
		carWidth   = windowWidth*(1/6)
		carHeight  = windowHeight*(1/4)
		redCarXStart  = 260
		redCarYStart  = 125
		redCarXEnd    = redCarXStart+carWidth
		redCarYEnd    = redCarYStart+carHeight
       
       
        
        #set up cars
#		self.photo = PhotoImage(file = './cars1.gif')
#		self.img1=self.canvas.create_image(redCarXStart,redCarYStart,image=self.photo)
#		blackCar = PhotoImage(file = './Car2.gif')
#		self.canvas.create_image(redCarXStart, redCarYStart-carHeight*2,image=blackCar)
#		infoBorderYStart = windowHeight*(1/10)
#		infoBorder = self.canvas.create_rectangle(0, 0, windowWidth, infoBorderYStart, fill="green")
#		solidYellowLineLeftXOffest = redCarXStart-carWidth*(1/2)
#		solidYellowLineLeft = self.canvas.create_line(solidYellowLineLeftXOffest, infoBorderYStart, solidYellowLineLeftXOffest, windowHeight, fill="black")
#		solidYellowLineRightXOffest = redCarXStart+carWidth*(3/2)
#		solidYellowLineRight = self.canvas.create_line(solidYellowLineRightXOffest, infoBorderYStart, solidYellowLineRightXOffest, windowHeight, fill="black")
#		speed          = self.canvas.create_text(windowWidth*(1/2), windowHeight*(1/20), text="Speed (MPH):\n"+"242")
#		redCarDistance = self.canvas.create_text(redCarXStart+carWidth*(1/2), redCarYStart-carHeight*(1/2), text="Distance (M):\n"+"2")
	#end __init__
	def update(self):
		if not self.hidden:
			self.updateECOCarImage()
			self.updateObstacles()
		#end of
	#end update
	
	def updateObstacles(self):
		currentlyTracked = self.obstacleGUIs.keys()
		for obstacle in self.data.obstacles:
			if obstacle in currentlyTracked:
				currentlyTracked.remove(obstacle)
			else:
				self.obstacleGUIs[obstacle] = Obstacle_GUI(self.master, obstacle)
			#end if
			obs = self.data.obstacles[obstacle]
			(x, y) = self.getGUIPoint( (obs.x, obs.y), obs.lanePosition) 
			(xRatio, yRatio) = self.relativeToGUIScale()
			xPixels = int(obs.sizeX * xRatio)
			yPixels = int(obs.sizeY * yRatio)
			self.obstacleGUIs[obstacle].update(x, y, xPixels, yPixels)
		#end for
		for dissapeared in currentlyTracked:
			del self.obstacleGUIs[dissapeared]
		#end for
	#end updateObstacles
	
	def updateECOCarImage(self):
		if not self.hidden:
			self.EcoCarLabel.destroy()
			(x, y) = self.getGUIPoint( (0,0), LanePosition.CENTER) 
			(xRatio, yRatio) = self.relativeToGUIScale()
			xPixels = int(1 * xRatio)
			yPixels = int(2 * yRatio)
			self.photoImage = ImageTk.PhotoImage(self.ECOCarImage.resize((int(xPixels), int(yPixels)))) 
			self.EcoCarLabel = Label(self.master, image=self.photoImage) 
			self.EcoCarLabel.place( relx = x, rely = y, anchor='center') 
			#self.EcoCarLabel.pack()
	#end setupECOCarImage
	
	def getGUIPoint(self, laneCoordinates, lanePosition):
		relativePos =  self.translateLaneToRelative(laneCoordinates, lanePosition)
		return self.translateRelativeToGUI(relativePos)
	#end getGUIPoint
	
	def translateRelativeToGUI(self, relativePos):
		(x, y) = relativePos
		
		yRatio = (self.yMax - self.yMin)/( self.showYDistance * 2)
		y *= yRatio
		y += self.yMin
		
		
		leftWidth = self.data.lanes[LanePosition.LEFT].laneWidth
		centerWidth = self.data.lanes[LanePosition.CENTER].laneWidth
		rightWidth = self.data.lanes[LanePosition.RIGHT].laneWidth
		xShow = leftWidth + rightWidth + centerWidth
		xRatio = (self.xMax - self.xMin)/(xShow)
		x *= xRatio
		x += self.xMin
		
		yMid = (self.yMax - self.yMin)/2
		xMid = (self.xMax - self.xMin)/2
		x += xMid
		y += yMid
		
		return (x,y)
	#end translateRelativeToGUI
	
	def translateLaneToRelative(self, laneCoordinates, lanePosition):
		(x, y) = laneCoordinates
		#TODO account for 2 lane road
		leftWidth = self.data.lanes[LanePosition.LEFT].laneWidth
		centerWidth = self.data.lanes[LanePosition.CENTER].laneWidth
		rightWidth = self.data.lanes[LanePosition.RIGHT].laneWidth
		
		laneCenter = 0.0
		if lanePosition == LanePosition.LEFT:
			laneCenter = -((centerWidth/2.0) + (leftWidth/2.0))
		elif lanePosition == LanePosition.RIGHT:
			laneCenter = (centerWidth/2.0) + (rightWidth/2.0)
		#end if 
		x += laneCenter
		return (x, y)
	#end translateLaneToRelative
	
	def relativeToGUIScale(self):
		w, h = self.master.winfo_screenwidth(), self.master.winfo_screenheight()
		
		leftWidth = self.data.lanes[LanePosition.LEFT].laneWidth
		centerWidth = self.data.lanes[LanePosition.CENTER].laneWidth
		rightWidth = self.data.lanes[LanePosition.RIGHT].laneWidth
		relativeWidth = leftWidth + centerWidth + rightWidth
		relativeHeight = self.showYDistance
		
		yRatio = h/relativeHeight
		
#		leftWidth = self.data.lanes[LanePosition.LEFT].laneWidth
#		centerWidth = self.data.lanes[LanePosition.CENTER].laneWidth
#		rightWidth = self.data.lanes[LanePosition.RIGHT].laneWidth
#		xShow = leftWidth + rightWidth + centerWidth
		xRatio = w/relativeWidth
		yRatio = abs(yRatio)
		xRatio = abs(xRatio)
		return (xRatio,yRatio)
	
#end GUI
def mainTest():
	time.sleep(5)
	test.hide()
	time.sleep(2)
	test.show()
	
def updateLoop(GUI):
	while True:
		time.sleep(0.1)
		GUI.update()
	#end while
#end updateLoop
if __name__ == '__main__':
	root = Tk()
	w, h = root.winfo_screenwidth(), root.winfo_screenheight()
	root.geometry("%dx%d+0+0" % (w, h))
	simulator = SimulateData()
	gui = GUI(root, 0, 1.0, 1.0, 0)
	#root.bind("<Left>", left)
	#root.bind("<Right>", right)
	#root.bind("<Up>", up)
	#root.bind("<Down>", down)
	#test = Thread( target=simulator.runCarPassing)
	#test.setDaemon(True)
	#test.start()
	test2 = Thread( target=simulator.runCarChangeLane)
	test2.setDaemon(True)
	test2.start()
	test3 = Thread( target=updateLoop, args=(gui,))
	test3.setDaemon(True)
	test3.start()
	
	root.mainloop()

