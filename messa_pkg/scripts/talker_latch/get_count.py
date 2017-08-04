#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

def callback(msg):
    #pass
    print msg.data

rospy.init_node('node_get_count')
sub = rospy.Subscriber('counter', Int32, callback)
rospy.spin()
