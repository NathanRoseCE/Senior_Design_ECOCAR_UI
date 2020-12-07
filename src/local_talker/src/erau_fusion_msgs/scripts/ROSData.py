
from enum import Enum
from listener import msg
from listener import mes_tracked_veh_object

class classification(Enum):
	UNKNOWN 	= 0
	CAR 		= 1
	TRUCK 		= 2
	PEDESTRIAN 	= 3
#end Obstacle_Type
class blinkerInfo(Enum):
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
#end lane

class Obstacle:
	def __init__(   self, oid, x, y, dx, dy, sizeX, sizeY, blinker_info, classification, lane):
		mes_tracked_veh_object.id = oid
		mes_tracked_veh_object.object.x = x
		mes_tracked_veh_object.object.y = y
		mes_tracked_veh_object.object.dx = dx
		mes_tracked_veh_object.object.dy = dy
		mes_tracked_veh_object.object.sizeX = sizeX
		mes_tracked_veh_object.object.sizeY = sizeY
		mes_tracked_veh_object.object.blinker_info = blinker_info
		mes_tracked_veh_object.object.classification = classification
		mes_tracked_veh_object.lane = lane

		self.id = mes_tracked_veh_object.id
		self.x = mes_tracked_veh_object.object.x
		self.y = mes_tracked_veh_object.object.y
		
		self.dx = mes_tracked_veh_object.object.dx
		self.dy = mes_tracked_veh_object.object.dy
		self.sizeX= mes_tracked_veh_object.object.sizeX
		self.sizeY= mes_tracked_veh_object.object.sizeY
        
		self.blinker_info= mes_tracked_veh_object.object.blinker_info
        
		self.classification = mes_tracked_veh_object.object.classification
		self.lane = mes_tracked_veh_object.lane

		print ("Oject %u \nPosition x: %f \nPosition y: %f \nPosition dx: %f \nPosition dy: %f \nCar Size X: %f \nCar Size Y: %f \nBlinker info: %s \nClassification: %s\nLane: %s\n\n" % (self.id, self.x, self.y, self.dx, self.dy, self.sizeX, self.sizeY, self.blinker_info, self.classification, self.lane))
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
	def __init__(	self, lane_type_Right, lane_type_Left, lanePosition, laneWidth):
		msg.lane_type_Left = lane_type_Left
		msg.lane_type_Right = lane_type_Right
		msg.lanePosition = lanePosition
		msg.laneWidth = laneWidth

		self.lane_type_Left = msg.lane_type_Left
		self.lane_type_Right = msg.lane_type_Right
		self.lane = msg.lanePosition
		self.laneWidth = msg.laneWidth
		print ("Lane Type Left: %s \nLane Type Right: %s \nLane Positon: %s \nLane Width: %u\n" % (self.lane_type_Left, self.lane_type_Right, self.lane, self.laneWidth))
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
		self.CarSpeed = 0.0
	#end __init__
#end ROSData
