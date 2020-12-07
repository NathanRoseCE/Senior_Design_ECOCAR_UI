;; Auto-generated. Do not edit!


(when (boundp 'erau_fusion_msgs::Tracked_Lane_Object)
  (if (not (find-package "ERAU_FUSION_MSGS"))
    (make-package "ERAU_FUSION_MSGS"))
  (shadow 'Tracked_Lane_Object (find-package "ERAU_FUSION_MSGS")))
(unless (find-package "ERAU_FUSION_MSGS::TRACKED_LANE_OBJECT")
  (make-package "ERAU_FUSION_MSGS::TRACKED_LANE_OBJECT"))

(in-package "ROS")
;;//! \htmlinclude Tracked_Lane_Object.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass erau_fusion_msgs::Tracked_Lane_Object
  :super ros::object
  :slots (_header _objects ))

(defmethod erau_fusion_msgs::Tracked_Lane_Object
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:objects __objects) (let (r) (dotimes (i 32) (push (instance erau_fusion_msgs::Tracked_Lane :init) r)) r))
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
    ;; erau_fusion_msgs/Tracked_Lane[32] _objects
    (apply #'+ (send-all _objects :serialization-length))
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; erau_fusion_msgs/Tracked_Lane[32] _objects
     (dolist (elem _objects)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; erau_fusion_msgs/Tracked_Lane[32] _objects
   (dotimes (i 32)
     (send (elt _objects i) :deserialize buf ptr-) (incf ptr- (send (elt _objects i) :serialization-length))
     )
   ;;
   self)
  )

(setf (get erau_fusion_msgs::Tracked_Lane_Object :md5sum-) "a320a79d93ffd064ef7141dc8e5a6c89")
(setf (get erau_fusion_msgs::Tracked_Lane_Object :datatype-) "erau_fusion_msgs/Tracked_Lane_Object")
(setf (get erau_fusion_msgs::Tracked_Lane_Object :definition-)
      "std_msgs/Header header
erau_fusion_msgs/Tracked_Lane[32] objects

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
MSG: erau_fusion_msgs/Tracked_Lane
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

")



(provide :erau_fusion_msgs/Tracked_Lane_Object "a320a79d93ffd064ef7141dc8e5a6c89")


