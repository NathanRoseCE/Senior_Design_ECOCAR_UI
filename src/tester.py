from ROSData import *
import time

from src.ROSData import LanePosition, ROSData, Obstacle, BlinkerInfo, ObstacleType, Lane, LaneType


class SimulateData:
    def __init__(self):
        self.data = ROSData()
        self.setupLanes()
    #end __init__
    
    def runCarPassing(self):
        obstacle = Obstacle(0, 0, -10, 0, 0, 1.0, 2.0, BlinkerInfo.BLINKER_INFO_OFF, ObstacleType.CAR, lanePosition = LanePosition.LEFT)
        self.data.obstacles[0] = obstacle
        while obstacle.y < 15:
            obstacle.y += 0.1
            time.sleep(0.1)
        #end for
        del self.data.obstacles[0]
    #end CarPassing  
    
    def setupLanes(self):
        leftLane = Lane(LaneType.LANE_TYPE_DASHED, LaneType.LANE_TYPE_SOLID, LanePosition.LEFT, 3)
        centerLane = Lane(LaneType.LANE_TYPE_DASHED, LaneType.LANE_TYPE_DASHED, LanePosition.CENTER, 3)
        rightLane = Lane(LaneType.LANE_TYPE_SOLID, LaneType.LANE_TYPE_DASHED, LanePosition.RIGHT, 3)
        self.data.lanes[LanePosition.LEFT] = leftLane
        self.data.lanes[LanePosition.CENTER] = centerLane
        self.data.lanes[LanePosition.RIGHT] = rightLane
    #end setupLanes
        
    def runCarChangeLane(self):
        obstacle = Obstacle(1, 0, -5, 0, 0, 1.0, 2.0, BlinkerInfo.BLINKER_INFO_OFF, ObstacleType.CAR, lanePosition = LanePosition.CENTER)
        self.data.obstacles[1] = obstacle
        for i in range(30):
			obstacle.x +=0.05
			obstacle.y +=0.05
			time.sleep(0.1)
        #end for
        obstacle.lanePosition = LanePosition.RIGHT
        obstacle.x = -1.5
        
        for i in range(30):
			obstacle.x +=0.05
			obstacle.y +=0.05
			time.sleep(0.1)
        #end for
        
        while obstacle.y < 3:
			obstacle.y +=0.05
			time.sleep(0.1)
			
        for i in range(30):
			obstacle.x -=0.05
			obstacle.y +=0.05
			time.sleep(0.1)
        #end for
        obstacle.lanePosition = LanePosition.CENTER
        obstacle.x = 1.5
        
        for i in range(30):
			obstacle.x -=0.05
			obstacle.y +=0.05
			time.sleep(0.1)
			
			
        while obstacle.y < 15:
			obstacle.y +=0.05
			time.sleep(0.1)
        #end for
        del self.data.obstacles[1]
    #end runCarChangeLane
#end SimulateData
