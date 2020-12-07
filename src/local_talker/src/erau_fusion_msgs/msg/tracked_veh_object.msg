erau_fusion_msgs/veh_object object

uint8 id # unique identifier to this object; should remain constant for this object over time
uint16 object_age  # total time this vehicle has been tracked for (in seconds)

# Lane assignment
# 0 - Unknown
# 1 - Left
# 2 - Host/center
# 3 - Right
uint8 lane

# TODO add tracks
