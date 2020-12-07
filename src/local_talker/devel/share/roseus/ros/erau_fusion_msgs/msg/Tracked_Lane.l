;; Auto-generated. Do not edit!


(when (boundp 'erau_fusion_msgs::Tracked_Lane)
  (if (not (find-package "ERAU_FUSION_MSGS"))
    (make-package "ERAU_FUSION_MSGS"))
  (shadow 'Tracked_Lane (find-package "ERAU_FUSION_MSGS")))
(unless (find-package "ERAU_FUSION_MSGS::TRACKED_LANE")
  (make-package "ERAU_FUSION_MSGS::TRACKED_LANE"))

(in-package "ROS")
;;//! \htmlinclude Tracked_Lane.msg.html


(defclass erau_fusion_msgs::Tracked_Lane
  :super ros::object
  :slots (_lane_type_Left _lane_type_Right _lanePosition _laneWidth _position_parameter ))

(defmethod erau_fusion_msgs::Tracked_Lane
  (:init
   (&key
    ((:lane_type_Left __lane_type_Left) 0)
    ((:lane_type_Right __lane_type_Right) 0)
    ((:lanePosition __lanePosition) 0)
    ((:laneWidth __laneWidth) 0)
    ((:position_parameter __position_parameter) 0.0)
    )
   (send-super :init)
   (setq _lane_type_Left (round __lane_type_Left))
   (setq _lane_type_Right (round __lane_type_Right))
   (setq _lanePosition (round __lanePosition))
   (setq _laneWidth (round __laneWidth))
   (setq _position_parameter (float __position_parameter))
   self)
  (:lane_type_Left
   (&optional __lane_type_Left)
   (if __lane_type_Left (setq _lane_type_Left __lane_type_Left)) _lane_type_Left)
  (:lane_type_Right
   (&optional __lane_type_Right)
   (if __lane_type_Right (setq _lane_type_Right __lane_type_Right)) _lane_type_Right)
  (:lanePosition
   (&optional __lanePosition)
   (if __lanePosition (setq _lanePosition __lanePosition)) _lanePosition)
  (:laneWidth
   (&optional __laneWidth)
   (if __laneWidth (setq _laneWidth __laneWidth)) _laneWidth)
  (:position_parameter
   (&optional __position_parameter)
   (if __position_parameter (setq _position_parameter __position_parameter)) _position_parameter)
  (:serialization-length
   ()
   (+
    ;; uint8 _lane_type_Left
    1
    ;; uint8 _lane_type_Right
    1
    ;; uint8 _lanePosition
    1
    ;; uint8 _laneWidth
    1
    ;; float64 _position_parameter
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint8 _lane_type_Left
       (write-byte _lane_type_Left s)
     ;; uint8 _lane_type_Right
       (write-byte _lane_type_Right s)
     ;; uint8 _lanePosition
       (write-byte _lanePosition s)
     ;; uint8 _laneWidth
       (write-byte _laneWidth s)
     ;; float64 _position_parameter
       (sys::poke _position_parameter (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint8 _lane_type_Left
     (setq _lane_type_Left (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _lane_type_Right
     (setq _lane_type_Right (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _lanePosition
     (setq _lanePosition (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _laneWidth
     (setq _laneWidth (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; float64 _position_parameter
     (setq _position_parameter (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get erau_fusion_msgs::Tracked_Lane :md5sum-) "14f981197f8d751c83fad6e1038cf6df")
(setf (get erau_fusion_msgs::Tracked_Lane :datatype-) "erau_fusion_msgs/Tracked_Lane")
(setf (get erau_fusion_msgs::Tracked_Lane :definition-)
      "#Lane info from LkaLane msg
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



(provide :erau_fusion_msgs/Tracked_Lane "14f981197f8d751c83fad6e1038cf6df")


