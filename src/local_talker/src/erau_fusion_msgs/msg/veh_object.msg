
# Coordinate frames based on center of front fascia at ground level.
# +x is forward, +y is left, +z is up

# Position
float32 x
float32 y
# Position Variance
float32 dx_var
float32 dy_var

# Relative Velocity
float32 dx
float32 dy
# Velocity Variance
float32 vx_var
float32 vy_var

# Classification
# 0 for Unknown
# 1 for car
# 2 for truck
# 3 for pedestrian
uint8 classification

#Car Size
float32 sizeX
float32 sizeY

#Blinker info (from ObstacleData.msg)
# BLINKER_INFO_UNAVAILABLE = 0
# BLINKER_INFO_OFF = 1
# BLINKER_INFO_LEFT = 2
# BLINKER_INFO_RIGHT = 3
# BLINKER_INFO_BOTH = 4
uint8 blinker_info
