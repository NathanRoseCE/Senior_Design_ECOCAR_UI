; Auto-generated. Do not edit!


(cl:in-package erau_fusion_msgs-msg)


;//! \htmlinclude Tracked_Lane_Object.msg.html

(cl:defclass <Tracked_Lane_Object> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (objects
    :reader objects
    :initarg :objects
    :type (cl:vector erau_fusion_msgs-msg:Tracked_Lane)
   :initform (cl:make-array 32 :element-type 'erau_fusion_msgs-msg:Tracked_Lane :initial-element (cl:make-instance 'erau_fusion_msgs-msg:Tracked_Lane))))
)

(cl:defclass Tracked_Lane_Object (<Tracked_Lane_Object>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Tracked_Lane_Object>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Tracked_Lane_Object)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name erau_fusion_msgs-msg:<Tracked_Lane_Object> is deprecated: use erau_fusion_msgs-msg:Tracked_Lane_Object instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <Tracked_Lane_Object>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader erau_fusion_msgs-msg:header-val is deprecated.  Use erau_fusion_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'objects-val :lambda-list '(m))
(cl:defmethod objects-val ((m <Tracked_Lane_Object>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader erau_fusion_msgs-msg:objects-val is deprecated.  Use erau_fusion_msgs-msg:objects instead.")
  (objects m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Tracked_Lane_Object>) ostream)
  "Serializes a message object of type '<Tracked_Lane_Object>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'objects))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Tracked_Lane_Object>) istream)
  "Deserializes a message object of type '<Tracked_Lane_Object>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (cl:setf (cl:slot-value msg 'objects) (cl:make-array 32))
  (cl:let ((vals (cl:slot-value msg 'objects)))
    (cl:dotimes (i 32)
    (cl:setf (cl:aref vals i) (cl:make-instance 'erau_fusion_msgs-msg:Tracked_Lane))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Tracked_Lane_Object>)))
  "Returns string type for a message object of type '<Tracked_Lane_Object>"
  "erau_fusion_msgs/Tracked_Lane_Object")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Tracked_Lane_Object)))
  "Returns string type for a message object of type 'Tracked_Lane_Object"
  "erau_fusion_msgs/Tracked_Lane_Object")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Tracked_Lane_Object>)))
  "Returns md5sum for a message object of type '<Tracked_Lane_Object>"
  "a320a79d93ffd064ef7141dc8e5a6c89")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Tracked_Lane_Object)))
  "Returns md5sum for a message object of type 'Tracked_Lane_Object"
  "a320a79d93ffd064ef7141dc8e5a6c89")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Tracked_Lane_Object>)))
  "Returns full string definition for message of type '<Tracked_Lane_Object>"
  (cl:format cl:nil "std_msgs/Header header~%erau_fusion_msgs/Tracked_Lane[32] objects~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: erau_fusion_msgs/Tracked_Lane~%#Lane info from LkaLane msg~%# LANE_TYPE_DASHED = 0~%# LANE_TYPE_SOLID = 1~%# LANE_TYPE_NONE = 2~%# LANE_TYPE_ROAD_EDGE = 3~%# LANE_TYPE_DOUBLE_LANE_MARK = 4~%# LANE_TYPE_BOTTS_DOTS = 5~%# LANE_TYPE_INVALID = 6~%uint8 lane_type_Left~%uint8 lane_type_Right~%uint8 lanePosition # (0 unknown, 1 left, 2 right)~%uint8 laneWidth #Used for scaling cars~%~%float64 position_parameter~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Tracked_Lane_Object)))
  "Returns full string definition for message of type 'Tracked_Lane_Object"
  (cl:format cl:nil "std_msgs/Header header~%erau_fusion_msgs/Tracked_Lane[32] objects~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: erau_fusion_msgs/Tracked_Lane~%#Lane info from LkaLane msg~%# LANE_TYPE_DASHED = 0~%# LANE_TYPE_SOLID = 1~%# LANE_TYPE_NONE = 2~%# LANE_TYPE_ROAD_EDGE = 3~%# LANE_TYPE_DOUBLE_LANE_MARK = 4~%# LANE_TYPE_BOTTS_DOTS = 5~%# LANE_TYPE_INVALID = 6~%uint8 lane_type_Left~%uint8 lane_type_Right~%uint8 lanePosition # (0 unknown, 1 left, 2 right)~%uint8 laneWidth #Used for scaling cars~%~%float64 position_parameter~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Tracked_Lane_Object>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'objects) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Tracked_Lane_Object>))
  "Converts a ROS message object to a list"
  (cl:list 'Tracked_Lane_Object
    (cl:cons ':header (header msg))
    (cl:cons ':objects (objects msg))
))
