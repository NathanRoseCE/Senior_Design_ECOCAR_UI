; Auto-generated. Do not edit!


(cl:in-package erau_fusion_msgs-msg)


;//! \htmlinclude veh_object.msg.html

(cl:defclass <veh_object> (roslisp-msg-protocol:ros-message)
  ((x
    :reader x
    :initarg :x
    :type cl:float
    :initform 0.0)
   (y
    :reader y
    :initarg :y
    :type cl:float
    :initform 0.0)
   (dx_var
    :reader dx_var
    :initarg :dx_var
    :type cl:float
    :initform 0.0)
   (dy_var
    :reader dy_var
    :initarg :dy_var
    :type cl:float
    :initform 0.0)
   (dx
    :reader dx
    :initarg :dx
    :type cl:float
    :initform 0.0)
   (dy
    :reader dy
    :initarg :dy
    :type cl:float
    :initform 0.0)
   (vx_var
    :reader vx_var
    :initarg :vx_var
    :type cl:float
    :initform 0.0)
   (vy_var
    :reader vy_var
    :initarg :vy_var
    :type cl:float
    :initform 0.0)
   (classification
    :reader classification
    :initarg :classification
    :type cl:fixnum
    :initform 0)
   (sizeX
    :reader sizeX
    :initarg :sizeX
    :type cl:float
    :initform 0.0)
   (sizeY
    :reader sizeY
    :initarg :sizeY
    :type cl:float
    :initform 0.0)
   (blinker_info
    :reader blinker_info
    :initarg :blinker_info
    :type cl:fixnum
    :initform 0))
)

(cl:defclass veh_object (<veh_object>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <veh_object>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'veh_object)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name erau_fusion_msgs-msg:<veh_object> is deprecated: use erau_fusion_msgs-msg:veh_object instead.")))

(cl:ensure-generic-function 'x-val :lambda-list '(m))
(cl:defmethod x-val ((m <veh_object>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader erau_fusion_msgs-msg:x-val is deprecated.  Use erau_fusion_msgs-msg:x instead.")
  (x m))

(cl:ensure-generic-function 'y-val :lambda-list '(m))
(cl:defmethod y-val ((m <veh_object>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader erau_fusion_msgs-msg:y-val is deprecated.  Use erau_fusion_msgs-msg:y instead.")
  (y m))

(cl:ensure-generic-function 'dx_var-val :lambda-list '(m))
(cl:defmethod dx_var-val ((m <veh_object>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader erau_fusion_msgs-msg:dx_var-val is deprecated.  Use erau_fusion_msgs-msg:dx_var instead.")
  (dx_var m))

(cl:ensure-generic-function 'dy_var-val :lambda-list '(m))
(cl:defmethod dy_var-val ((m <veh_object>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader erau_fusion_msgs-msg:dy_var-val is deprecated.  Use erau_fusion_msgs-msg:dy_var instead.")
  (dy_var m))

(cl:ensure-generic-function 'dx-val :lambda-list '(m))
(cl:defmethod dx-val ((m <veh_object>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader erau_fusion_msgs-msg:dx-val is deprecated.  Use erau_fusion_msgs-msg:dx instead.")
  (dx m))

(cl:ensure-generic-function 'dy-val :lambda-list '(m))
(cl:defmethod dy-val ((m <veh_object>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader erau_fusion_msgs-msg:dy-val is deprecated.  Use erau_fusion_msgs-msg:dy instead.")
  (dy m))

(cl:ensure-generic-function 'vx_var-val :lambda-list '(m))
(cl:defmethod vx_var-val ((m <veh_object>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader erau_fusion_msgs-msg:vx_var-val is deprecated.  Use erau_fusion_msgs-msg:vx_var instead.")
  (vx_var m))

(cl:ensure-generic-function 'vy_var-val :lambda-list '(m))
(cl:defmethod vy_var-val ((m <veh_object>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader erau_fusion_msgs-msg:vy_var-val is deprecated.  Use erau_fusion_msgs-msg:vy_var instead.")
  (vy_var m))

(cl:ensure-generic-function 'classification-val :lambda-list '(m))
(cl:defmethod classification-val ((m <veh_object>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader erau_fusion_msgs-msg:classification-val is deprecated.  Use erau_fusion_msgs-msg:classification instead.")
  (classification m))

(cl:ensure-generic-function 'sizeX-val :lambda-list '(m))
(cl:defmethod sizeX-val ((m <veh_object>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader erau_fusion_msgs-msg:sizeX-val is deprecated.  Use erau_fusion_msgs-msg:sizeX instead.")
  (sizeX m))

(cl:ensure-generic-function 'sizeY-val :lambda-list '(m))
(cl:defmethod sizeY-val ((m <veh_object>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader erau_fusion_msgs-msg:sizeY-val is deprecated.  Use erau_fusion_msgs-msg:sizeY instead.")
  (sizeY m))

(cl:ensure-generic-function 'blinker_info-val :lambda-list '(m))
(cl:defmethod blinker_info-val ((m <veh_object>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader erau_fusion_msgs-msg:blinker_info-val is deprecated.  Use erau_fusion_msgs-msg:blinker_info instead.")
  (blinker_info m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <veh_object>) ostream)
  "Serializes a message object of type '<veh_object>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'dx_var))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'dy_var))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'dx))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'dy))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'vx_var))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'vy_var))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'classification)) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'sizeX))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'sizeY))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'blinker_info)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <veh_object>) istream)
  "Deserializes a message object of type '<veh_object>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'x) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'y) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'dx_var) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'dy_var) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'dx) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'dy) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'vx_var) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'vy_var) (roslisp-utils:decode-single-float-bits bits)))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'classification)) (cl:read-byte istream))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'sizeX) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'sizeY) (roslisp-utils:decode-single-float-bits bits)))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'blinker_info)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<veh_object>)))
  "Returns string type for a message object of type '<veh_object>"
  "erau_fusion_msgs/veh_object")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'veh_object)))
  "Returns string type for a message object of type 'veh_object"
  "erau_fusion_msgs/veh_object")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<veh_object>)))
  "Returns md5sum for a message object of type '<veh_object>"
  "854e2d728659a600f851a5b56bc86a26")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'veh_object)))
  "Returns md5sum for a message object of type 'veh_object"
  "854e2d728659a600f851a5b56bc86a26")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<veh_object>)))
  "Returns full string definition for message of type '<veh_object>"
  (cl:format cl:nil "~%# Coordinate frames based on center of front fascia at ground level.~%# +x is forward, +y is left, +z is up~%~%# Position~%float32 x~%float32 y~%# Position Variance~%float32 dx_var~%float32 dy_var~%~%# Relative Velocity~%float32 dx~%float32 dy~%# Velocity Variance~%float32 vx_var~%float32 vy_var~%~%# Classification~%# 0 for Unknown~%# 1 for car~%# 2 for truck~%# 3 for pedestrian~%uint8 classification~%~%#Car Size~%float32 sizeX~%float32 sizeY~%~%#Blinker info (from ObstacleData.msg)~%# BLINKER_INFO_UNAVAILABLE = 0~%# BLINKER_INFO_OFF = 1~%# BLINKER_INFO_LEFT = 2~%# BLINKER_INFO_RIGHT = 3~%# BLINKER_INFO_BOTH = 4~%uint8 blinker_info~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'veh_object)))
  "Returns full string definition for message of type 'veh_object"
  (cl:format cl:nil "~%# Coordinate frames based on center of front fascia at ground level.~%# +x is forward, +y is left, +z is up~%~%# Position~%float32 x~%float32 y~%# Position Variance~%float32 dx_var~%float32 dy_var~%~%# Relative Velocity~%float32 dx~%float32 dy~%# Velocity Variance~%float32 vx_var~%float32 vy_var~%~%# Classification~%# 0 for Unknown~%# 1 for car~%# 2 for truck~%# 3 for pedestrian~%uint8 classification~%~%#Car Size~%float32 sizeX~%float32 sizeY~%~%#Blinker info (from ObstacleData.msg)~%# BLINKER_INFO_UNAVAILABLE = 0~%# BLINKER_INFO_OFF = 1~%# BLINKER_INFO_LEFT = 2~%# BLINKER_INFO_RIGHT = 3~%# BLINKER_INFO_BOTH = 4~%uint8 blinker_info~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <veh_object>))
  (cl:+ 0
     4
     4
     4
     4
     4
     4
     4
     4
     1
     4
     4
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <veh_object>))
  "Converts a ROS message object to a list"
  (cl:list 'veh_object
    (cl:cons ':x (x msg))
    (cl:cons ':y (y msg))
    (cl:cons ':dx_var (dx_var msg))
    (cl:cons ':dy_var (dy_var msg))
    (cl:cons ':dx (dx msg))
    (cl:cons ':dy (dy msg))
    (cl:cons ':vx_var (vx_var msg))
    (cl:cons ':vy_var (vy_var msg))
    (cl:cons ':classification (classification msg))
    (cl:cons ':sizeX (sizeX msg))
    (cl:cons ':sizeY (sizeY msg))
    (cl:cons ':blinker_info (blinker_info msg))
))
