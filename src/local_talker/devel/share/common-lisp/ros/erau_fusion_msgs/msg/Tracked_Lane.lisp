; Auto-generated. Do not edit!


(cl:in-package erau_fusion_msgs-msg)


;//! \htmlinclude Tracked_Lane.msg.html

(cl:defclass <Tracked_Lane> (roslisp-msg-protocol:ros-message)
  ((lane_type_Left
    :reader lane_type_Left
    :initarg :lane_type_Left
    :type cl:fixnum
    :initform 0)
   (lane_type_Right
    :reader lane_type_Right
    :initarg :lane_type_Right
    :type cl:fixnum
    :initform 0)
   (lanePosition
    :reader lanePosition
    :initarg :lanePosition
    :type cl:fixnum
    :initform 0)
   (laneWidth
    :reader laneWidth
    :initarg :laneWidth
    :type cl:fixnum
    :initform 0)
   (position_parameter
    :reader position_parameter
    :initarg :position_parameter
    :type cl:float
    :initform 0.0))
)

(cl:defclass Tracked_Lane (<Tracked_Lane>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Tracked_Lane>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Tracked_Lane)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name erau_fusion_msgs-msg:<Tracked_Lane> is deprecated: use erau_fusion_msgs-msg:Tracked_Lane instead.")))

(cl:ensure-generic-function 'lane_type_Left-val :lambda-list '(m))
(cl:defmethod lane_type_Left-val ((m <Tracked_Lane>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader erau_fusion_msgs-msg:lane_type_Left-val is deprecated.  Use erau_fusion_msgs-msg:lane_type_Left instead.")
  (lane_type_Left m))

(cl:ensure-generic-function 'lane_type_Right-val :lambda-list '(m))
(cl:defmethod lane_type_Right-val ((m <Tracked_Lane>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader erau_fusion_msgs-msg:lane_type_Right-val is deprecated.  Use erau_fusion_msgs-msg:lane_type_Right instead.")
  (lane_type_Right m))

(cl:ensure-generic-function 'lanePosition-val :lambda-list '(m))
(cl:defmethod lanePosition-val ((m <Tracked_Lane>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader erau_fusion_msgs-msg:lanePosition-val is deprecated.  Use erau_fusion_msgs-msg:lanePosition instead.")
  (lanePosition m))

(cl:ensure-generic-function 'laneWidth-val :lambda-list '(m))
(cl:defmethod laneWidth-val ((m <Tracked_Lane>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader erau_fusion_msgs-msg:laneWidth-val is deprecated.  Use erau_fusion_msgs-msg:laneWidth instead.")
  (laneWidth m))

(cl:ensure-generic-function 'position_parameter-val :lambda-list '(m))
(cl:defmethod position_parameter-val ((m <Tracked_Lane>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader erau_fusion_msgs-msg:position_parameter-val is deprecated.  Use erau_fusion_msgs-msg:position_parameter instead.")
  (position_parameter m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Tracked_Lane>) ostream)
  "Serializes a message object of type '<Tracked_Lane>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'lane_type_Left)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'lane_type_Right)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'lanePosition)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'laneWidth)) ostream)
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'position_parameter))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Tracked_Lane>) istream)
  "Deserializes a message object of type '<Tracked_Lane>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'lane_type_Left)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'lane_type_Right)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'lanePosition)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'laneWidth)) (cl:read-byte istream))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'position_parameter) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Tracked_Lane>)))
  "Returns string type for a message object of type '<Tracked_Lane>"
  "erau_fusion_msgs/Tracked_Lane")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Tracked_Lane)))
  "Returns string type for a message object of type 'Tracked_Lane"
  "erau_fusion_msgs/Tracked_Lane")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Tracked_Lane>)))
  "Returns md5sum for a message object of type '<Tracked_Lane>"
  "14f981197f8d751c83fad6e1038cf6df")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Tracked_Lane)))
  "Returns md5sum for a message object of type 'Tracked_Lane"
  "14f981197f8d751c83fad6e1038cf6df")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Tracked_Lane>)))
  "Returns full string definition for message of type '<Tracked_Lane>"
  (cl:format cl:nil "#Lane info from LkaLane msg~%# LANE_TYPE_DASHED = 0~%# LANE_TYPE_SOLID = 1~%# LANE_TYPE_NONE = 2~%# LANE_TYPE_ROAD_EDGE = 3~%# LANE_TYPE_DOUBLE_LANE_MARK = 4~%# LANE_TYPE_BOTTS_DOTS = 5~%# LANE_TYPE_INVALID = 6~%uint8 lane_type_Left~%uint8 lane_type_Right~%uint8 lanePosition # (0 unknown, 1 left, 2 right)~%uint8 laneWidth #Used for scaling cars~%~%float64 position_parameter~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Tracked_Lane)))
  "Returns full string definition for message of type 'Tracked_Lane"
  (cl:format cl:nil "#Lane info from LkaLane msg~%# LANE_TYPE_DASHED = 0~%# LANE_TYPE_SOLID = 1~%# LANE_TYPE_NONE = 2~%# LANE_TYPE_ROAD_EDGE = 3~%# LANE_TYPE_DOUBLE_LANE_MARK = 4~%# LANE_TYPE_BOTTS_DOTS = 5~%# LANE_TYPE_INVALID = 6~%uint8 lane_type_Left~%uint8 lane_type_Right~%uint8 lanePosition # (0 unknown, 1 left, 2 right)~%uint8 laneWidth #Used for scaling cars~%~%float64 position_parameter~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Tracked_Lane>))
  (cl:+ 0
     1
     1
     1
     1
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Tracked_Lane>))
  "Converts a ROS message object to a list"
  (cl:list 'Tracked_Lane
    (cl:cons ':lane_type_Left (lane_type_Left msg))
    (cl:cons ':lane_type_Right (lane_type_Right msg))
    (cl:cons ':lanePosition (lanePosition msg))
    (cl:cons ':laneWidth (laneWidth msg))
    (cl:cons ':position_parameter (position_parameter msg))
))
