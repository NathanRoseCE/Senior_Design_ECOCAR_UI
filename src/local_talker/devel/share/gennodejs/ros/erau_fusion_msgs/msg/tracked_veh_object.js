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

//-----------------------------------------------------------

class tracked_veh_object {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.object = null;
      this.id = null;
      this.object_age = null;
      this.lane = null;
    }
    else {
      if (initObj.hasOwnProperty('object')) {
        this.object = initObj.object
      }
      else {
        this.object = new veh_object();
      }
      if (initObj.hasOwnProperty('id')) {
        this.id = initObj.id
      }
      else {
        this.id = 0;
      }
      if (initObj.hasOwnProperty('object_age')) {
        this.object_age = initObj.object_age
      }
      else {
        this.object_age = 0;
      }
      if (initObj.hasOwnProperty('lane')) {
        this.lane = initObj.lane
      }
      else {
        this.lane = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type tracked_veh_object
    // Serialize message field [object]
    bufferOffset = veh_object.serialize(obj.object, buffer, bufferOffset);
    // Serialize message field [id]
    bufferOffset = _serializer.uint8(obj.id, buffer, bufferOffset);
    // Serialize message field [object_age]
    bufferOffset = _serializer.uint16(obj.object_age, buffer, bufferOffset);
    // Serialize message field [lane]
    bufferOffset = _serializer.uint8(obj.lane, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type tracked_veh_object
    let len;
    let data = new tracked_veh_object(null);
    // Deserialize message field [object]
    data.object = veh_object.deserialize(buffer, bufferOffset);
    // Deserialize message field [id]
    data.id = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [object_age]
    data.object_age = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [lane]
    data.lane = _deserializer.uint8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 46;
  }

  static datatype() {
    // Returns string type for a message object
    return 'erau_fusion_msgs/tracked_veh_object';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '0eaf4f33ea0e60aee406a700d7cb793e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    erau_fusion_msgs/veh_object object
    
    uint8 id # unique identifier to this object; should remain constant for this object over time
    uint16 object_age  # total time this vehicle has been tracked for (in seconds)
    
    # Lane assignment
    # 0 - Unknown
    # 1 - Left
    # 2 - Host/center
    # 3 - Right
    uint8 lane
    
    # TODO add tracks
    
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
    const resolved = new tracked_veh_object(null);
    if (msg.object !== undefined) {
      resolved.object = veh_object.Resolve(msg.object)
    }
    else {
      resolved.object = new veh_object()
    }

    if (msg.id !== undefined) {
      resolved.id = msg.id;
    }
    else {
      resolved.id = 0
    }

    if (msg.object_age !== undefined) {
      resolved.object_age = msg.object_age;
    }
    else {
      resolved.object_age = 0
    }

    if (msg.lane !== undefined) {
      resolved.lane = msg.lane;
    }
    else {
      resolved.lane = 0
    }

    return resolved;
    }
};

module.exports = tracked_veh_object;
