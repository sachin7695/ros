#!/usr/bin/env python
# license removed for brevity
import rospy
from ros_essentials_cpp.msg import hello
import random
# we create a new publisher,we specify new topic name,then type opf message
pub=rospy.Publisher('IoT_sensor_topic',hello,queue_size=10)
rospy.init_node('IoT_sensor_publisher_node',anonymous=True)

rate=rospy.Rate(0.5)

i=0
while not rospy.is_shutdown():
    hello_sensor=hello()
    hello_sensor_id=1
    hello_sensor_name="IoT_parking_01"
    hello_sensor.temperature=21.33+(random.random()*2)
    hello_sensor.humidity=32.41+(random.random()*2)
    rospy.loginfo("I Publish:")
    rospy.loginfo(hello_sensor)
    pub.publish(hello_sensor)
    rate.sleep()
    i+=1