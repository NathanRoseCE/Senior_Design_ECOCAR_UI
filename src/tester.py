from ROSData import *
import time


class SimulateData:
    def __init__(self):
        self.data = ROSData()
        self.data.CarSpeed = 0
    #end __init__
    
    def runCarPassing(self):
        obstacle = Obstacle(0, 0, -50, 0, 0, 6.0, 15.0, BlinkerInfo.BLINKER_INFO_OFF, ObstacleType.CAR, lanePosition = LanePosition.LEFT)
        self.data.obstacles[0] = obstacle
        while obstacle.y < 50:
            obstacle.y += 0.4
            time.sleep(0.1)
        #end for
        del self.data.obstacles[0]
    #end CarPassing  
    
    def speedUpEcoCAR(self):
    	while self.data.CarSpeed < 20:
			self.data.CarSpeed += 0.5
			time.sleep(0.1)
    	#end while    
    #end speedUpEcoCARs
    def setupThreeLanes(self):
        leftLane = Lane(LaneType.LANE_TYPE_DASHED, LaneType.LANE_TYPE_SOLID, LanePosition.LEFT, 10)
        centerLane = Lane(LaneType.LANE_TYPE_DASHED, LaneType.LANE_TYPE_DASHED, LanePosition.CENTER, 10)
        rightLane = Lane(LaneType.LANE_TYPE_SOLID, LaneType.LANE_TYPE_DASHED, LanePosition.RIGHT, 10)
        self.data.lanes[LanePosition.LEFT] = leftLane
        self.data.lanes[LanePosition.CENTER] = centerLane
        self.data.lanes[LanePosition.RIGHT] = rightLane
        print "Three lanes set up"
    #end setupLanes
      
    def setupTwoLanes(self):
        centerLane = Lane(LaneType.LANE_TYPE_DASHED, LaneType.LANE_TYPE_DASHED, LanePosition.CENTER, 10)
        rightLane = Lane(LaneType.LANE_TYPE_SOLID, LaneType.LANE_TYPE_DASHED, LanePosition.RIGHT, 10)
        del self.data.lanes[LanePosition.LEFT]
        self.data.lanes[LanePosition.CENTER] = centerLane
        self.data.lanes[LanePosition.RIGHT] = rightLane
        print "Lanes set up!"
    #end setupLanes
    
    def twoLaneTest(self):
    	self.setupTwoLanes()
    	self.runCarChangeLane()
    	
    def runCarChangeLane(self):
        print "Running Car changing lanes!"
        obstacle = Obstacle(1, 0, -50, 0, 0, 6.0, 15.0, BlinkerInfo.BLINKER_INFO_RIGHT, ObstacleType.TRUCK, lanePosition = LanePosition.CENTER)
        self.data.obstacles[1] = obstacle
        forwardSpeed = 0.25
        sidespeed = 0.2
        while obstacle.y < -25:
			obstacle.y +=forwardSpeed
			time.sleep(0.1)
			
			
        while obstacle.x < self.data.lanes[LanePosition.CENTER].laneWidth/2:
			obstacle.x +=sidespeed
			obstacle.y +=forwardSpeed
			time.sleep(0.1)
        #end for
        obstacle.lanePosition = LanePosition.RIGHT
        obstacle.x = -self.data.lanes[LanePosition.RIGHT].laneWidth/2
        obstacle.blinkerInfo = BlinkerInfo.BLINKER_INFO_OFF
        while obstacle.x < 0:
			obstacle.x +=forwardSpeed
			obstacle.y +=sidespeed
			time.sleep(0.1)
        #end for
        
        while obstacle.y < 15:
			obstacle.y +=forwardSpeed
			time.sleep(0.1)
			
        obstacle.blinkerInfo = BlinkerInfo.BLINKER_INFO_LEFT
        while obstacle.x > -self.data.lanes[LanePosition.CENTER].laneWidth/2:
			obstacle.x -=sidespeed
			obstacle.y +=forwardSpeed
			time.sleep(0.1)
        #end for
        obstacle.lanePosition = LanePosition.CENTER
        obstacle.x = self.data.lanes[LanePosition.CENTER].laneWidth/2
        
        while obstacle.x > 0:
			obstacle.x -=sidespeed
			obstacle.y +=forwardSpeed
			time.sleep(0.1)
			
			
        while obstacle.y < 100:
			obstacle.y +=forwardSpeed
			time.sleep(0.1)
        #end for
        del self.data.obstacles[1]
        print "DONE!"
    #end runCarChangeLane
    
    def carStoppingInForntTest(self):
		print "Car Stopping Test"
		time.sleep(10)
		obstacle = Obstacle(2, 0, -50, 0, 0, 6.0, 15.0, BlinkerInfo.BLINKER_INFO_OFF, ObstacleType.CAR, lanePosition = LanePosition.RIGHT)
		self.data.obstacles[2] = obstacle
    	
		forwardSpeed = 0.25
		sidespeed = 0.2
		while obstacle.y < 10:
			obstacle.y +=forwardSpeed
			time.sleep(0.1)
    	#end while
    	
		obstacle.blinkerInfo = BlinkerInfo.BLINKER_INFO_LEFT
		while obstacle.x > -self.data.lanes[LanePosition.CENTER].laneWidth/2:
			obstacle.x -=sidespeed
			obstacle.y +=forwardSpeed
			time.sleep(0.1)
        #end for
		obstacle.lanePosition = LanePosition.CENTER
		obstacle.x = self.data.lanes[LanePosition.CENTER].laneWidth/2
        
		while obstacle.x > 0:
			obstacle.x -=sidespeed
			obstacle.y +=forwardSpeed
			time.sleep(0.1)
		print "Stopping Car"
		
		while forwardSpeed > 0:
			forwardSpeed -= 0.05
			obstacle.y += forwardSpeed
			time.sleep(0.1)
		#end while
		
		while self.data.CarSpeed > 0:
			self.data.CarSpeed -= 1
			time.sleep(0.1)
		#end while
		
		   	
   	#end carStoppingInFrontTest
#end SimulateData
