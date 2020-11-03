
from enum import Enum

class ObstacleType(Enum):
	UNKNOWN 	= 0
	CAR 		= 1
	TRUCK 		= 2
	PEDESTRIAN 	= 3
#end Obstacle_Type
class BlinkerInfo(Enum):
    BLINKER_INFO_UNAVAILABLE = 0
    BLINKER_INFO_OFF = 1
    BLINKER_INFO_LEFT = 2
    BLINKER_INFO_RIGHT = 3
    BLINKER_INFO_BOTH = 4  
  #end BlinkerInfo
class LanePosition(Enum):
    UNKNOWN = 0
    LEFT = 1
    CENTER = 2
    RIGHT = 3
#end LanePosition
class Obstacle:
	def __init__(   self, oid=0, x=0.0, y=0.0, dx=0.0, dy=0.0, sizeX=0.0, sizeY = 0.0, 
                    blinkerInfo=BlinkerInfo.BLINKER_INFO_UNAVAILABLE, obstacleType=ObstacleType.UNKNOWN,
                    lanePosition = LanePosition.UNKNOWN):
		self.oid = oid
		self.x = float(x)
		self.y = float(y)
		
		self.dx = float(dx)
		self.dy = float(dy)
		self.sizeX=float(sizeX)
		self.sizeY=float(sizeY)
        
		self.blinkerInfo=blinkerInfo
        
		self.obstacleType = obstacleType
		self.lanePosition = lanePosition
	#end __init__ non-default
#end Obstacle

class LaneType(Enum):
	LANE_TYPE_DASHED = 0
	LANE_TYPE_SOLID = 1
	LANE_TYPE_NONE = 2
	LANE_TYPE_ROAD_EDGE = 3
	LANE_TYPE_DOUBLE_LANE_MARK = 4
	LANE_TYPE_BOTTS_DOTS = 5
	LANE_TYPE_INVALID = 6
#end LaneType


    
class Lane:
	def __init__(	self, laneTypeRight=LaneType.LANE_TYPE_NONE, laneTypeLeft=LaneType.LANE_TYPE_NONE, 
                    lanePosition = LanePosition.UNKNOWN, laneWidth = 0.0):
		self.laneTypeRight = laneTypeRight
		self.laneTypeLeft = laneTypeLeft
		self.lanePosition = lanePosition
		self.laneWidth = float(laneWidth)
	#end __init__
#end Lane
class _Singleton(type):
	__INSTANCE = None
	def __call__(cls, *args, **kwargs):
		if cls.__INSTANCE is None:
			cls.__INSTANCE = super(_Singleton, cls).__call__(*args, **kwargs);
		#end if
		return cls.__INSTANCE
	#end call
#end singleton
	
class ROSData(object):
	__metaclass__ = _Singleton
	def __init__(self):
		self.obstacles = {} 	#key is the object id, object is an Obstacle instance
		self.lanes = {}         #key is LanePosition, object is Lane instance
		self.ACCSpeed = 0.0		#Current Speed ACC is set to
	#end __init__
#end ROSData
