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

class CanBus {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.CarSpeed = null;
    }
    else {
      if (initObj.hasOwnProperty('CarSpeed')) {
        this.CarSpeed = initObj.CarSpeed
      }
      else {
        this.CarSpeed = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type CanBus
    // Serialize message field [CarSpeed]
    bufferOffset = _serializer.float32(obj.CarSpeed, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type CanBus
    let len;
    let data = new CanBus(null);
    // Deserialize message field [CarSpeed]
    data.CarSpeed = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'erau_fusion_msgs/CanBus';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'dc1a7c020ca7ccfab53c9facec5520c4';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 CarSpeed
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new CanBus(null);
    if (msg.CarSpeed !== undefined) {
      resolved.CarSpeed = msg.CarSpeed;
    }
    else {
      resolved.CarSpeed = 0.0
    }

    return resolved;
    }
};

module.exports = CanBus;
