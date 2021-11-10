#!/usr/bin/env python
import rospy
from ros_essentials_cpp.msg import hello

def hello_sensor_callback(hello_sensor_message):
    rospy.loginfo("new IoT data received: (%d, %s, %.2f, %.2f)",hello_sensor_message.id,hello_sensor_message.name,hello_sensor_message.temperature,hello_sensor_message.humidity)

rospy.init_node("IoT_sensor_subscriber_node",anonymous=True)

rospy.Subscriber("IoT_sensor_topic",hello,hello_sensor_callback)


rospy.spin()
