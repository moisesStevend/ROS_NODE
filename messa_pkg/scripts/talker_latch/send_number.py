#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

rospy.init_node('node_send_count')
pub = rospy.Publisher('counter', Int32, queue_size=10, latch=True)#, latch=True) #crea topico
rate = rospy.Rate(1/10.0)

count = 0
count_send=0

while not rospy.is_shutdown():
    try:
        pub.publish(count)
        #print count
        count+=1
        #if(count>10 and count<20):
        #    count_send=count
        #if(count>=20 and count<30):
        #    count_send=0
        #    count=0

        rate.sleep()
    except rospy.ROSInterruptException:
        print 'salio'
