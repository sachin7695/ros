#!/usr/bin/env python
from logging import error
import sys
import rospy
from ros_essentials_cpp.srv import SubtractTwoInts
from ros_essentials_cpp.srv import SubtractTwoIntsRequest
from ros_essentials_cpp.srv import SubtractTwoIntsResponse

def sub_two_ints_client(a,b):
    rospy.wait_for_service("subtract_two_ints")
    try:
        sub_two_ints = rospy.ServiceProxy('subtract_two_ints', SubtractTwoInts)
        resp1 = sub_two_ints(a, b)
        return resp1.difference
    except rospy.ServiceException(error):
        print ("Service call failed: %s"%error)




def usage():
    return


if __name__ == "__main__":
    if len(sys.argv) == 2:
        a=int(sys.argv[1])
        b=int(sys.argv[2])

    else:
        print("%s [a b]"%sys.argv[0])
        sys.exit(1)

    print("Requesting %s-%s"%(a,b))
    rem=sub_two_ints_client(a,b)
    print("%s - %s = %s"%(a,b,rem))