#!/usr/bin/env python
import rospy
from messa_pkg.srv import WordCount, WordCountResponse

def count_words(request):
    return WordCountResponse(len(request.words.split()))


rospy.init_node('service_server')
server = rospy.Service('word_count', WordCount, count_words)
rospy.spin()
