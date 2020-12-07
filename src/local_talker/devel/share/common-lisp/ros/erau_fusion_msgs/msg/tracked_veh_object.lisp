; Auto-generated. Do not edit!


(cl:in-package erau_fusion_msgs-msg)


;//! \htmlinclude tracked_veh_object.msg.html

(cl:defclass <tracked_veh_object> (roslisp-msg-protocol:ros-message)
  ((object
    :reader object
    :initarg :object
    :type erau_fusion_msgs-msg:veh_object
    :initform (cl:make-instance 'erau_fusion_msgs-msg:veh_object))
   (id
    :reader id
    :initarg :id
    :type cl:fixnum
    :initform 0)
   (object_age
    :reader object_age
    :initarg :object_age
    :type cl:fixnum
    :initform 0)
   (lane
    :reader lane
    :initarg :lane
    :type cl:fixnum
    :initform 0))
)

(cl:defclass tracked_veh_object (<tracked_veh_object>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <tracked_veh_object>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'tracked_veh_object)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name erau_fusion_msgs-msg:<tracked_veh_object> is deprecated: use erau_fusion_msgs-msg:tracked_veh_object instead.")))

(cl:ensure-generic-function 'object-val :lambda-list '(m))
(cl:defmethod object-val ((m <tracked_veh_object>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader erau_fusion_msgs-msg:object-val is deprecated.  Use erau_fusion_msgs-msg:object instead.")
  (object m))

(cl:ensure-generic-function 'id-val :lambda-list '(m))
(cl:defmethod id-val ((m <tracked_veh_object>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader erau_fusion_msgs-msg:id-val is deprecated.  Use erau_fusion_msgs-msg:id instead.")
  (id m))

(cl:ensure-generic-function 'object_age-val :lambda-list '(m))
(cl:defmethod object_age-val ((m <tracked_veh_object>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader erau_fusion_msgs-msg:object_age-val is deprecated.  Use erau_fusion_msgs-msg:object_age instead.")
  (object_age m))

(cl:ensure-generic-function 'lane-val :lambda-list '(m))
(cl:defmethod lane-val ((m <tracked_veh_object>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader erau_fusion_msgs-msg:lane-val is deprecated.  Use erau_fusion_msgs-msg:lane instead.")
  (lane m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <tracked_veh_object>) ostream)
  "Serializes a message object of type '<tracked_veh_object>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'object) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'object_age)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'object_age)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'lane)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <tracked_veh_object>) istream)
  "Deserializes a message object of type '<tracked_veh_object>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'object) istream)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'object_age)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'object_age)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'lane)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<tracked_veh_object>)))
  "Returns string type for a message object of type '<tracked_veh_object>"
  "erau_fusion_msgs/tracked_veh_object")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'tracked_veh_object)))
  "Returns string type for a message object of type 'tracked_veh_object"
  "erau_fusion_msgs/tracked_veh_object")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<tracked_veh_object>)))
  "Returns md5sum for a message object of type '<tracked_veh_object>"
  "0eaf4f33ea0e60aee406a700d7cb793e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'tracked_veh_object)))
  "Returns md5sum for a message object of type 'tracked_veh_object"
  "0eaf4f33ea0e60aee406a700d7cb793e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<tracked_veh_object>)))
  "Returns full string definition for message of type '<tracked_veh_object>"
  (cl:format cl:nil "erau_fusion_msgs/veh_object object~%~%uint8 id # unique identifier to this object; should remain constant for this object over time~%uint16 object_age  # total time this vehicle has been tracked for (in seconds)~%~%# Lane assignment~%# 0 - Unknown~%# 1 - Left~%# 2 - Host/center~%# 3 - Right~%uint8 lane~%~%# TODO add tracks~%~%================================================================================~%MSG: erau_fusion_msgs/veh_object~%~%# Coordinate frames based on center of front fascia at ground level.~%# +x is forward, +y is left, +z is up~%~%# Position~%float32 x~%float32 y~%# Position Variance~%float32 dx_var~%float32 dy_var~%~%# Relative Velocity~%float32 dx~%float32 dy~%# Velocity Variance~%float32 vx_var~%float32 vy_var~%~%# Classification~%# 0 for Unknown~%# 1 for car~%# 2 for truck~%# 3 for pedestrian~%uint8 classification~%~%#Car Size~%float32 sizeX~%float32 sizeY~%~%#Blinker info (from ObstacleData.msg)~%# BLINKER_INFO_UNAVAILABLE = 0~%# BLINKER_INFO_OFF = 1~%# BLINKER_INFO_LEFT = 2~%# BLINKER_INFO_RIGHT = 3~%# BLINKER_INFO_BOTH = 4~%uint8 blinker_info~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'tracked_veh_object)))
  "Returns full string definition for message of type 'tracked_veh_object"
  (cl:format cl:nil "erau_fusion_msgs/veh_object object~%~%uint8 id # unique identifier to this object; should remain constant for this object over time~%uint16 object_age  # total time this vehicle has been tracked for (in seconds)~%~%# Lane assignment~%# 0 - Unknown~%# 1 - Left~%# 2 - Host/center~%# 3 - Right~%uint8 lane~%~%# TODO add tracks~%~%================================================================================~%MSG: erau_fusion_msgs/veh_object~%~%# Coordinate frames based on center of front fascia at ground level.~%# +x is forward, +y is left, +z is up~%~%# Position~%float32 x~%float32 y~%# Position Variance~%float32 dx_var~%float32 dy_var~%~%# Relative Velocity~%float32 dx~%float32 dy~%# Velocity Variance~%float32 vx_var~%float32 vy_var~%~%# Classification~%# 0 for Unknown~%# 1 for car~%# 2 for truck~%# 3 for pedestrian~%uint8 classification~%~%#Car Size~%float32 sizeX~%float32 sizeY~%~%#Blinker info (from ObstacleData.msg)~%# BLINKER_INFO_UNAVAILABLE = 0~%# BLINKER_INFO_OFF = 1~%# BLINKER_INFO_LEFT = 2~%# BLINKER_INFO_RIGHT = 3~%# BLINKER_INFO_BOTH = 4~%uint8 blinker_info~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <tracked_veh_object>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'object))
     1
     2
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <tracked_veh_object>))
  "Converts a ROS message object to a list"
  (cl:list 'tracked_veh_object
    (cl:cons ':object (object msg))
    (cl:cons ':id (id msg))
    (cl:cons ':object_age (object_age msg))
    (cl:cons ':lane (lane msg))
))
