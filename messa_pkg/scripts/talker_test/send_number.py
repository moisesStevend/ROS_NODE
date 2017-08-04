#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

rospy.init_node('node_send_count')
pub = rospy.Publisher('counter', Int32, queue_size=10)#topico
rate = rospy.Rate(2)

count = 0

while not rospy.is_shutdown():
    try:
        pub.publish(count)
        count+=1

        rate.sleep()
    except rospy.ROSInterruptException:
        print 'salio'
