#!/usr/bin/env python  
import rospy

# Because of transformations
import tf_conversions

import tf2_ros
import nav_msgs.msg
import geometry_msgs.msg
import pdb

def handle_odom(msg):
    br = tf2_ros.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()

    t.header.stamp = rospy.Time.now()
    t.header.frame_id = msg.header.frame_id
    t.child_frame_id = msg.child_frame_id
    t.transform.translation = msg.pose.pose.position
    t.transform.rotation =msg.pose.pose.orientation
    br.sendTransform(t)

if __name__ == '__main__':
    rospy.init_node('tf_broadcaster')
    rospy.Subscriber('/ground_truth/state',
                     nav_msgs.msg.Odometry,
                     handle_odom)
    rospy.spin()