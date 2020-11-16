################
# YOU NEED TO RUN 'pip2 install python-vlc' TO RUN NOW
################
import threading
import vlc
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
		self.image = Image.open('../resources/Car1.gif')
		self.hidden=False
		self.master= master
		self.label = Label(self.master) 
	#end  __init__
	
	def update(self, x, y, xPixels, yPixels):
		#ensure proper image is loaded(rn its only cars)
		if not self.hidden:
			temp = self.label
			self.photoImage = ImageTk.PhotoImage(self.image.resize((int(xPixels), int(yPixels)))) 
			self.label = Label(self.master, image=self.photoImage) 
			self.label.place( relx = x, rely = y, anchor='center')
			temp.destroy()
	#end prep
	def hide(self):
		self.hidden = True
		self.label.destroy()
	#end hide
	
	def show(self):
		self.hidden = False
	#end show
	
	def __del__(self):
		self.hide() #Hide, then DIE
	#end __del__
	
class Lane_GUI:
	def __init__(self, master, lanePosition, ros):
		self.data = ros
		self.lanePosition = lanePosition
		self.lastLoadLeft = None
		lastLoadRight = None
		self.imageLeft = None
		self.imageRight = None
		self.hidden= False
		self.master= master
		self.labelLeft = Label(self.master)
		self.labelRight= Label(self.master)
		self.loadImage()
	#end  __init__
	
	def loadImage(self):
		if self.lastLoadLeft != self.data.lanes[self.lanePosition].laneTypeRight:
			if self.data.lanes[self.lanePosition].laneTypeRight == LaneType.LANE_TYPE_DASHED:
				self.imageRight = Image.open('../resources/dashedWhiteLine.png')
			elif self.data.lanes[self.lanePosition].laneTypeRight == LaneType.LANE_TYPE_SOLID:
				self.imageRight = Image.open('../resources/solidWhiteLine.png')
			else: 
				self.imageRight = Image.open('../resources/dashedYellowLine.png')
			self.lastLoadRight = self.data.lanes[self.lanePosition].laneTypeRight
			
		if self.lastLoadLeft != self.data.lanes[self.lanePosition].laneTypeLeft:
			if self.data.lanes[self.lanePosition].laneTypeLeft == LaneType.LANE_TYPE_DASHED:
				self.imageLeft = Image.open('../resources/dashedWhiteLine.png')
			elif self.data.lanes[self.lanePosition].laneTypeLeft == LaneType.LANE_TYPE_SOLID:
				self.imageLeft = Image.open('../resources/solidWhiteLine.png')
			else:
				self.imageLeft = Image.open('../resources/dashedYellowLine.png')
			self.lastLoadLeft= self.data.lanes[self.lanePosition].laneTypeLeft
			
	def update(self, xl, yl, xr, yr,  xPixels, yPixels):
		#ensure proper image is loaded(rn its only dashed yellow)
		if not self.hidden:
			self.loadImage()
			temp = self.labelLeft
			self.photoImageLeft = ImageTk.PhotoImage(self.imageLeft.resize((int(xPixels), int(yPixels)))) 
			self.labelLeft = Label(self.master, image=self.photoImageLeft) 
			self.labelLeft.place( relx = xl, rely = yl, anchor='center')
			temp.destroy()
			
			temp = self.labelRight
			self.photoImageRight = ImageTk.PhotoImage(self.imageRight.resize((int(xPixels), int(yPixels)))) 
			self.labelRight = Label(self.master, image=self.photoImageRight) 
			self.labelRight.place( relx = xr, rely = yr, anchor='center')
			temp.destroy()
	#end prep
	def hide(self):
		self.hidden = True
		self.labelRight.destroy()
		self.labelLeft.destroy()
	#end hide
	
	def show(self):
		self.hidden = False
	#end show
	
	def __del__(self):
		self.hide() #Hide, then DIE
	#end __del__
	
class FrontCarTracker:
	def __init__(self, master, ros, ecoCar, topFrame):
		self.data = ros
		self.master= master
		self.ecoCar = ecoCar
		self.text = StringVar()
		self.label = Label(self.master, text = "Initiliazed")
		self.label.place( relx = 0.5, rely = 0, anchor='nw') 
		self.topFrame = topFrame
		self.hidden = False
	#end  __init__
	
	def update(self):
		#ensure proper image is loaded(rn its only dashed yellow)
		if not self.hidden:
			distance = self.distanceToFrontCar()
			if distance is None:
				text = "None in Front"
			else: 
				text =str(distance)
			#end if
			temp = self.label
			self.label = Label(self.master, text = text)
			self.label.place( relx = 0.5, rely = 0, anchor='nw') 
			temp.destroy()
		#end if
	#end update
			
	def distanceToFrontCar(self):
		carsInLane = []
		obstacles = self.data.obstacles.copy()
		for obstacle in obstacles:
			if obstacles[obstacle].lanePosition == LanePosition.CENTER:
				if obstacles[obstacle].y > 0:
					carsInLane.append(obstacles[obstacle])
			#end if
		#end for
		
		if carsInLane == []:
			return None
		#end if
		
		closestCar = carsInLane[0]
		for car in carsInLane:
			if closestCar.y > car.y:
				closestCar = car
			#end if
		#end for
		
		distance = closestCar.y - closestCar.sizeY/2 - self.ecoCar.sizeY/2
		self.alert(distance)
		return distance
	#end checkCarInFront
	
	def alert(self, distance):
		if distance is None:
			return
		#end if
		
		thresholdValue = self.data.CarSpeed * 0.5
		if distance < thresholdValue:
			self.topFrame.alert()
		else:
			self.topFrame.stopAlert()
		#end if
		
		
	#end checkIfAlert
	def hide(self):
		self.hidden = True
		self.label.destroy()
	#end hide
	
	def show(self):
		self.hidden = False
	#end show
	
	def __del__(self):
		self.hide() #Hide, then DIE
	#end __del__
#end FrontCarTracker
class EcoCar:
	def __init__(self, sizeX, sizeY):
		self.sizeX = sizeX
		self.sizeY = sizeY
	#end init
#end EcoCar
class GUI:

	def hide(self):
		self.EcoCarLabel.destroy()
		self.hidden = True
      
	def show(self):
		self.hidden = False
		
	def toggleLightMode(self):
		if self.darkMode == False:
			self.setDarkMode()
		else:
			self.setLightMode()
		#end if
	#end toggleLightMode
	
	def setDarkMode(self):
		self.darkMode = True
		self.carFrame.config(bg="black")
	#end setDarkMode
	
	def setLightMode(self):
		self.darkMode = False
		self.carFrame.config(bg="white")
    #end setLightMode
    
	def __init__(self, master):
		# set up some vars
		self.xMin = 0.0
		self.xMax = 1.0
		self.yMin = 1.0 
		self.yMax = 0.0
		self.data = ROSData()
		self.hidden = False
		self.obstacleGUIs = {}
		self.laneGUIs = {}
		self.updateSeeDistance()
		
		#set up GUI
		master.update()
		w, h = master.winfo_width(), master.winfo_height()
		self.master = master
		self.topFrame = Frame(master, bg="white", height=h*0.25, width=w*1.0)
		self.topFrame.update()
		self.topFrame.pack(side='top')
		self.topFrameHandler = TopFrameHandler(self.topFrame, self, h*0.25, w*1.0)
		self.carFrame=Frame(master, bg="black", height=h*0.75, width=w*1.0)
		self.carFrame.update()
		self.carFrame.pack(side='bottom')
		self.ecoCar = EcoCar(1, 2)
		self.ECOCarImage = Image.open('../resources/Car2.gif')
		self.EcoCarLabel = Label(self.carFrame) 
		self.updateECOCarImage()
		
		self.frontCarTracker = FrontCarTracker(master, self.data, self.ecoCar, self.topFrameHandler)
		self.darkMode = False
       
	#end __init__
	def update(self):
		if not self.hidden:
			self.updateECOCarImage()
			self.updateObstacles()
			self.updateLanes()
			self.updateFrontCarChecker()
			self.updateSeeDistance()
		#end of
	#end update
	
	def updateSeeDistance(self):
		speed = self.data.CarSpeed
		self.showYDistance = (speed * 0.5) + 10
	#end updateSeeDistance
	
	def updateFrontCarChecker(self):
		self.frontCarTracker.update()
	#end updateFrontCarChecker
	
	def updateObstacles(self):
		currentlyTracked = self.obstacleGUIs.keys()
		obstacleCpy = self.data.obstacles.copy()
		for obstacle in obstacleCpy:
			if obstacle in currentlyTracked:
				currentlyTracked.remove(obstacle)
			else:
				self.obstacleGUIs[obstacle] = Obstacle_GUI(self.carFrame, obstacle)
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
	
	def updateLanes(self):
		trackedLanes = self.laneGUIs.keys()
		laneCpy = self.data.lanes.copy()
		for lane in laneCpy:
			if lane in trackedLanes:
				trackedLanes.remove(lane)
			else:
				self.laneGUIs[lane] = Lane_GUI(self.carFrame, lane, self.data)
			#end if
			lne = self.data.lanes[lane]
			(xl, yl) = self.getGUIPoint( (-lne.laneWidth/2, 0), lane) 
			(xr, yr) = self.getGUIPoint( (lne.laneWidth/2, 0), lane) 
			(xRatio, yRatio) = self.relativeToGUIScale()
			xPixels = int(0.1 * xRatio)
			yPixels = int(self.showYDistance * yRatio)
			self.laneGUIs[lane].update(xl, yl, xr, yr, xPixels, yPixels)
		#end for
		for dissapeared in trackedLanes:
			del self.laneGUIs[dissapeared]
		#end for
	#end updateObstacles
	
	def updateECOCarImage(self):
		if not self.hidden:
			temp = self.EcoCarLabel
			(x, y) = self.getGUIPoint( (0,0), LanePosition.CENTER) 
			(xRatio, yRatio) = self.relativeToGUIScale()
			xPixels = int(self.ecoCar.sizeX * xRatio)
			yPixels = int(self.ecoCar.sizeY * yRatio)
			self.photoImage = ImageTk.PhotoImage(self.ECOCarImage.resize((int(xPixels), int(yPixels)))) 
			self.EcoCarLabel = Label(self.carFrame, image=self.photoImage) 
			self.EcoCarLabel.place( relx = x, rely = y, anchor='center') 
			temp.destroy()
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
		
		noLeftLane = False
		noRightLane = False
		centerWidth = self.data.lanes[LanePosition.CENTER].laneWidth
		xShow = centerWidth
		leftWidth = -1
		rightWidth = -1
		try:
			leftWidth = self.data.lanes[LanePosition.LEFT].laneWidth
			xShow += leftWidth
		except KeyError:
			noLeftLane = True
		#end try
		
		try:
			rightWidth = self.data.lanes[LanePosition.RIGHT].laneWidth
			xShow += rightWidth
		except KeyError:
			noRightLane = True
		#end try
		
		
		#center the image if there are two lanes
		if noLeftLane and not noRightLane:
			x -= (rightWidth + centerWidth)/4
		elif noRightLane and not noLeftLane:
			x += (rightWidth + centerWidth)/4
		#end if
		
		
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
		
		
		laneCenter = 0.0
		centerWidth = self.data.lanes[LanePosition.CENTER].laneWidth
		try:
			leftWidth = self.data.lanes[LanePosition.LEFT].laneWidth
			if lanePosition == LanePosition.LEFT:
				laneCenter = -((centerWidth/2.0) + (leftWidth/2.0))
		except KeyError:
			pass
		#end try
		try:
			rightWidth = self.data.lanes[LanePosition.RIGHT].laneWidth
			if lanePosition == LanePosition.RIGHT:
				laneCenter = (centerWidth/2.0) + (rightWidth/2.0)
		except KeyError:
			pass
		#end try
		
		#end if 
		x += laneCenter
		return (x, y)
	#end translateLaneToRelative
	
	def relativeToGUIScale(self):
		self.carFrame.update()
		w, h = self.carFrame.winfo_width(), self.carFrame.winfo_height()
		
		relativeWidth = self.data.lanes[LanePosition.CENTER].laneWidth
		try:
			leftWidth = self.data.lanes[LanePosition.LEFT].laneWidth
			relativeWidth += leftWidth
		except KeyError:
			noLeftLane = True
		#end try
		
		try:
			rightWidth = self.data.lanes[LanePosition.RIGHT].laneWidth
			relativeWidth += rightWidth
		except KeyError:
			noRightLane = True
		#end try
		
		relativeHeight = self.showYDistance
		
		yRatio = h/relativeHeight
		
		xRatio = w/relativeWidth
		yRatio = abs(yRatio)
		xRatio = abs(xRatio)
		return (xRatio,yRatio)
	
#end GUI

class TopFrameHandler:
	def __init__(self, frame, GUI, height, width):
		self.frame = frame
		self.alerted = False
		self.darkMode = False
		self.gui = GUI
		#self.frame.grid(row=1, column=3, sticky='nsew')
		#self.frame.grid_rowconfigure(0, minsize=100, weight=1)
		#self.frame.grid_columnconfigure(0, minsize=100, weight=1)
		self.frame.pack(fill=None, expand=False)
		self.label = Label(self.frame, text = "test")
		self.button = Button(self.frame, text="Toggle Dark Mode", command = self.gui.toggleLightMode)
		self.button.place(relx=.5, rely=.5, anchor="c")
		#self.button.pack()
	#end __init__
	
	def alert(self):
		self.alerted = True
		self.frame.config(bg="red")
	#end alert
	
	def stopAlert(self):
		self.alerted = False
		self.frame.config(bg="white")
	#end stopAlert
		
			
	def setDarkMode(self):
		self.darkMode = True
		if not self.alerted:
			self.carFrame.config(bg="black")
		#end if
	#end setDarkMode
	
	def setLightMode(self):
		self.darkMode = False
		if not self.alerted:
			self.carFrame.config(bg="white")
		#end if
    #end setLightMode
#end TopFrameHandler
def mainTest():
	time.sleep(5)
	test.hide()
	time.sleep(2)
	test.show()

def videoPlay():
	vidPlayer = vlc.MediaPlayer()
	vidPlayer.set_fullscreen(True)
	video = vlc.Media("../resources/vid.mp4")
	vidPlayer.set_media(video)
	vidPlayer.play()
	time.sleep(0.1)

	while(vidPlayer.is_playing()) == 1:
		time.sleep(0.3)
	vidPlayer.stop()
	
def updateLoop(GUI):
	while True:
		time.sleep(0.1)
		GUI.update()
	#end while
#end updateLoop
if __name__ == '__main__':
	root = Tk()
	w, h = root.winfo_screenwidth(), root.winfo_screenheight()
	frame = Frame(root, bg="black", height=h*1, width=w*0.5)
	frame.pack(  )
	root.geometry("%dx%d+0+0" % (w, h))
	simulator = SimulateData()
	gui = GUI(frame)
	vidButton = Button(root, text="video", command=videoPlay)
	vidButton.place(x=10,y=10)
	#root.bind("<Left>", left)
	#root.bind("<Right>", right)
	#root.bind("<Up>", up)
	#root.bind("<Down>", down)
	test = Thread( target=simulator.twoLaneTest)
	test.setDaemon(True)
	test.start()
	#test = Thread( target=simulator.runCarPassing)
	#test.setDaemon(True)
	#test.start()
	#test2 = Thread( target=simulator.runCarChangeLane)
	#test2.setDaemon(True)
	#test2.start()
	
	test3 = Thread(target=simulator.speedUpEcoCAR)
	test3.setDaemon(True)
	test3.start()
	
	mainLoop = Thread( target=updateLoop, args=(gui,))
	mainLoop.setDaemon(True)
	mainLoop.start()
	
	root.mainloop()

