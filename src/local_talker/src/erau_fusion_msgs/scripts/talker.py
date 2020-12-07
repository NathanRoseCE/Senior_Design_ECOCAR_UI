#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
import std_msgs.msg
from erau_fusion_msgs.msg import Tracked_Lane
from erau_fusion_msgs.msg import veh_object
from erau_fusion_msgs.msg import Tracked_Lane_Object
from erau_fusion_msgs.msg import tracked_veh_object
from erau_fusion_msgs.msg import tracked_vehicles
from erau_fusion_msgs.msg import unfused_vehicles
from erau_fusion_msgs.msg import CanBus
from listener import msg
from listener import mes_tracked_veh_object

def talker():
    data = Tracked_Lane()
    data_tracked_veh_object = Tracked_Lane_Object()

    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    pub_Tracked_Lane = rospy.Publisher('chatter', Tracked_Lane, queue_size=10)
    pub_veh_object = rospy.Publisher('veh_object_chatter', veh_object, queue_size=10)
    pub_Tracked_Lane_Object = rospy.Publisher('Tracked_Lane_Object_chatter', Tracked_Lane_Object, queue_size=10)
    pub_tracked_veh_object = rospy.Publisher('tracked_veh_object_chatter', tracked_veh_object, queue_size=10)
    pub_tracked_vehicles = rospy.Publisher('tracked_vehicles_chatter', tracked_vehicles, queue_size=10)
    pub_unfused_vehicles = rospy.Publisher('unfused_vehicles_chatter', unfused_vehicles, queue_size=10)
    pub_CanBus = rospy.Publisher('CanBus_chatter', CanBus, queue_size=10)

    while not rospy.is_shutdown():

        data = Tracked_Lane()
   	data.lane_type_Left = msg.lane_type_Left
    	data.lane_type_Right = msg.lane_type_Right
    	data.lanePosition = msg.lanePosition
    	data.laneWidth = msg.laneWidth
    	data.position_parameter = msg.position_parameter
        rospy.loginfo(data)
        pub_Tracked_Lane.publish(data)

        msg_veh_object = veh_object()
   	msg_veh_object.x = 0
    	msg_veh_object.y = 0
    	msg_veh_object.dx_var = 0
    	msg_veh_object.dy_var = 0
    	msg_veh_object.dx = 0
    	msg_veh_object.dy = 0
    	msg_veh_object.vx_var = 0
    	msg_veh_object.vy_var = 0
    	msg_veh_object.classification = 0
    	msg_veh_object.sizeX = 0
    	msg_veh_object.sizeY = 0
    	msg_veh_object.blinker_info = 0
        rospy.loginfo(msg_veh_object)
        pub_veh_object.publish(msg_veh_object)

        mes_Tracked_Lane_Object = Tracked_Lane_Object()
        mes_Tracked_Lane_Object.header.stamp = rospy.Time.now()
        mes_Tracked_Lane_Object.header.frame_id = "Tracked Lane Object"
        mes_Tracked_Lane_Object.objects = [Tracked_Lane(), Tracked_Lane(), Tracked_Lane(), Tracked_Lane(), Tracked_Lane(), Tracked_Lane(), Tracked_Lane(), Tracked_Lane(), Tracked_Lane(), Tracked_Lane(), Tracked_Lane(), Tracked_Lane(), Tracked_Lane(), Tracked_Lane(), Tracked_Lane(), Tracked_Lane(), Tracked_Lane(), Tracked_Lane(), Tracked_Lane(), Tracked_Lane(), Tracked_Lane(), Tracked_Lane(), Tracked_Lane(), Tracked_Lane(), Tracked_Lane(), Tracked_Lane(), Tracked_Lane(), Tracked_Lane(), Tracked_Lane(), Tracked_Lane(), Tracked_Lane(), Tracked_Lane()]
	rospy.loginfo(mes_Tracked_Lane_Object)
        pub_Tracked_Lane_Object.publish(mes_Tracked_Lane_Object)

        data_tracked_veh_object = tracked_veh_object()
        data_tracked_veh_object.object = veh_object()
	data_tracked_veh_object.object.x = mes_tracked_veh_object.object.x
	data_tracked_veh_object.object.y = mes_tracked_veh_object.object.y
	data_tracked_veh_object.object.dx = mes_tracked_veh_object.object.dx
	data_tracked_veh_object.object.dy = mes_tracked_veh_object.object.dy
	data_tracked_veh_object.object.sizeX = mes_tracked_veh_object.object.sizeX
	data_tracked_veh_object.object.sizeY = mes_tracked_veh_object.object.sizeY
	data_tracked_veh_object.object.blinker_info = mes_tracked_veh_object.object.blinker_info
	data_tracked_veh_object.object.classification = mes_tracked_veh_object.object.classification
        data_tracked_veh_object.id = mes_tracked_veh_object.id
        data_tracked_veh_object.object_age = mes_tracked_veh_object.object_age
        data_tracked_veh_object.lane = mes_tracked_veh_object.lane
	rospy.loginfo(data_tracked_veh_object)
        pub_tracked_veh_object.publish(data_tracked_veh_object)

        mes_tracked_vehicles = tracked_vehicles()
        mes_tracked_vehicles.header.stamp = rospy.Time.now()
        mes_tracked_vehicles.header.frame_id = "Tracked Vehicles"
        mes_tracked_vehicles.objects = [tracked_veh_object(),tracked_veh_object(), tracked_veh_object(), tracked_veh_object(),tracked_veh_object(), tracked_veh_object(), tracked_veh_object(), tracked_veh_object(), tracked_veh_object(), tracked_veh_object(), tracked_veh_object(), tracked_veh_object(), tracked_veh_object(), tracked_veh_object(), tracked_veh_object(), tracked_veh_object(), tracked_veh_object(), tracked_veh_object(), tracked_veh_object(), tracked_veh_object(), tracked_veh_object(), tracked_veh_object(), tracked_veh_object(), tracked_veh_object(), tracked_veh_object(), tracked_veh_object(), tracked_veh_object(), tracked_veh_object(), tracked_veh_object(), tracked_veh_object(), tracked_veh_object(), tracked_veh_object()]
	rospy.loginfo(mes_tracked_vehicles)
        pub_tracked_vehicles.publish(mes_tracked_vehicles)

        mes_unfused_vehicles = unfused_vehicles()
        mes_unfused_vehicles.header.stamp = rospy.Time.now()
        mes_unfused_vehicles.header.frame_id = "Unfused Vehicles"
        mes_unfused_vehicles.objects = [veh_object(), veh_object(), veh_object(), veh_object(), veh_object(), veh_object(), veh_object(), veh_object(), veh_object(), veh_object(), veh_object(), veh_object(), veh_object(), veh_object(), veh_object(), veh_object(), veh_object(), veh_object(), veh_object(), veh_object(), veh_object(), veh_object(), veh_object(), veh_object(), veh_object(), veh_object(), veh_object(), veh_object(), veh_object(), veh_object(), veh_object(), veh_object()]
	rospy.loginfo(mes_unfused_vehicles)
        pub_unfused_vehicles.publish(mes_unfused_vehicles)

   	msg_CanBus = CanBus()
   	msg_CanBus.CarSpeed = 45
        rospy.loginfo(msg_CanBus)
        pub_CanBus.publish(msg_CanBus)

        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
