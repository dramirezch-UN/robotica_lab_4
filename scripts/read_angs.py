#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState
import math
import time

def callback(data):
    print("Angulos")
    angs = data.position
    i = 1
    for ang in angs:
        print("Motor {}: {}".format(i, math.degrees(ang)))
        i = i + 1
    time.sleep(100)
    
def listener():
    rospy.init_node('joint_listener', anonymous=True)
    rospy.Subscriber("/dynamixel_workbench/joint_states", JointState, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        while not rospy.is_shutdown():
            listener()
    except rospy.ROSInterruptException:
        pass