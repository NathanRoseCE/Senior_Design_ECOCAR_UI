;; Auto-generated. Do not edit!


(when (boundp 'erau_fusion_msgs::CanBus)
  (if (not (find-package "ERAU_FUSION_MSGS"))
    (make-package "ERAU_FUSION_MSGS"))
  (shadow 'CanBus (find-package "ERAU_FUSION_MSGS")))
(unless (find-package "ERAU_FUSION_MSGS::CANBUS")
  (make-package "ERAU_FUSION_MSGS::CANBUS"))

(in-package "ROS")
;;//! \htmlinclude CanBus.msg.html


(defclass erau_fusion_msgs::CanBus
  :super ros::object
  :slots (_CarSpeed ))

(defmethod erau_fusion_msgs::CanBus
  (:init
   (&key
    ((:CarSpeed __CarSpeed) 0.0)
    )
   (send-super :init)
   (setq _CarSpeed (float __CarSpeed))
   self)
  (:CarSpeed
   (&optional __CarSpeed)
   (if __CarSpeed (setq _CarSpeed __CarSpeed)) _CarSpeed)
  (:serialization-length
   ()
   (+
    ;; float32 _CarSpeed
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _CarSpeed
       (sys::poke _CarSpeed (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _CarSpeed
     (setq _CarSpeed (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get erau_fusion_msgs::CanBus :md5sum-) "dc1a7c020ca7ccfab53c9facec5520c4")
(setf (get erau_fusion_msgs::CanBus :datatype-) "erau_fusion_msgs/CanBus")
(setf (get erau_fusion_msgs::CanBus :definition-)
      "float32 CarSpeed

")



(provide :erau_fusion_msgs/CanBus "dc1a7c020ca7ccfab53c9facec5520c4")


