;; Auto-generated. Do not edit!


(when (boundp 'erau_fusion_msgs::tracked_vehicles)
  (if (not (find-package "ERAU_FUSION_MSGS"))
    (make-package "ERAU_FUSION_MSGS"))
  (shadow 'tracked_vehicles (find-package "ERAU_FUSION_MSGS")))
(unless (find-package "ERAU_FUSION_MSGS::TRACKED_VEHICLES")
  (make-package "ERAU_FUSION_MSGS::TRACKED_VEHICLES"))

(in-package "ROS")
;;//! \htmlinclude tracked_vehicles.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass erau_fusion_msgs::tracked_vehicles
  :super ros::object
  :slots (_header _objects ))

(defmethod erau_fusion_msgs::tracked_vehicles
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:objects __objects) (let (r) (dotimes (i 32) (push (instance erau_fusion_msgs::tracked_veh_object :init) r)) r))
    )
   (send-super :init)
   (setq _header __header)
   (setq _objects __objects)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:objects
   (&rest __objects)
   (if (keywordp (car __objects))
       (send* _objects __objects)
     (progn
       (if __objects (setq _objects (car __objects)))
       _objects)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; erau_fusion_msgs/tracked_veh_object[32] _objects
    (apply #'+ (send-all _objects :serialization-length))
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; erau_fusion_msgs/tracked_veh_object[32] _objects
     (dolist (elem _objects)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; erau_fusion_msgs/tracked_veh_object[32] _objects
   (dotimes (i 32)
     (send (elt _objects i) :deserialize buf ptr-) (incf ptr- (send (elt _objects i) :serialization-length))
     )
   ;;
   self)
  )

(setf (get erau_fusion_msgs::tracked_vehicles :md5sum-) "dd7f5ff80dc1711c347504ad53ab7290")
(setf (get erau_fusion_msgs::tracked_vehicles :datatype-) "erau_fusion_msgs/tracked_vehicles")
(setf (get erau_fusion_msgs::tracked_vehicles :definition-)
      "std_msgs/Header header
erau_fusion_msgs/tracked_veh_object[32] objects

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: erau_fusion_msgs/tracked_veh_object
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

================================================================================
MSG: erau_fusion_msgs/veh_object

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

")



(provide :erau_fusion_msgs/tracked_vehicles "dd7f5ff80dc1711c347504ad53ab7290")


