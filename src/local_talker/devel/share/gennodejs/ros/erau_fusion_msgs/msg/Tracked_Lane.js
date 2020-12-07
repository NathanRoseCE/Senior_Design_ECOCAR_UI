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

class Tracked_Lane {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.lane_type_Left = null;
      this.lane_type_Right = null;
      this.lanePosition = null;
      this.laneWidth = null;
      this.position_parameter = null;
    }
    else {
      if (initObj.hasOwnProperty('lane_type_Left')) {
        this.lane_type_Left = initObj.lane_type_Left
      }
      else {
        this.lane_type_Left = 0;
      }
      if (initObj.hasOwnProperty('lane_type_Right')) {
        this.lane_type_Right = initObj.lane_type_Right
      }
      else {
        this.lane_type_Right = 0;
      }
      if (initObj.hasOwnProperty('lanePosition')) {
        this.lanePosition = initObj.lanePosition
      }
      else {
        this.lanePosition = 0;
      }
      if (initObj.hasOwnProperty('laneWidth')) {
        this.laneWidth = initObj.laneWidth
      }
      else {
        this.laneWidth = 0;
      }
      if (initObj.hasOwnProperty('position_parameter')) {
        this.position_parameter = initObj.position_parameter
      }
      else {
        this.position_parameter = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Tracked_Lane
    // Serialize message field [lane_type_Left]
    bufferOffset = _serializer.uint8(obj.lane_type_Left, buffer, bufferOffset);
    // Serialize message field [lane_type_Right]
    bufferOffset = _serializer.uint8(obj.lane_type_Right, buffer, bufferOffset);
    // Serialize message field [lanePosition]
    bufferOffset = _serializer.uint8(obj.lanePosition, buffer, bufferOffset);
    // Serialize message field [laneWidth]
    bufferOffset = _serializer.uint8(obj.laneWidth, buffer, bufferOffset);
    // Serialize message field [position_parameter]
    bufferOffset = _serializer.float64(obj.position_parameter, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Tracked_Lane
    let len;
    let data = new Tracked_Lane(null);
    // Deserialize message field [lane_type_Left]
    data.lane_type_Left = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [lane_type_Right]
    data.lane_type_Right = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [lanePosition]
    data.lanePosition = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [laneWidth]
    data.laneWidth = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [position_parameter]
    data.position_parameter = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 12;
  }

  static datatype() {
    // Returns string type for a message object
    return 'erau_fusion_msgs/Tracked_Lane';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '14f981197f8d751c83fad6e1038cf6df';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
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
    const resolved = new Tracked_Lane(null);
    if (msg.lane_type_Left !== undefined) {
      resolved.lane_type_Left = msg.lane_type_Left;
    }
    else {
      resolved.lane_type_Left = 0
    }

    if (msg.lane_type_Right !== undefined) {
      resolved.lane_type_Right = msg.lane_type_Right;
    }
    else {
      resolved.lane_type_Right = 0
    }

    if (msg.lanePosition !== undefined) {
      resolved.lanePosition = msg.lanePosition;
    }
    else {
      resolved.lanePosition = 0
    }

    if (msg.laneWidth !== undefined) {
      resolved.laneWidth = msg.laneWidth;
    }
    else {
      resolved.laneWidth = 0
    }

    if (msg.position_parameter !== undefined) {
      resolved.position_parameter = msg.position_parameter;
    }
    else {
      resolved.position_parameter = 0.0
    }

    return resolved;
    }
};

module.exports = Tracked_Lane;
