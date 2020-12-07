;; Auto-generated. Do not edit!


(when (boundp 'erau_fusion_msgs::veh_object)
  (if (not (find-package "ERAU_FUSION_MSGS"))
    (make-package "ERAU_FUSION_MSGS"))
  (shadow 'veh_object (find-package "ERAU_FUSION_MSGS")))
(unless (find-package "ERAU_FUSION_MSGS::VEH_OBJECT")
  (make-package "ERAU_FUSION_MSGS::VEH_OBJECT"))

(in-package "ROS")
;;//! \htmlinclude veh_object.msg.html


(defclass erau_fusion_msgs::veh_object
  :super ros::object
  :slots (_x _y _dx_var _dy_var _dx _dy _vx_var _vy_var _classification _sizeX _sizeY _blinker_info ))

(defmethod erau_fusion_msgs::veh_object
  (:init
   (&key
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    ((:dx_var __dx_var) 0.0)
    ((:dy_var __dy_var) 0.0)
    ((:dx __dx) 0.0)
    ((:dy __dy) 0.0)
    ((:vx_var __vx_var) 0.0)
    ((:vy_var __vy_var) 0.0)
    ((:classification __classification) 0)
    ((:sizeX __sizeX) 0.0)
    ((:sizeY __sizeY) 0.0)
    ((:blinker_info __blinker_info) 0)
    )
   (send-super :init)
   (setq _x (float __x))
   (setq _y (float __y))
   (setq _dx_var (float __dx_var))
   (setq _dy_var (float __dy_var))
   (setq _dx (float __dx))
   (setq _dy (float __dy))
   (setq _vx_var (float __vx_var))
   (setq _vy_var (float __vy_var))
   (setq _classification (round __classification))
   (setq _sizeX (float __sizeX))
   (setq _sizeY (float __sizeY))
   (setq _blinker_info (round __blinker_info))
   self)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:dx_var
   (&optional __dx_var)
   (if __dx_var (setq _dx_var __dx_var)) _dx_var)
  (:dy_var
   (&optional __dy_var)
   (if __dy_var (setq _dy_var __dy_var)) _dy_var)
  (:dx
   (&optional __dx)
   (if __dx (setq _dx __dx)) _dx)
  (:dy
   (&optional __dy)
   (if __dy (setq _dy __dy)) _dy)
  (:vx_var
   (&optional __vx_var)
   (if __vx_var (setq _vx_var __vx_var)) _vx_var)
  (:vy_var
   (&optional __vy_var)
   (if __vy_var (setq _vy_var __vy_var)) _vy_var)
  (:classification
   (&optional __classification)
   (if __classification (setq _classification __classification)) _classification)
  (:sizeX
   (&optional __sizeX)
   (if __sizeX (setq _sizeX __sizeX)) _sizeX)
  (:sizeY
   (&optional __sizeY)
   (if __sizeY (setq _sizeY __sizeY)) _sizeY)
  (:blinker_info
   (&optional __blinker_info)
   (if __blinker_info (setq _blinker_info __blinker_info)) _blinker_info)
  (:serialization-length
   ()
   (+
    ;; float32 _x
    4
    ;; float32 _y
    4
    ;; float32 _dx_var
    4
    ;; float32 _dy_var
    4
    ;; float32 _dx
    4
    ;; float32 _dy
    4
    ;; float32 _vx_var
    4
    ;; float32 _vy_var
    4
    ;; uint8 _classification
    1
    ;; float32 _sizeX
    4
    ;; float32 _sizeY
    4
    ;; uint8 _blinker_info
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _x
       (sys::poke _x (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _y
       (sys::poke _y (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _dx_var
       (sys::poke _dx_var (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _dy_var
       (sys::poke _dy_var (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _dx
       (sys::poke _dx (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _dy
       (sys::poke _dy (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _vx_var
       (sys::poke _vx_var (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _vy_var
       (sys::poke _vy_var (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; uint8 _classification
       (write-byte _classification s)
     ;; float32 _sizeX
       (sys::poke _sizeX (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _sizeY
       (sys::poke _sizeY (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; uint8 _blinker_info
       (write-byte _blinker_info s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _x
     (setq _x (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _y
     (setq _y (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _dx_var
     (setq _dx_var (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _dy_var
     (setq _dy_var (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _dx
     (setq _dx (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _dy
     (setq _dy (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _vx_var
     (setq _vx_var (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _vy_var
     (setq _vy_var (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; uint8 _classification
     (setq _classification (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; float32 _sizeX
     (setq _sizeX (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _sizeY
     (setq _sizeY (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; uint8 _blinker_info
     (setq _blinker_info (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;;
   self)
  )

(setf (get erau_fusion_msgs::veh_object :md5sum-) "854e2d728659a600f851a5b56bc86a26")
(setf (get erau_fusion_msgs::veh_object :datatype-) "erau_fusion_msgs/veh_object")
(setf (get erau_fusion_msgs::veh_object :definition-)
      "
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



(provide :erau_fusion_msgs/veh_object "854e2d728659a600f851a5b56bc86a26")


