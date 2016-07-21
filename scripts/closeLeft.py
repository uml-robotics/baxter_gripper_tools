#!/usr/bin/env python
import rospy

from baxter_interface import Gripper

if __name__ == '__main__':
    rospy.init_node('gripperTools', anonymous=True)
    gripper = Gripper('left')
    gripper.close(True)
