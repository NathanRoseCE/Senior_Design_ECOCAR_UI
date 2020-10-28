from ROSData import *
import time


class SimulateData:
    def __init__(self):
        self.data = ROSData()
        self.setupLanes()
    #end __init__
    
    def runCarPassing(self):
        obstacle = Obstacle(0, 0, -10, 0, 0, 5.0, 7.0, BlinkerInfo.BLINKER_INFO_OFF, ObstacleType.CAR)
        ROSData.obstacles[0] = obstacle
        for i in range(200):
            obstacle.y += 0.1
            time.sleep(0.1)
        #end for
    #end CarPassing  
    
    def setupLanes(self):
        leftLane = Lane(LaneType.LANE_TYPE_SOLID, LaneType.LANE_TYPE_SOLID, anePosition.LEFT, 10)
        centerLane = Lane(LaneType.LANE_TYPE_SOLID, LaneType.LANE_TYPE_SOLID, LanePosition.CENTER, 10)
        rightLane = Lane(LaneType.LANE_TYPE_SOLID, LaneType.LANE_TYPE_SOLID, LanePosition.RIGHT, 10)
        ROSData.lanes[LanePosition.LEFT] = leftLane
        ROSData.lanes[LanePosition.CENTER] = centerLane
        ROSData.lanes[LanePosition.RIGHT] = rightLane
    #end setupLanes
        
    def runCarChangeLane(self):
        obstacle = Obstacle(0, 0, 10, 0, 0, 5.0, 7.0, BlinkerInfo.BLINKER_INFO_OFF, ObstacleType.CAR)
        ROSData.obstacles[0] = obstacle
        for i in range(200):
            obstacle.y += 0.1
            time.sleep(0.1)
        #end for
    #end runCarChangeLane
#end SimulateData
