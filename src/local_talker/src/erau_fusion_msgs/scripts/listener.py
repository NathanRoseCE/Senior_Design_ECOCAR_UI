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

## Simple talker demo that listens to std_msgs/Strings published 
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

msg = Tracked_Lane() 
mes_tracked_veh_object = tracked_veh_object()


def callback(data):
    ## rospy.loginfo("Lane Type Left: %u \nLane Type Right: %u \nLane Positon: %u \nLane Width: %u \nPositon Parameter: %f \n\n" % (data.lane_type_Left, data.lane_type_Right, data.lanePosition, data.laneWidth, data.position_parameter))
    msg.lane_type_Left = data.lane_type_Left
    msg.lane_type_Right = data.lane_type_Right
    msg.lanePosition = data.lanePosition
    msg.laneWidth = data.laneWidth
    msg.position_parameter = data.position_parameter
    print ("Lane Type Left: %u \nLane Type Right: %u \nLane Positon: %u \nLane Width: %u \nPositon Parameter: %f \n\n" % (data.lane_type_Left, data.lane_type_Right, data.lanePosition, data.laneWidth, data.position_parameter))
  
def callback_veh_object(data_veh_object):
    ## rospy.loginfo("Position x: %f \nPosition y: %f \nPosition Variance dx_var: %f \nPosition Variance dy_var: %f \nPosition dx: %f \nPosition dy: %f \nPosition Variance vx_var: %f \nPosition Variance vy_var: %f \nClassification: %u \nCar Size sizeX: %f \nCar Size sizeY: %f \nBlinker info: %u\n\n" % (data_veh_object.x, data_veh_object.y, data_veh_object.dx_var, data_veh_object.dy_var, data_veh_object.dx, data_veh_object.dy, data_veh_object.vx_var, data_veh_object.vy_var, data_veh_object.classification, data_veh_object.sizeX, data_veh_object.sizeY, data_veh_object.blinker_info))
   print ("callback veh object called")

def callback_Tracked_Lane_Object(data_Tracked_Lane_Object):
    ## rospy.loginfo("Header seq: %u \nHeader time: %s \nHeader frame_id: %s \n" % (data_Tracked_Lane_Object.header.seq, data_Tracked_Lane_Object.header.stamp, data_Tracked_Lane_Object.header.frame_id))
    # loginfo for list of Tracked_Lane objects
    ## for i in range (0,31):
	## rospy.loginfo("Tracked Lane Object %u \n   Lane Type Left: %u \n   Lane Type Right: %u \n   Lane Positon: %u \n   Lane Width: %u \n   Positon Parameter: %f \n\n" % (i, data_Tracked_Lane_Object.objects[i].lane_type_Left, data_Tracked_Lane_Object.objects[i].lane_type_Right, data_Tracked_Lane_Object.objects[i].lanePosition, data_Tracked_Lane_Object.objects[i].laneWidth, data_Tracked_Lane_Object.objects[i].position_parameter))
   print ("callback tracked lane object called")

def callback_tracked_veh_object(data_tracked_veh_object):
    ## rospy.loginfo("Object created by tracked_veh_object: \nPosition x: %f \nPosition y: %f \nPosition Variance dx_var: %f \nPosition Variance dy_var: %f \nPosition dx: %f \nPosition dy: %f \nPosition Variance vx_var: %f \nPosition Variance vy_var: %f \nClassification: %u \nCar Size sizeX: %f \nCar Size sizeY: %f \nBlinker info: %u \nID: %u \nObject Age: %u\nLane: %u\n\n" % (data_tracked_veh_object.object.x, data_tracked_veh_object.object.y, data_tracked_veh_object.object.dx_var, data_tracked_veh_object.object.dy_var, data_tracked_veh_object.object.dx, data_tracked_veh_object.object.dy, data_tracked_veh_object.object.vx_var, data_tracked_veh_object.object.vy_var, data_tracked_veh_object.object.classification, data_tracked_veh_object.object.sizeX, data_tracked_veh_object.object.sizeY, data_tracked_veh_object.object.blinker_info,data_tracked_veh_object.id, data_tracked_veh_object.object_age, data_tracked_veh_object.lane))
    mes_tracked_veh_object.object = veh_object()
    mes_tracked_veh_object.object.x = data_tracked_veh_object.object.x
    mes_tracked_veh_object.object.y = data_tracked_veh_object.object.y
    mes_tracked_veh_object.object.dx = data_tracked_veh_object.object.dx
    mes_tracked_veh_object.object.dy = data_tracked_veh_object.object.dy
    mes_tracked_veh_object.object.sizeX = data_tracked_veh_object.object.sizeX
    mes_tracked_veh_object.object.sizeY = data_tracked_veh_object.object.sizeY
    mes_tracked_veh_object.object.blinker_info = data_tracked_veh_object.object.blinker_info
    mes_tracked_veh_object.object.classification = data_tracked_veh_object.object.classification
    mes_tracked_veh_object.id = data_tracked_veh_object.id
    mes_tracked_veh_object.lane = data_tracked_veh_object.lane
    print ("Object created by tracked_veh_object: \nPosition x: %f \nPosition y: %f \nPosition Variance dx_var: %f \nPosition Variance dy_var: %f \nPosition dx: %f \nPosition dy: %f \nPosition Variance vx_var: %f \nPosition Variance vy_var: %f \nClassification: %u \nCar Size sizeX: %f \nCar Size sizeY: %f \nBlinker info: %u \nID: %u \nObject Age: %u\nLane: %u\n\n" % (data_tracked_veh_object.object.x, data_tracked_veh_object.object.y, data_tracked_veh_object.object.dx_var, data_tracked_veh_object.object.dy_var, data_tracked_veh_object.object.dx, data_tracked_veh_object.object.dy, data_tracked_veh_object.object.vx_var, data_tracked_veh_object.object.vy_var, data_tracked_veh_object.object.classification, data_tracked_veh_object.object.sizeX, data_tracked_veh_object.object.sizeY, data_tracked_veh_object.object.blinker_info,data_tracked_veh_object.id, data_tracked_veh_object.object_age, data_tracked_veh_object.lane))

def callback_tracked_vehicles(data_tracked_vehicles):
    ## rospy.loginfo("Header seq: %u \nHeader time: %s \nHeader frame_id: %s \n" % (data_tracked_vehicles.header.seq, data_tracked_vehicles.header.stamp, data_tracked_vehicles.header.frame_id))
    # loginfo for list of veh_object objects
    ## for x in range (0,31):
	## rospy.loginfo("Object created by tracked_vehicle: %u\nPosition x: %f \nPosition y: %f \nPosition Variance dx_var: %f \nPosition Variance dy_var: %f \nPosition dx: %f \nPosition dy: %f \nPosition Variance vx_var: %f \nPosition Variance vy_var: %f \nClassification: %u \nCar Size sizeX: %f \nCar Size sizeY: %f \nBlinker info: %u \nID: %u \nObject Age: %u\nLane: %u\n\n" % (x, data_tracked_vehicles.objects[x].object.x, data_tracked_vehicles.objects[x].object.y, data_tracked_vehicles.objects[x].object.dx_var, data_tracked_vehicles.objects[x].object.dy_var, data_tracked_vehicles.objects[x].object.dx, data_tracked_vehicles.objects[x].object.dy, data_tracked_vehicles.objects[x].object.vx_var, data_tracked_vehicles.objects[x].object.vy_var, data_tracked_vehicles.objects[x].object.classification, data_tracked_vehicles.objects[x].object.sizeX, data_tracked_vehicles.objects[x].object.sizeY, data_tracked_vehicles.objects[x].object.blinker_info,data_tracked_vehicles.objects[x].id, data_tracked_vehicles.objects[x].object_age, data_tracked_vehicles.objects[x].lane))
   print ("callback tracked vehicles called")

def callback_unfused_vehicles(data_unfused_vehicles):
    ## rospy.loginfo("Header seq: %u \nHeader time: %s \nHeader frame_id: %s \n" % (data_unfused_vehicles.header.seq, data_unfused_vehicles.header.stamp, data_unfused_vehicles.header.frame_id))
    # loginfo for list of veh_object objects
    ## for y in range (0,31):
	## rospy.loginfo("Object created by unfused_vehicle: %u\nPosition x: %f \nPosition y: %f \nPosition Variance dx_var: %f \nPosition Variance dy_var: %f \nPosition dx: %f \nPosition dy: %f \nPosition Variance vx_var: %f \nPosition Variance vy_var: %f \nClassification: %u \nCar Size sizeX: %f \nCar Size sizeY: %f \nBlinker info: %u \n\n" % (y, data_unfused_vehicles.objects[y].x, data_unfused_vehicles.objects[y].y, data_unfused_vehicles.objects[y].dx_var, data_unfused_vehicles.objects[y].dy_var, data_unfused_vehicles.objects[y].dx, data_unfused_vehicles.objects[y].dy, data_unfused_vehicles.objects[y].vx_var, data_unfused_vehicles.objects[y].vy_var, data_unfused_vehicles.objects[y].classification, data_unfused_vehicles.objects[y].sizeX, data_unfused_vehicles.objects[y].sizeY, data_unfused_vehicles.objects[y].blinker_info))
   print ("callback unfused vehicles called")

def callback_CanBus(data_CanBus):
    ## rospy.loginfo("Car Speed: %f \n\n" % (data_CanBus.CarSpeed))
   print ("callback canbus called")

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('chatter', Tracked_Lane, callback)

    rospy.Subscriber('veh_object_chatter', veh_object, callback_veh_object)
    rospy.Subscriber('Tracked_Lane_Object_chatter', Tracked_Lane_Object, callback_Tracked_Lane_Object)

    rospy.Subscriber('tracked_veh_object_chatter', tracked_veh_object, callback_tracked_veh_object)

    rospy.Subscriber('tracked_vehicles_chatter', tracked_vehicles, callback_tracked_vehicles)
    rospy.Subscriber('unfused_vehicles_chatter', unfused_vehicles, callback_unfused_vehicles)
    rospy.Subscriber('CanBus_chatter', CanBus, callback_CanBus)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
