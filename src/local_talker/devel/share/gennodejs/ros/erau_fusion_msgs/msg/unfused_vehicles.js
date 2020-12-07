// Auto-generated. Do not edit!

// (in-package erau_fusion_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let veh_object = require('./veh_object.js');
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class unfused_vehicles {
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
        this.objects = new Array(32).fill(new veh_object());
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type unfused_vehicles
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Check that the constant length array field [objects] has the right length
    if (obj.objects.length !== 32) {
      throw new Error('Unable to serialize array field objects - length must be 32')
    }
    // Serialize message field [objects]
    obj.objects.forEach((val) => {
      bufferOffset = veh_object.serialize(val, buffer, bufferOffset);
    });
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type unfused_vehicles
    let len;
    let data = new unfused_vehicles(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [objects]
    len = 32;
    data.objects = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.objects[i] = veh_object.deserialize(buffer, bufferOffset)
    }
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 1344;
  }

  static datatype() {
    // Returns string type for a message object
    return 'erau_fusion_msgs/unfused_vehicles';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '684bc5fc33bc46adb1a1a5655fe0e25f';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    std_msgs/Header header
    erau_fusion_msgs/veh_object[32] objects
    
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
    MSG: erau_fusion_msgs/veh_object
    
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new unfused_vehicles(null);
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
          resolved.objects[i] = veh_object.Resolve(msg.objects[i]);
        }
        else {
          resolved.objects[i] = new veh_object();
        }
      }
    }
    else {
      resolved.objects = new Array(32).fill(new veh_object())
    }

    return resolved;
    }
};

module.exports = unfused_vehicles;
