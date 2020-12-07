// Auto-generated. Do not edit!

// (in-package erau_fusion_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class veh_object {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.x = null;
      this.y = null;
      this.dx_var = null;
      this.dy_var = null;
      this.dx = null;
      this.dy = null;
      this.vx_var = null;
      this.vy_var = null;
      this.classification = null;
      this.sizeX = null;
      this.sizeY = null;
      this.blinker_info = null;
    }
    else {
      if (initObj.hasOwnProperty('x')) {
        this.x = initObj.x
      }
      else {
        this.x = 0.0;
      }
      if (initObj.hasOwnProperty('y')) {
        this.y = initObj.y
      }
      else {
        this.y = 0.0;
      }
      if (initObj.hasOwnProperty('dx_var')) {
        this.dx_var = initObj.dx_var
      }
      else {
        this.dx_var = 0.0;
      }
      if (initObj.hasOwnProperty('dy_var')) {
        this.dy_var = initObj.dy_var
      }
      else {
        this.dy_var = 0.0;
      }
      if (initObj.hasOwnProperty('dx')) {
        this.dx = initObj.dx
      }
      else {
        this.dx = 0.0;
      }
      if (initObj.hasOwnProperty('dy')) {
        this.dy = initObj.dy
      }
      else {
        this.dy = 0.0;
      }
      if (initObj.hasOwnProperty('vx_var')) {
        this.vx_var = initObj.vx_var
      }
      else {
        this.vx_var = 0.0;
      }
      if (initObj.hasOwnProperty('vy_var')) {
        this.vy_var = initObj.vy_var
      }
      else {
        this.vy_var = 0.0;
      }
      if (initObj.hasOwnProperty('classification')) {
        this.classification = initObj.classification
      }
      else {
        this.classification = 0;
      }
      if (initObj.hasOwnProperty('sizeX')) {
        this.sizeX = initObj.sizeX
      }
      else {
        this.sizeX = 0.0;
      }
      if (initObj.hasOwnProperty('sizeY')) {
        this.sizeY = initObj.sizeY
      }
      else {
        this.sizeY = 0.0;
      }
      if (initObj.hasOwnProperty('blinker_info')) {
        this.blinker_info = initObj.blinker_info
      }
      else {
        this.blinker_info = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type veh_object
    // Serialize message field [x]
    bufferOffset = _serializer.float32(obj.x, buffer, bufferOffset);
    // Serialize message field [y]
    bufferOffset = _serializer.float32(obj.y, buffer, bufferOffset);
    // Serialize message field [dx_var]
    bufferOffset = _serializer.float32(obj.dx_var, buffer, bufferOffset);
    // Serialize message field [dy_var]
    bufferOffset = _serializer.float32(obj.dy_var, buffer, bufferOffset);
    // Serialize message field [dx]
    bufferOffset = _serializer.float32(obj.dx, buffer, bufferOffset);
    // Serialize message field [dy]
    bufferOffset = _serializer.float32(obj.dy, buffer, bufferOffset);
    // Serialize message field [vx_var]
    bufferOffset = _serializer.float32(obj.vx_var, buffer, bufferOffset);
    // Serialize message field [vy_var]
    bufferOffset = _serializer.float32(obj.vy_var, buffer, bufferOffset);
    // Serialize message field [classification]
    bufferOffset = _serializer.uint8(obj.classification, buffer, bufferOffset);
    // Serialize message field [sizeX]
    bufferOffset = _serializer.float32(obj.sizeX, buffer, bufferOffset);
    // Serialize message field [sizeY]
    bufferOffset = _serializer.float32(obj.sizeY, buffer, bufferOffset);
    // Serialize message field [blinker_info]
    bufferOffset = _serializer.uint8(obj.blinker_info, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type veh_object
    let len;
    let data = new veh_object(null);
    // Deserialize message field [x]
    data.x = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [y]
    data.y = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [dx_var]
    data.dx_var = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [dy_var]
    data.dy_var = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [dx]
    data.dx = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [dy]
    data.dy = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [vx_var]
    data.vx_var = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [vy_var]
    data.vy_var = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [classification]
    data.classification = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [sizeX]
    data.sizeX = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [sizeY]
    data.sizeY = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [blinker_info]
    data.blinker_info = _deserializer.uint8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 42;
  }

  static datatype() {
    // Returns string type for a message object
    return 'erau_fusion_msgs/veh_object';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '854e2d728659a600f851a5b56bc86a26';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
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
    const resolved = new veh_object(null);
    if (msg.x !== undefined) {
      resolved.x = msg.x;
    }
    else {
      resolved.x = 0.0
    }

    if (msg.y !== undefined) {
      resolved.y = msg.y;
    }
    else {
      resolved.y = 0.0
    }

    if (msg.dx_var !== undefined) {
      resolved.dx_var = msg.dx_var;
    }
    else {
      resolved.dx_var = 0.0
    }

    if (msg.dy_var !== undefined) {
      resolved.dy_var = msg.dy_var;
    }
    else {
      resolved.dy_var = 0.0
    }

    if (msg.dx !== undefined) {
      resolved.dx = msg.dx;
    }
    else {
      resolved.dx = 0.0
    }

    if (msg.dy !== undefined) {
      resolved.dy = msg.dy;
    }
    else {
      resolved.dy = 0.0
    }

    if (msg.vx_var !== undefined) {
      resolved.vx_var = msg.vx_var;
    }
    else {
      resolved.vx_var = 0.0
    }

    if (msg.vy_var !== undefined) {
      resolved.vy_var = msg.vy_var;
    }
    else {
      resolved.vy_var = 0.0
    }

    if (msg.classification !== undefined) {
      resolved.classification = msg.classification;
    }
    else {
      resolved.classification = 0
    }

    if (msg.sizeX !== undefined) {
      resolved.sizeX = msg.sizeX;
    }
    else {
      resolved.sizeX = 0.0
    }

    if (msg.sizeY !== undefined) {
      resolved.sizeY = msg.sizeY;
    }
    else {
      resolved.sizeY = 0.0
    }

    if (msg.blinker_info !== undefined) {
      resolved.blinker_info = msg.blinker_info;
    }
    else {
      resolved.blinker_info = 0
    }

    return resolved;
    }
};

module.exports = veh_object;
