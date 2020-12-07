// Auto-generated. Do not edit!

// (in-package erau_fusion_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let Tracked_Lane = require('./Tracked_Lane.js');
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class Tracked_Lane_Object {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.objects = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('objects')) {
        this.objects = initObj.objects
      }
      else {
        this.objects = new Array(32).fill(new Tracked_Lane());
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Tracked_Lane_Object
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Check that the constant length array field [objects] has the right length
    if (obj.objects.length !== 32) {
      throw new Error('Unable to serialize array field objects - length must be 32')
    }
    // Serialize message field [objects]
    obj.objects.forEach((val) => {
      bufferOffset = Tracked_Lane.serialize(val, buffer, bufferOffset);
    });
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Tracked_Lane_Object
    let len;
    let data = new Tracked_Lane_Object(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [objects]
    len = 32;
    data.objects = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.objects[i] = Tracked_Lane.deserialize(buffer, bufferOffset)
    }
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 384;
  }

  static datatype() {
    // Returns string type for a message object
    return 'erau_fusion_msgs/Tracked_Lane_Object';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'a320a79d93ffd064ef7141dc8e5a6c89';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    std_msgs/Header header
    erau_fusion_msgs/Tracked_Lane[32] objects
    
    ================================================================================
    MSG: std_msgs/Header
    # Standard metadata for higher-level stamped data types.
    # This is generally used to communicate timestamped data 
    # in a particular coordinate frame.
    # 
    # sequence ID: consecutively increasing ID 
    uint32 seq
    #Two-integer timestamp that is expressed as:
    # * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
    # * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
    # time-handling sugar is provided by the client library
    time stamp
    #Frame this data is associated with
    # 0: no frame
    # 1: global frame
    string frame_id
    
    ================================================================================
    MSG: erau_fusion_msgs/Tracked_Lane
    #Lane info from LkaLane msg
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Tracked_Lane_Object(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.objects !== undefined) {
      resolved.objects = new Array(32)
      for (let i = 0; i < resolved.objects.length; ++i) {
        if (msg.objects.length > i) {
          resolved.objects[i] = Tracked_Lane.Resolve(msg.objects[i]);
        }
        else {
          resolved.objects[i] = new Tracked_Lane();
        }
      }
    }
    else {
      resolved.objects = new Array(32).fill(new Tracked_Lane())
    }

    return resolved;
    }
};

module.exports = Tracked_Lane_Object;
