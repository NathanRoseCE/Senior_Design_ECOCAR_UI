; Auto-generated. Do not edit!


(cl:in-package erau_fusion_msgs-msg)


;//! \htmlinclude tracked_vehicles.msg.html

(cl:defclass <tracked_vehicles> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (objects
    :reader objects
    :initarg :objects
    :type (cl:vector erau_fusion_msgs-msg:tracked_veh_object)
   :initform (cl:make-array 32 :element-type 'erau_fusion_msgs-msg:tracked_veh_object :initial-element (cl:make-instance 'erau_fusion_msgs-msg:tracked_veh_object))))
)

(cl:defclass tracked_vehicles (<tracked_vehicles>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <tracked_vehicles>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'tracked_vehicles)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name erau_fusion_msgs-msg:<tracked_vehicles> is deprecated: use erau_fusion_msgs-msg:tracked_vehicles instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <tracked_vehicles>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader erau_fusion_msgs-msg:header-val is deprecated.  Use erau_fusion_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'objects-val :lambda-list '(m))
(cl:defmethod objects-val ((m <tracked_vehicles>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader erau_fusion_msgs-msg:objects-val is deprecated.  Use erau_fusion_msgs-msg:objects instead.")
  (objects m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <tracked_vehicles>) ostream)
  "Serializes a message object of type '<tracked_vehicles>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'objects))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <tracked_vehicles>) istream)
  "Deserializes a message object of type '<tracked_vehicles>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (cl:setf (cl:slot-value msg 'objects) (cl:make-array 32))
  (cl:let ((vals (cl:slot-value msg 'objects)))
    (cl:dotimes (i 32)
    (cl:setf (cl:aref vals i) (cl:make-instance 'erau_fusion_msgs-msg:tracked_veh_object))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<tracked_vehicles>)))
  "Returns string type for a message object of type '<tracked_vehicles>"
  "erau_fusion_msgs/tracked_vehicles")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'tracked_vehicles)))
  "Returns string type for a message object of type 'tracked_vehicles"
  "erau_fusion_msgs/tracked_vehicles")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<tracked_vehicles>)))
  "Returns md5sum for a message object of type '<tracked_vehicles>"
  "dd7f5ff80dc1711c347504ad53ab7290")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'tracked_vehicles)))
  "Returns md5sum for a message object of type 'tracked_vehicles"
  "dd7f5ff80dc1711c347504ad53ab7290")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<tracked_vehicles>)))
  "Returns full string definition for message of type '<tracked_vehicles>"
  (cl:format cl:nil "std_msgs/Header header~%erau_fusion_msgs/tracked_veh_object[32] objects~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: erau_fusion_msgs/tracked_veh_object~%erau_fusion_msgs/veh_object object~%~%uint8 id # unique identifier to this object; should remain constant for this object over time~%uint16 object_age  # total time this vehicle has been tracked for (in seconds)~%~%# Lane assignment~%# 0 - Unknown~%# 1 - Left~%# 2 - Host/center~%# 3 - Right~%uint8 lane~%~%# TODO add tracks~%~%================================================================================~%MSG: erau_fusion_msgs/veh_object~%~%# Coordinate frames based on center of front fascia at ground level.~%# +x is forward, +y is left, +z is up~%~%# Position~%float32 x~%float32 y~%# Position Variance~%float32 dx_var~%float32 dy_var~%~%# Relative Velocity~%float32 dx~%float32 dy~%# Velocity Variance~%float32 vx_var~%float32 vy_var~%~%# Classification~%# 0 for Unknown~%# 1 for car~%# 2 for truck~%# 3 for pedestrian~%uint8 classification~%~%#Car Size~%float32 sizeX~%float32 sizeY~%~%#Blinker info (from ObstacleData.msg)~%# BLINKER_INFO_UNAVAILABLE = 0~%# BLINKER_INFO_OFF = 1~%# BLINKER_INFO_LEFT = 2~%# BLINKER_INFO_RIGHT = 3~%# BLINKER_INFO_BOTH = 4~%uint8 blinker_info~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'tracked_vehicles)))
  "Returns full string definition for message of type 'tracked_vehicles"
  (cl:format cl:nil "std_msgs/Header header~%erau_fusion_msgs/tracked_veh_object[32] objects~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: erau_fusion_msgs/tracked_veh_object~%erau_fusion_msgs/veh_object object~%~%uint8 id # unique identifier to this object; should remain constant for this object over time~%uint16 object_age  # total time this vehicle has been tracked for (in seconds)~%~%# Lane assignment~%# 0 - Unknown~%# 1 - Left~%# 2 - Host/center~%# 3 - Right~%uint8 lane~%~%# TODO add tracks~%~%================================================================================~%MSG: erau_fusion_msgs/veh_object~%~%# Coordinate frames based on center of front fascia at ground level.~%# +x is forward, +y is left, +z is up~%~%# Position~%float32 x~%float32 y~%# Position Variance~%float32 dx_var~%float32 dy_var~%~%# Relative Velocity~%float32 dx~%float32 dy~%# Velocity Variance~%float32 vx_var~%float32 vy_var~%~%# Classification~%# 0 for Unknown~%# 1 for car~%# 2 for truck~%# 3 for pedestrian~%uint8 classification~%~%#Car Size~%float32 sizeX~%float32 sizeY~%~%#Blinker info (from ObstacleData.msg)~%# BLINKER_INFO_UNAVAILABLE = 0~%# BLINKER_INFO_OFF = 1~%# BLINKER_INFO_LEFT = 2~%# BLINKER_INFO_RIGHT = 3~%# BLINKER_INFO_BOTH = 4~%uint8 blinker_info~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <tracked_vehicles>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'objects) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <tracked_vehicles>))
  "Converts a ROS message object to a list"
  (cl:list 'tracked_vehicles
    (cl:cons ':header (header msg))
    (cl:cons ':objects (objects msg))
))
