

#! /usr/bin/env python3

from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
import rclpy
from geometry_msgs.msg import PoseStamped, Quaternion

rclpy.init()
odom_publisher = rclpy.create_node('odom_publisher')
odom_pub = odom_publisher.create_publisher(PoseStamped, 'odom', 10)
tf_publisher = rclpy.create_node('tf_publisher')
tf_pub = tf_publisher.create_publisher(PoseStamped, 'tf', 10)
nav = BasicNavigator()

initial_pose = PoseStamped()
initial_pose.header.frame_id = 'map'
initial_pose.header.stamp = nav.get_clock().now().to_msg()
initial_pose.pose.position.x = 0.0
initial_pose.pose.position.y = 0.0
initial_pose.pose.orientation.w = 0.0
initial_pose.pose.orientation.z = 0.0
nav.setInitialPose(initial_pose)
nav.waitUntilNav2Active()

for a in range(3):

    p=[[0.0,0.0,0.0],[1.8,1.5,1.57],[2.0, -7.0, -1.57],[-3.0, 2.5, 1.57]]
    

    goal_pose = PoseStamped()
    goal_pose.header.frame_id = 'map'
    #goal_pose.header.stamp = nav.get_clock().now().to_msg()
    goal_pose.header.stamp = odom_publisher.get_clock().now().to_msg()

    goal_pose.pose.position.x = p[a+1][0]
    goal_pose.pose.position.y = p[a+1][1]
    
    goal_pose.pose.orientation = Quaternion(x=0.0, y=0.0, z=p[a+1][2], w=0.0) 
    quaternion_goal_tolerance = Quaternion()
    
    

    nav.goToPose(goal_pose)


    while not nav.isTaskComplete():
        feedback = nav.getFeedback()
    
    result = nav.getResult()
    if result == TaskResult.SUCCEEDED:
        tf_pub.publish(goal_pose)
        odom_pub.publish(goal_pose)
        print('Goal succeeded!')
    elif result == TaskResult.CANCELED:
        print('Goal was canceled!')
    elif result == TaskResult.FAILED:
        print('Goal failed!')


nav.lifecycleShutdown()

exit(0)

