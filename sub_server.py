#!/usr/bin/env python
# import sys
from ros_essentials_cpp.srv import SubtractTwoInts
from ros_essentials_cpp.srv import SubtractTwoIntsRequest
from ros_essentials_cpp.srv import SubtractTwoIntsResponse
import time
import rospy


def handle_sub_two_ints(req):
    print("Returning [%s + %s = %s]" % (req.x, req.y,(req.x-req.y)))
    time.sleep(5)
    return SubtractTwoIntsResponse(req.x-req.y)

def sub_two_ints_server():
    rospy.init_node("subtract_two_ints_server")
    rem=rospy.Service("Sub_two_ints",SubtractTwoInts,handle_sub_two_ints)
    print("ready to subtract two ints. ")
    rospy.spin()

if __name__=="__main__":
    sub_two_ints_server()
