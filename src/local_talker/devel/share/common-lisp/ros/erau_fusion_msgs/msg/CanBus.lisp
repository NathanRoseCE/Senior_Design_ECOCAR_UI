; Auto-generated. Do not edit!


(cl:in-package erau_fusion_msgs-msg)


;//! \htmlinclude CanBus.msg.html

(cl:defclass <CanBus> (roslisp-msg-protocol:ros-message)
  ((CarSpeed
    :reader CarSpeed
    :initarg :CarSpeed
    :type cl:float
    :initform 0.0))
)

(cl:defclass CanBus (<CanBus>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <CanBus>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'CanBus)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name erau_fusion_msgs-msg:<CanBus> is deprecated: use erau_fusion_msgs-msg:CanBus instead.")))

(cl:ensure-generic-function 'CarSpeed-val :lambda-list '(m))
(cl:defmethod CarSpeed-val ((m <CanBus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader erau_fusion_msgs-msg:CarSpeed-val is deprecated.  Use erau_fusion_msgs-msg:CarSpeed instead.")
  (CarSpeed m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <CanBus>) ostream)
  "Serializes a message object of type '<CanBus>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'CarSpeed))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <CanBus>) istream)
  "Deserializes a message object of type '<CanBus>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'CarSpeed) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<CanBus>)))
  "Returns string type for a message object of type '<CanBus>"
  "erau_fusion_msgs/CanBus")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'CanBus)))
  "Returns string type for a message object of type 'CanBus"
  "erau_fusion_msgs/CanBus")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<CanBus>)))
  "Returns md5sum for a message object of type '<CanBus>"
  "dc1a7c020ca7ccfab53c9facec5520c4")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'CanBus)))
  "Returns md5sum for a message object of type 'CanBus"
  "dc1a7c020ca7ccfab53c9facec5520c4")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<CanBus>)))
  "Returns full string definition for message of type '<CanBus>"
  (cl:format cl:nil "float32 CarSpeed~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'CanBus)))
  "Returns full string definition for message of type 'CanBus"
  (cl:format cl:nil "float32 CarSpeed~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <CanBus>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <CanBus>))
  "Converts a ROS message object to a list"
  (cl:list 'CanBus
    (cl:cons ':CarSpeed (CarSpeed msg))
))
