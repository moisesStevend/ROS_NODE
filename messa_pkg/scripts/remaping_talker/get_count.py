#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

def callback(msg):
    #pass
    print msg.data

rospy.init_node('node_get_count')
sub = rospy.Subscriber('counter_otro', Int32, callback)
rospy.spin()


# $ rosrun messa_pkg get_count.py counter_otro:=counter
