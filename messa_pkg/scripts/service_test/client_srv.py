#!/usr/bin/env python
import sys
import rospy
from messa_pkg.srv import WordCount

rospy.init_node('service_client')
rospy.wait_for_service('word_count')

word_counter = rospy.ServiceProxy('word_count', WordCount)
words = ''.join(sys.argv[1:])

word_count = word_counter(words)#ejecuta el servicio

print words, '->', word_count.count
