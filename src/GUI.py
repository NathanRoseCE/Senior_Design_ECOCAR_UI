import threading
import vlc
import time
import sys
from Tkinter import*
from PIL import Image, ImageTk
import multiprocessing
#from PIL import Image
#from OS import *
#sys.path.append("Senior_Design_ECOCAR_UI/ROSData.py")
from threading import Thread
from ROSData import *
from tester import SimulateData      
DIE = False
from enum import Enum

class Obstacle_GUI:
	def __init__(self, master, oid, obstacleType, darkMode = False):
		self.oid = oid
		self.master= master
		self.label = Label(self.master, bd=0) 
		self.obstacleType = obstacleType
		self.blinking = False
		self.blinkerInfo = BlinkerInfo.BLINKER_INFO_UNAVAILABLE
		self.blinkerOn = False
		self.die = False
		self.dead = False
		self.__blinkingThread = Thread(target = self.__blinkBlinkers)
		self.__blinkingThread.setDaemon(True)
		self.__blinkingThread.start()
		self.darkMode = darkMode
		self.filePath = ""
		self.x = 0
		self.y = 0
		self.xPixels = 20
		self.yPixels = 20
		self.update()
	#end  __init__
	def place(self, x, y, xPixels, yPixels, blinkerInfo):
			self.x = x
			self.y = y
			self.xPixels = xPixels
			self.yPixels = yPixels
			self.blinkerInfo = blinkerInfo
			self.update()
	#ned place
	def update(self):
		#ensure proper image is loaded(rn its only cars)
		self.updateImage()
		self.photoImage = ImageTk.PhotoImage(self.image.resize((int(self.xPixels), int(self.yPixels)))) 
		self.label.destroy()
		self.label = Label(self.master, image=self.photoImage, bd=0) 
		self.label.place( relx = self.x, rely = self.y, anchor='center')
	#end prep
	
	def updateImage(self):
		if self.obstacleType == ObstacleType.CAR:
			filePath = "../resources/Car1"
		elif self.obstacleType == ObstacleType.TRUCK:
			filePath = "../resources/Truck"
		elif self.obstacleType == ObstacleType.PEDESTRIAN:
			filePath = "../resources/pedestrian"
		#end if
		
		if self.obstacleType == ObstacleType.CAR or self.obstacleType == ObstacleType.TRUCK:
			if self.blinkerOn == True:
				if self.blinkerInfo == BlinkerInfo.BLINKER_INFO_LEFT:
					filePath += "LightsL"
				elif self.blinkerInfo == BlinkerInfo.BLINKER_INFO_RIGHT:
					filePath += "LightsR"
				elif self.blinkerInfo == BlinkerInfo.BLINKER_INFO_BOTH:
					filePath += "LightsH"
				#end if
			#end if
		#end if
		if not self.darkMode:
			filePath += "L"
		#end if
		filePath += ".png"
		if self.filePath != filePath:
			self.filePath = filePath
			self.image = Image.open(filePath)
		#end if
			
	#end hide
	def cleanUp(self): # call this before del
		self.die = True
		self.label.destroy()
		print "Killing thread"
		while not self.dead:
			time.sleep(0.5)
			print "IM STILL ALIVE"
	#end cleanup
	
	#This runs on its own thread
	def __blinkBlinkers(self):
		while not (self.die or DIE):
			if self.blinkerInfo == BlinkerInfo.BLINKER_INFO_LEFT:
				if self.blinkerOn:
					self.blinkerOn = False
				else:
					self.blinkerOn = True
				#end if
			elif self.blinkerInfo == BlinkerInfo.BLINKER_INFO_RIGHT:
				if self.blinkerOn:
					self.blinkerOn = False
				else:
					self.blinkerOn = True
				#end if
			elif self.blinkerInfo == BlinkerInfo.BLINKER_INFO_BOTH:
				if self.blinkerOn:
					self.blinkerOn = False
				else:
					self.blinkerOn = True
				#end if
			#end if
			time.sleep(0.5)
		#end while
		self.dead = True 
	#end __blinkBlinkers
	
class Lane_GUI:
	def __init__(self, master, lanePosition, ros):
		self.data = ros
		self.lanePosition = lanePosition
		self.lastLoadLeft = None
		self.lastLoadRight = None
		self.imageLeft = None
		self.imageRight = None
		self.master= master
		self.labelLeft = Label(self.master)
		self.labelRight= Label(self.master)
		self.loadImage()
	#end  __init__
	
	def loadImage(self):
		if self.lastLoadRight!= self.data.lanes[self.lanePosition].laneTypeRight:
			if self.data.lanes[self.lanePosition].laneTypeRight == LaneType.LANE_TYPE_DASHED:
				self.imageRight = Image.open('../resources/dashedWhiteLine.png')
			elif self.data.lanes[self.lanePosition].laneTypeRight == LaneType.LANE_TYPE_SOLID:
				self.imageRight = Image.open('../resources/solidWhiteLine.png')
			elif self.data.lanes[self.lanePosition].laneTypeRight == LaneType.LANE_TYPE_NONE:
				self.imageRight = Image.open('../resources/Blackline.png')	
			elif self.data.lanes[self.lanePosition].laneTypeRight == LaneType.LANE_TYPE_ROAD_EDGE:
				self.imageRight = Image.open('../resources/solidWhiteLine.png')
			
			elif self.data.lanes[self.lanePosition].laneTypeRight == LaneType.LANE_TYPE_DOUBLE_LANE_MARK:
				self.imageRight = Image.open('../resources/Doublelane.jpg')
			
			elif self.data.lanes[self.lanePosition].laneTypeRight == LaneType.LANE_TYPE_BOTTS_DOTS:
				self.imageRight = Image.open('../resources/Blackline.png')
			elif self.data.lanes[self.lanePosition].laneTypeRight == LaneType.LANE_TYPE_INVALID:
				self.imageRight = Image.open('../resources/Redline.png')
			
			self.lastLoadRight = self.data.lanes[self.lanePosition].laneTypeRight
			
		if self.lastLoadLeft != self.data.lanes[self.lanePosition].laneTypeLeft:
			if self.data.lanes[self.lanePosition].laneTypeLeft == LaneType.LANE_TYPE_DASHED:
				self.imageLeft = Image.open('../resources/dashedWhiteLine.png')
			elif self.data.lanes[self.lanePosition].laneTypeLeft == LaneType.LANE_TYPE_SOLID:
				self.imageLeft = Image.open('../resources/solidWhiteLine.png')
			elif self.data.lanes[self.lanePosition].laneTypeLeft == LaneType.LANE_TYPE_NONE:
				self.imageRight = Image.open('../resources/Blackline.png')	
				
			elif self.data.lanes[self.lanePosition].laneTypeLeft == LaneType.LANE_TYPE_ROAD_EDGE:
				self.imageRight = Image.open('../resources/solidWhiteLine.png')
			
			
			elif self.data.lanes[self.lanePosition].laneTypeLeft == LaneType.LANE_TYPE_DOUBLE_LANE_MARK:
				self.imageRight = Image.open('../resources/Doublelane.jpg')
			
			
			elif self.data.lanes[self.lanePosition].laneTypeLeft == LaneType.LANE_TYPE_BOTTS_DOTS:
				self.imageRight = Image.open('../resources/Blackline.png')
			
			
			elif self.data.lanes[self.lanePosition].laneTypeLeft == LaneType.LANE_TYPE_INVALID:
				self.imageRight = Image.open('../resources/Redline.png')
			
			self.lastLoadLeft= self.data.lanes[self.lanePosition].laneTypeLeft

		#topBar = PhotoImage(file= r'../resources/topBar.png')
		
			
	def update(self, xl, yl, xr, yr,  xPixels, yPixels):
		#ensure proper image is loaded(rn its only dashed yellow)
		self.loadImage()
		self.photoImageLeft = ImageTk.PhotoImage(self.imageLeft.resize((int(xPixels), int(yPixels))))
		self.labelLeft.destroy() 
		self.labelLeft = Label(self.master, image=self.photoImageLeft, bd=0) 
		self.labelLeft.place( relx = xl, rely = yl,anchor='c')
			
		
		self.photoImageRight = ImageTk.PhotoImage(self.imageRight.resize((int(xPixels), int(yPixels)))) 
		self.labelRight.destroy()
		self.labelRight = Label(self.master, image=self.photoImageRight, bd=0) 
		self.labelRight.place( relx = xr, rely = yr, anchor='c')

	#end prep
	def __del__(self):
		self.labelRight.destroy()
		self.labelLeft.destroy()
	#end __del__
	
class AlertLevel(Enum):
	CLOSE=0
	MID=1
	NONE=2
class FrontCarTracker:
	def __init__(self, master, ecoCar):
		self.master= master
		self.ecoCar = ecoCar
		self.text = StringVar()
		self.lineLabel = Label(self.master)
		self.image = Image.open('../resources/BarToCarInFrontClose.png')
		self.label = Label(self.master)
		self.label.place( relx = 0.5, rely = 0, anchor='nw') 
		self.hidden = False
		self.onScreen = False
		self.alertLevel = AlertLevel.NONE
		self.bg = '#d9d9d9'
		self.textColor = "red"
	#end  __init__
	
	def update(self, x, y, xPixels, yPixels, distance, speed):
		#ensure proper image is loaded(rn its only dashed yellow)
		if not self.hidden:
			distance = distance
			self.alert(distance, speed)
			if (not self.onScreen) and (self.alertLevel != AlertLevel.NONE):		
				self.label = Label(self.master)
				self.lineLabel= Label(self.master)
				self.onScreen = True
			elif self.onScreen and ( self.alertLevel == AlertLevel.NONE):
				self.label.destroy()
				self.lineLabel.destroy()

			if self.alertLevel != AlertLevel.NONE:
				self.photoImage = ImageTk.PhotoImage(self.image.resize((int(xPixels), int(yPixels)))) 
				self.lineLabel.destroy()
				self.lineLabel = Label(self.master, image=self.photoImage, bd=0) 
				self.lineLabel.place( relx = x, rely = y, anchor='center')
				
				
				text =str(distance) + " ft"
				self.label.destroy()
				self.label = Label(self.master, text = text, fg=self.textColor, bg = self.bg)
				self.label.place( relx = x + 0.05, rely = y, anchor='center')
			else:
				self.onScreen = False
		#end if
	#end update
	def alert(self, distance, speed):
		if distance is None:
			return
		#end if
		
		#convert distance to distance in seconds(assumes speed is MPH)
		distanceS = distance / (speed * 5280/3600)
		closeThreshold = 1.0 #less than on second
		midthresholdValue = 2.0 #less than two seconds
		newAlertLevel = self.alertLevel
		if distanceS < closeThreshold:
			newAlertLevel = AlertLevel.CLOSE
		elif distanceS < midthresholdValue:
			newAlertLevel = AlertLevel.MID
		else:
			newAlertLevel = AlertLevel.NONE
		#end if
		
		if self.alertLevel != newAlertLevel:
			self.alertLevel = newAlertLevel
			if self.alertLevel == AlertLevel.MID:
				self.image = Image.open('../resources/BarToCarInFrontMid.png')
				self.textColor="Orange"
			elif self.alertLevel == AlertLevel.CLOSE:
				self.image = Image.open('../resources/BarToCarInFrontClose.png')
				self.textColor="Red"
			#end if
		#end if
		
	#end checkIfAlert
	
	def __del__(self):
		self.label.destroy()
	#end __del__
#end FrontCarTracker
class EcoCar:
	def __init__(self, master, sizeX, sizeY, darkMode = False):
		self.master = master
		self.sizeX = sizeX
		self.sizeY = sizeY
		self.label = Label()
		self.blinkerOn = False
		self.die = False
		self.dead = False
		self.darkMode = darkMode
		self.filePath = ""
		self.place(0, 0, 20, 20, BlinkerInfo.BLINKER_INFO_OFF)
		self.__blinkingThread = Thread(target = self.__blinkBlinkers)
		self.__blinkingThread.setDaemon(True)
		self.__blinkingThread.start()
	#end init
	def place(self, x, y, xPixels, yPixels, blinkerInfo):
			self.x = x
			self.y = y
			self.xPixels = xPixels
			self.yPixels = yPixels
			self.blinkerInfo = blinkerInfo
			self.update()
	#ned place
	
	def update(self):
		self.updateImage()
		self.photoImage = ImageTk.PhotoImage(self.image.resize((int(self.xPixels), int(self.yPixels)))) 
		self.label.destroy()
		self.label = Label(self.master, image=self.photoImage, bd=0) 
		self.label.place( relx = self.x, rely = self.y, anchor='center')
		
	#end prep
	
	def updateImage(self):
		filePath = "../resources/Car2"
		if self.blinkerOn == True:
			if self.blinkerInfo == BlinkerInfo.BLINKER_INFO_LEFT:
				filePath += "LightsL"
			elif self.blinkerInfo == BlinkerInfo.BLINKER_INFO_RIGHT:
				filePath += "LightsR"
			elif self.blinkerInfo == BlinkerInfo.BLINKER_INFO_BOTH:
				filePath += "LightsH"
			#end if
		#end if
		if not self.darkMode:
			filePath += "L"
		#end if
		filePath += ".png"
		if self.filePath != filePath:
			self.filePath = filePath
			self.image = Image.open(filePath)
			print "New image loaded"
		#end if
	
	def __del__(self):
		self.die = True
		print "Killing EcoCar Blinker thread"
		while not self.dead:
			time.sleep(0.5)
			print "IM STILL ALIVE"
	#end __del__
	
	#This runs on its own thread
	def __blinkBlinkers(self):
		while ( not self.die ) and (not DIE):
			if self.blinkerInfo == BlinkerInfo.BLINKER_INFO_LEFT:
				if self.blinkerOn:
					self.blinkerOn = False
				else:
					self.blinkerOn = True
				#end if
			elif self.blinkerInfo == BlinkerInfo.BLINKER_INFO_RIGHT:
				if self.blinkerOn:
					self.blinkerOn = False
				else:
					self.blinkerOn = True
				#end if
			elif self.blinkerInfo == BlinkerInfo.BLINKER_INFO_BOTH:
				if self.blinkerOn:
					self.blinkerOn = False
				else:
					self.blinkerOn = True
				#end if
			#end if
			time.sleep(0.5)
		#end while
		self.dead = True 
	#end __blinkBlinkers
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
		self.ecoCar.darkMode = True
		self.ecoCar.update()
		self.carFrame.config(bg="black")
		self.master.config(bg="black")
		self.topFrameHandler.setDarkMode()
		root.config(bg="black")
		self.frontCarTracker.bg="black"
		for obs in self.obstacleGUIs:
			self.obstacleGUIs[obs].darkMode = True
			self.obstacleGUIs[obs].update()
	#end setDarkMode
	
	def setLightMode(self):
		self.darkMode = False
		self.ecoCar.darkMode = False
		self.ecoCar.update()
		self.carFrame.config(bg="#d9d9d9")
		root.config(bg="#d9d9d9")
		self.frontCarTracker.bg="#d9d9d9"
		self.topFrameHandler.setLightMode()
		for obs in self.obstacleGUIs:
			self.obstacleGUIs[obs].darkMode = False
			self.obstacleGUIs[obs].update()
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
		self.die = False
		
		#set up GUI
		master.update()
		w, h = master.winfo_width(), master.winfo_height()
		self.master = master
		self.topFrame = Frame(master, bg='#d9d9d9', height=h*0.1, width=w*1.0)
		self.topFrame.update()
		self.topFrame.pack(side='top')
		self.topFrameHandler = TopFrameHandler(self.topFrame, self, h*0.25, w*1.0)
		self.carFrame=Frame(master, bg="#d9d9d9", height=h*1, width=w*1.0)
		self.carFrame.update()
		self.carFrame.pack(side='bottom')
		self.ecoCar = EcoCar(self.carFrame, 6, 15)
		self.updateECOCarImage()
		self.frontCarTracker = FrontCarTracker(self.carFrame, self.ecoCar)
		self.darkMode = False
       
	#end __init__
	def __del__():
		self.die = True
		print "deconstructor GUI"
		for obstacleGUI in obstacleGUIs:
			del obstacleGUIs[obstacleGUI]
			
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
		self.showYDistance = (speed * 2) + 30
	#end updateSeeDistance
	
	def updateFrontCarChecker(self):
		distance, closestCar = self.distanceToFrontCar()
		x = None
		y = None
		xPixels = None
		yPixels = None
		if distance is not None:
			(x, y) = self.getGUIPoint( (0, (distance + self.ecoCar.sizeY/2 + closestCar.sizeY/2)/2), LanePosition.CENTER)
			(xRatio, yRatio) = self.relativeToGUIScale()
			yPixels = int(distance * yRatio)
			xPixels = int(5)
		#end if
		self.frontCarTracker.update(x, y, xPixels, yPixels, distance, self.data.CarSpeed)
		del closestCar
	#end updateFrontCarChecker
	
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
			return None, None
		#end if
		
		closestCar = carsInLane[0]
		for car in carsInLane:
			if closestCar.y > car.y and closestCar.y > 0:
				closestCar = car
			#end if
		#end for
		
		distance = closestCar.y - closestCar.sizeY/2 - self.ecoCar.sizeY/2
		return (distance, closestCar)
	def updateObstacles(self):
		currentlyTracked = self.obstacleGUIs.keys()
		obstacleCpy = self.data.obstacles.copy()
		for obstacle in obstacleCpy:
			if obstacle in currentlyTracked:
				currentlyTracked.remove(obstacle)
			else:
				print "New obstacle: " + str(obstacle)
				obstacleType = obstacleCpy[obstacle].obstacleType
				self.obstacleGUIs[obstacle] = Obstacle_GUI(self.carFrame, obstacle, obstacleType)
			#end if
			obs = self.data.obstacles[obstacle]
			blinkerInfo = obs.blinkerInfo
			(x, y) = self.getGUIPoint( (obs.x, obs.y), obs.lanePosition) 
			(xRatio, yRatio) = self.relativeToGUIScale()
			xPixels = int(obs.sizeX * xRatio)
			yPixels = int(obs.sizeY * yRatio)
			self.obstacleGUIs[obstacle].place(x, y, xPixels, yPixels, blinkerInfo)
		#end for
		for dissapeared in currentlyTracked:
			self.obstacleGUIs[dissapeared].cleanUp()
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
			xPixels = int(0.5* xRatio)
			yPixels = int(self.showYDistance*2 * yRatio)
			self.laneGUIs[lane].update(xl, yl, xr, yr, xPixels, yPixels)
		#end for
		for dissapeared in trackedLanes:
			del self.laneGUIs[dissapeared]
		#end for
	#end updateObstacles
	
	def updateECOCarImage(self):
		if not self.hidden:
			(x, y) = self.getGUIPoint( (0,0), LanePosition.CENTER) 
			(xRatio, yRatio) = self.relativeToGUIScale()
			xPixels = int(self.ecoCar.sizeX * xRatio)
			yPixels = int(self.ecoCar.sizeY * yRatio)
			self.ecoCar.place(x, y, xPixels, yPixels, BlinkerInfo.BLINKER_INFO_OFF)
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
		
		relativeHeight = self.showYDistance*2
		
		yRatio = h/relativeHeight
		
		xRatio = w/relativeWidth
		yRatio = abs(yRatio)
		xRatio = abs(xRatio)
		return (xRatio,yRatio)
	
#end GUI

class TopFrameHandler:
	def __init__(self, frame, GUI, height, width):
		self.frame = frame
		self.darkMode = False
		self.gui = GUI
		#self.frame.grid(row=1, column=3, sticky='nsew')
		#self.frame.grid_rowconfigure(0, minsize=100, weight=1)
		#self.frame.grid_columnconfigure(0, minsize=100, weight=1)
		self.frame.pack(fill=None, expand=False)

		self.photoDarkMode = Image.open('../resources/buttonDarkModeL.png')
		self.photo = Image.open('../resources/buttonPlayVideoL.png')
		self.bg='#d9d9d9'
		self.update()
	#end __init__
		
			
	def update(self):
		self.frame.config(bg=self.bg)
		self.photoDarkMode = self.photoDarkMode.resize((150,60), Image.ANTIALIAS)
		self.photoDarkModeImg = ImageTk.PhotoImage(self.photoDarkMode)
		self.button = Button(self.frame, image=self.photoDarkModeImg, command = self.gui.toggleLightMode, bd=0, bg = self.bg, highlightthickness=0)
		self.button.place(relx=.333333, rely=.5, anchor="c")
		
		self.photo = self.photo.resize((150,60), Image.ANTIALIAS)
		self.photoImg =  ImageTk.PhotoImage(self.photo)
		self.vidButton = Button(self.frame, image=self.photoImg, command=videoPlay, bd=0, bg=self.bg, highlightthickness=0)
		self.vidButton.place(relx=.666666, rely=.5, anchor="c")
		
	def setDarkMode(self):
		self.photoDarkMode = Image.open('../resources/buttonDarkMode.png')
		self.photo = Image.open('../resources/buttonPlayVideo.png')
		self.bg='black'
		self.darkMode = True
		self.update()
	#end setDarkMode
	
	def setLightMode(self):
		self.photoDarkMode = Image.open('../resources/buttonDarkModeL.png')
		self.photo = Image.open('../resources/buttonPlayVideoL.png')
		self.bg='#d9d9d9'
		self.darkMode = False
		self.update()
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
	while not DIE:
		time.sleep(0.1)
		GUI.update()
	#end while
#end updateLoop
if __name__ == '__main__':
	root = Tk()
	#root.configure(bg='#d9d9d9')
	w, h = root.winfo_screenwidth(), root.winfo_screenheight()
	frame = Frame(root, bg="black", height=h*1, width=w*0.5)
	frame.pack(  )
	root.geometry("%dx%d+0+0" % (w, h))
	simulator = SimulateData()
	simulator.setupThreeLanes()
	gui = GUI(frame)
	
	
	# test = Thread( target=simulator.twoLaneTest)
	# test.setDaemon(True)
	# test.start()
	test = Thread( target=simulator.runCarPassing)
	test.setDaemon(True)
	test.start()
	test2 = Thread( target=simulator.runCarChangeLane)
	test2.setDaemon(True)
	test2.start()
	
	test3 = Thread(target=simulator.speedUpEcoCAR)
	test3.setDaemon(True)
	test3.start()
	
	mainLoop = Thread( target=updateLoop, args=(gui,))
	mainLoop.start()
	
	root.mainloop()
	DIE = True

