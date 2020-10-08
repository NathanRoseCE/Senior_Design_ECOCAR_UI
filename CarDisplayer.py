
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
		self.x = self.x + (self.dx + dt)
		self.y = self.y + (self.dy + dt)
	#end updatePosition
#end Obstacle
