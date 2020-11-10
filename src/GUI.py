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
		self.image = Image.open('../resources/Car1.png')
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

		#topBar = PhotoImage(file= r'../resources/topBar.png')
		
			
	def update(self, xl, yl, xr, yr,  xPixels, yPixels):
		#ensure proper image is loaded(rn its only dashed yellow)
		if not self.hidden:
			self.loadImage()
			self.labelLeft.destroy()
			self.photoImageLeft = ImageTk.PhotoImage(self.imageLeft.resize((int(xPixels), int(yPixels)))) 
			self.labelLeft = Label(self.master, image=self.photoImageLeft) 
			self.labelLeft.place( relx = xl, rely = yl, anchor='center')
			
			self.labelRight.destroy()
			self.photoImageRight = ImageTk.PhotoImage(self.imageRight.resize((int(xPixels), int(yPixels)))) 
			self.labelRight = Label(self.master, image=self.photoImageRight) 
			self.labelRight.place( relx = xr, rely = yr, anchor='center')

			




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
	def __init__(self, master, ros, ecoCar):
		self.data = ros
		self.master= master
		self.ecoCar = ecoCar
		self.text = StringVar()
		self.label = Label(self.master, text = "Initiliazed")
		self.label.place( relx = 0.5, rely = 0, anchor='nw') 
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
			self.label.destroy()
			self.label = Label(self.master, text = text)
			self.label.place( relx = 0.5, rely = 0, anchor='nw') 
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
		return distance
	#end checkCarInFront
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
		self.laneGUIs = {}
		
		#set up GUI
		self.master=master
		self.ecoCar = EcoCar(1, 2)
		self.ECOCarImage = Image.open('../resources/Car2.png')
		self.EcoCarLabel = Label(self.master) 
		self.updateECOCarImage()

		#self.topBar = Image.open('../resources/topBar.png')
		#root.create_image(20,20, anchor=NW, image=self.topBar)

		self.frontCarTracker = FrontCarTracker(master, self.data, self.ecoCar)
       
	#end __init__
	def update(self):
		if not self.hidden:
			self.updateECOCarImage()
			self.updateObstacles()
			self.updateLanes()
			self.updateFrontCarChecker()
		#end of
	#end update
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
	
	def updateLanes(self):
		trackedLanes = self.laneGUIs.keys()
		laneCpy = self.data.lanes.copy()
		for lane in laneCpy:
			if lane in trackedLanes:
				trackedLanes.remove(lane)
			else:
				self.laneGUIs[lane] = Lane_GUI(self.master, lane, self.data)
			#end if
			lne = self.data.lanes[lane]
			(xl, yl) = self.getGUIPoint( (-lne.laneWidth/2, 0), lane) 
			(xr, yr) = self.getGUIPoint( (lne.laneWidth/2, 0), lane) 
			(xRatio, yRatio) = self.relativeToGUIScale()
			xPixels = int(0.1 * xRatio)
			yPixels = int(self.showYDistance*2 * yRatio)
			self.laneGUIs[lane].update(xl, yl, xr, yr, xPixels, yPixels)
		#end for
		for dissapeared in trackedLanes:
			del self.laneGUIs[dissapeared]
		#end for
	#end updateObstacles
	
	def updateECOCarImage(self):
		if not self.hidden:
			self.EcoCarLabel.destroy()
			(x, y) = self.getGUIPoint( (0,0), LanePosition.CENTER) 
			(xRatio, yRatio) = self.relativeToGUIScale()
			xPixels = int(self.ecoCar.sizeX * xRatio)
			yPixels = int(self.ecoCar.sizeY * yRatio)
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
		self.master.update()
		w, h = self.master.winfo_height(), self.master.winfo_height()
		
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
	root.configure(bg='#d9d9d9')
	w, h = root.winfo_screenwidth(), root.winfo_screenheight()
	frame = Frame(root, bg="black", height=h*1, width=w*0.5)
	frame.pack(  )
	root.geometry("%dx%d+0+0" % (w, h))
	simulator = SimulateData()
	gui = GUI(frame, 0.0, 1.0, 1.0, 0.0)
	#photo = PhotoImage(file = r'../resources/button1Test.png')
	topbarimg = Image.open('../resources/topBar2.png')
	topbarimg = topbarimg.resize((2000,75),Image.ANTIALIAS)
	topb = ImageTk.PhotoImage(topbarimg)
	labelTopBar = Label(root, image=topb)
	labelTopBar.place(x=0,y=0)


	photo = Image.open('../resources/button1Test.png')
	photo = photo.resize((150,60), Image.ANTIALIAS)
	photoImg =  ImageTk.PhotoImage(photo)
	vidButton = Button(root, image = photoImg, command=videoPlay, bd = 0)
	vidButton.place(x=0,y=0)

	

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
	mainLoop = Thread( target=updateLoop, args=(gui,))
	mainLoop.setDaemon(True)
	mainLoop.start()
	
	root.mainloop()

