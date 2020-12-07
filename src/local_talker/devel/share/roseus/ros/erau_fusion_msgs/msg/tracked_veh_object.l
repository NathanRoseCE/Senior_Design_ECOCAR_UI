;; Auto-generated. Do not edit!


(when (boundp 'erau_fusion_msgs::tracked_veh_object)
  (if (not (find-package "ERAU_FUSION_MSGS"))
    (make-package "ERAU_FUSION_MSGS"))
  (shadow 'tracked_veh_object (find-package "ERAU_FUSION_MSGS")))
(unless (find-package "ERAU_FUSION_MSGS::TRACKED_VEH_OBJECT")
  (make-package "ERAU_FUSION_MSGS::TRACKED_VEH_OBJECT"))

(in-package "ROS")
;;//! \htmlinclude tracked_veh_object.msg.html


(defclass erau_fusion_msgs::tracked_veh_object
  :super ros::object
  :slots (_object _id _object_age _lane ))

(defmethod erau_fusion_msgs::tracked_veh_object
  (:init
   (&key
    ((:object __object) (instance erau_fusion_msgs::veh_object :init))
    ((:id __id) 0)
    ((:object_age __object_age) 0)
    ((:lane __lane) 0)
    )
   (send-super :init)
   (setq _object __object)
   (setq _id (round __id))
   (setq _object_age (round __object_age))
   (setq _lane (round __lane))
   self)
  (:object
   (&rest __object)
   (if (keywordp (car __object))
       (send* _object __object)
     (progn
       (if __object (setq _object (car __object)))
       _object)))
  (:id
   (&optional __id)
   (if __id (setq _id __id)) _id)
  (:object_age
   (&optional __object_age)
   (if __object_age (setq _object_age __object_age)) _object_age)
  (:lane
   (&optional __lane)
   (if __lane (setq _lane __lane)) _lane)
  (:serialization-length
   ()
   (+
    ;; erau_fusion_msgs/veh_object _object
    (send _object :serialization-length)
    ;; uint8 _id
    1
    ;; uint16 _object_age
    2
    ;; uint8 _lane
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; erau_fusion_msgs/veh_object _object
       (send _object :serialize s)
     ;; uint8 _id
       (write-byte _id s)
     ;; uint16 _object_age
       (write-word _object_age s)
     ;; uint8 _lane
       (write-byte _lane s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; erau_fusion_msgs/veh_object _object
     (send _object :deserialize buf ptr-) (incf ptr- (send _object :serialization-length))
   ;; uint8 _id
     (setq _id (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint16 _object_age
     (setq _object_age (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint8 _lane
     (setq _lane (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;;
   self)
  )

(setf (get erau_fusion_msgs::tracked_veh_object :md5sum-) "0eaf4f33ea0e60aee406a700d7cb793e")
(setf (get erau_fusion_msgs::tracked_veh_object :datatype-) "erau_fusion_msgs/tracked_veh_object")
(setf (get erau_fusion_msgs::tracked_veh_object :definition-)
      "erau_fusion_msgs/veh_object object

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



(provide :erau_fusion_msgs/tracked_veh_object "0eaf4f33ea0e60aee406a700d7cb793e")


