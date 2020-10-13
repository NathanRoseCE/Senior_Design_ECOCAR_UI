
from enum import Enum

class ObstacleType(Enum):
	UNKNOWN 	= 0
	CAR 		= 1
	TRUCK 		= 2
	PEDESTRIAN 	= 3
#end Obstacle_Type

class Obstacle:
	def __init__(self, oid=0, x=0.0, y=0.0, dx=0.0, dy=0.0, obstacleType=ObstacleType.UNKNOWN):
		self.oid = oid
		self.x = x
		self.y = y
		
		self.dx = dx
		self.dy = dy
		
		self.obstacleType = obstacleType
	#end __init__ non-default
	
	def updatePosition(self, dt):
		# Updates position between readings
		self.x = self.x + (self.dx * dt)
		self.y = self.y + (self.dy * dt)
	#end updatePosition
	
#end Obstacle

class LaneConfidence(Enum):
	LANE_CONFIDENCE_NONE = 0
	LANE_CONFIDENCE_LOW = 1
	LANE_CONFIDENCE_MED = 2
	LANE_CONFIDENCE_HIGH = 3
#end Lane_Confidence

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
	def __init__(	self, laneType=LaneType.LANE_TYPE_NONE, quality=LaneConfidence.LANE_CONFIDENCE_NONE,
					modelDegree=0, position_parameter_c0=0.0, curvature_parameter_c2=0.0,
					curvature_derivative_parameter_c3=0.0, marking_width=0.0, heading_angle_parameter_c1=0.0,
					view_range=0.0, view_range_availability=False):
		self.laneType = lane_type
		self.quality = quality
		self.model_degree = modelDegree
		self.position_parameter_c0 = position_parameter_c0
 		self.curvature_parameter_c2 = curvature_parameter_c2
		self.curvature_derivative_parameter_c3 = curvature_derivative_parameter_c3
		self.marking_width = marking_width
		self.heading_angle_parameter_c1 = heading_angle_parameter_c1
		self.view_range = view_range
		self.view_range_availability = view_range_availability
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
		self.lanes = [] 		#key is idk, object is Lane Instance
		self.ACCSpeed = 0.0		#Current Speed ACC is set to
	#end __init__
#end ROSData
