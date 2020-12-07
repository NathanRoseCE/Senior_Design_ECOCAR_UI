# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from erau_fusion_msgs/Tracked_Lane.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class Tracked_Lane(genpy.Message):
  _md5sum = "14f981197f8d751c83fad6e1038cf6df"
  _type = "erau_fusion_msgs/Tracked_Lane"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """#Lane info from LkaLane msg
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
"""
  __slots__ = ['lane_type_Left','lane_type_Right','lanePosition','laneWidth','position_parameter']
  _slot_types = ['uint8','uint8','uint8','uint8','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       lane_type_Left,lane_type_Right,lanePosition,laneWidth,position_parameter

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Tracked_Lane, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.lane_type_Left is None:
        self.lane_type_Left = 0
      if self.lane_type_Right is None:
        self.lane_type_Right = 0
      if self.lanePosition is None:
        self.lanePosition = 0
      if self.laneWidth is None:
        self.laneWidth = 0
      if self.position_parameter is None:
        self.position_parameter = 0.
    else:
      self.lane_type_Left = 0
      self.lane_type_Right = 0
      self.lanePosition = 0
      self.laneWidth = 0
      self.position_parameter = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_4Bd().pack(_x.lane_type_Left, _x.lane_type_Right, _x.lanePosition, _x.laneWidth, _x.position_parameter))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 12
      (_x.lane_type_Left, _x.lane_type_Right, _x.lanePosition, _x.laneWidth, _x.position_parameter,) = _get_struct_4Bd().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_4Bd().pack(_x.lane_type_Left, _x.lane_type_Right, _x.lanePosition, _x.laneWidth, _x.position_parameter))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 12
      (_x.lane_type_Left, _x.lane_type_Right, _x.lanePosition, _x.laneWidth, _x.position_parameter,) = _get_struct_4Bd().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_4Bd = None
def _get_struct_4Bd():
    global _struct_4Bd
    if _struct_4Bd is None:
        _struct_4Bd = struct.Struct("<4Bd")
    return _struct_4Bd