#Lane info from LkaLane msg
# LANE_TYPE_DASHED = 0
# LANE_TYPE_SOLID = 1
# LANE_TYPE_NONE = 2
# LANE_TYPE_ROAD_EDGE = 3
# LANE_TYPE_DOUBLE_LANE_MARK = 4
# LANE_TYPE_BOTTS_DOTS = 5
# LANE_TYPE_INVALID = 6
uint8 lane_type_Left
uint8 lane_type_Right
uint8 lanePosition # (0 unknown, 1 left, 2 right)
uint8 laneWidth #Used for scaling cars

float64 position_parameter
