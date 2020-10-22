
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
class Obstacle:
	def __init__(   self, oid=0, x=0.0, y=0.0, dx=0.0, dy=0.0, sizeX=0.0, sizeY=0.0, 
                    blinkerInfo=BlinkerInfo.BLINKER_INFO_UNAVAILABLE, obstacleType=ObstacleType.UNKNOWN ):
		self.oid = oid
		self.x = x
		self.y = y
		self.dx = dx
		self.dy = dy
		self.sizeY=sizeY
		self.sizeX=sizeX
		self.blinkerInfo=blinkerInfo
		self.obstacleType = obstacleType
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
	def __init__(	self, laneType=LaneType.LANE_TYPE_NONE, curvature_offset = 0.0,
					position_parameter=0.0, curvature_parameter=0.0):
		self.laneType = lane_type
		self.position_parameter = position_parameter
		self.curvature_parameter = curvature_parameter
		self.curavure_offset = curvature_offset
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
		self.lanes = [] 		#List of all detected lanes
		self.ACCSpeed = 0.0		#Current Speed ACC is set to
	#end __init__
#end ROSData
