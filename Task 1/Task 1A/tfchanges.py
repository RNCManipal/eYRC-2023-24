#!/usr/bin/env python3


'''
*****************************************************************************************
*
*        		===============================================
*           		    Cosmo Logistic (CL) Theme (eYRC 2023-24)
*        		===============================================
*
*  This script should be used to implement Task 1A of Cosmo Logistic (CL) Theme (eYRC 2023-24).
*
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or
*  breach of the terms of this agreement.
*
*****************************************************************************************
'''

# Team ID:          [ CL#2414 ]
# Author List:	    [ Aditya Wadgaonkar,Harikishanthini K,Sujan Adiga,Tanay Srivastava]
# Filename:         task1a.py
# Functions:        [ Comma separated list of functions in this file ]
# Nodes:	    Add your publishing and subscribing node
# Example:          Publishing Topics  - [ /tf ]
#                   Subscribing Topics - [ /camera/aligned_depth_to_color/image_raw, /etc... ]

################### IMPORT MODULES #######################

import rclpy
import sys
import cv2
import math
import tf2_ros 
import tf_transformations
import tf2_geometry_msgs
import numpy as np
from rclpy.node import Node
from cv_bridge import CvBridge, CvBridgeError
from geometry_msgs.msg import TransformStamped
from scipy.spatial.transform import Rotation as R
from sensor_msgs.msg import CompressedImage, Image


##################### FUNCTION DEFINITIONS #######################


ARUCO_DICT = {
	"DICT_4X4_50": cv2.aruco.DICT_4X4_50,
	"DICT_4X4_100": cv2.aruco.DICT_4X4_100,
	"DICT_4X4_250": cv2.aruco.DICT_4X4_250,
	"DICT_4X4_1000": cv2.aruco.DICT_4X4_1000,
	"DICT_5X5_50": cv2.aruco.DICT_5X5_50,
	"DICT_5X5_100": cv2.aruco.DICT_5X5_100,
	"DICT_5X5_250": cv2.aruco.DICT_5X5_250,
	"DICT_5X5_1000": cv2.aruco.DICT_5X5_1000,
	"DICT_6X6_50": cv2.aruco.DICT_6X6_50,
	"DICT_6X6_100": cv2.aruco.DICT_6X6_100,
	"DICT_6X6_250": cv2.aruco.DICT_6X6_250,
	"DICT_6X6_1000": cv2.aruco.DICT_6X6_1000,
	"DICT_7X7_50": cv2.aruco.DICT_7X7_50,
	"DICT_7X7_100": cv2.aruco.DICT_7X7_100,
	"DICT_7X7_250": cv2.aruco.DICT_7X7_250,
	"DICT_7X7_1000": cv2.aruco.DICT_7X7_1000,
	"DICT_ARUCO_ORIGINAL": cv2.aruco.DICT_ARUCO_ORIGINAL,
	"DICT_APRILTAG_16h5": cv2.aruco.DICT_APRILTAG_16h5,
	"DICT_APRILTAG_25h9": cv2.aruco.DICT_APRILTAG_25h9,
	"DICT_APRILTAG_36h10": cv2.aruco.DICT_APRILTAG_36h10,
	"DICT_APRILTAG_36h11": cv2.aruco.DICT_APRILTAG_36h11
}


def calculate_rectangle_area(coordinates):
    '''
    Description:    Function to calculate area or detected aruco

    Args:
        coordinates (list):     coordinates of detected aruco (4 set of (x,y) coordinates)

    Returns:
        area        (float):    area of detected aruco
        width       (float):    width of detected aruco
    '''

    ############ Function VARIABLES ############

    # You can remove these variables after reading the instructions. These are just for sample.

    area = None
    width = None

    ############ ADD YOUR CODE HERE ############

    # INSTRUCTIONS & HELP : 
    #	->  Recevice coordiantes from 'detectMarkers' using cv2.aruco library 
    #       and use these coordinates to calculate area and width of aruco detected.
    #	->  Extract values from input set of 4 (x,y) coordinates 
    #       and formulate width and height of aruco detected to return 'area' and 'width'.

    ############################################
    
    [[[x1,y1],[x2,y2],[x3,y3],[x4,y4]]] = coordinates #extracting values from coordinates argument passed form main function
    # Use the Shoelace formula to calculate the area
    area = 0.5 * abs((x1*y2 + x2*y3 + x3*y4 + x4*y1) - (y1*x2 + y2*x3 + y3*x4 + y4*x1))

    #calculating the width of the detected marker
    # Calculate the distance between two opposite corners
    diagonal1 = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)
    diagonal2 = math.sqrt((x2 - x4)**2 + (y2 - y4)**2)
    
    # Check if both diagonals are approximately equal (within a small tolerance)
    tolerance = 1e-6
    if abs(diagonal1 - diagonal2) < tolerance:
        width = diagonal1  # Use either diagonal to determine width
    

    '''if len(coordinates) != 4: 
           #raise ValueError("Input should contain exactly 4 sets of coordinates")

    # Calculate width as the Euclidean distance between two opposite corners
    width = ((coordinates[0][0] - coordinates[2][0])*2 + (coordinates[0][1] - coordinates[2][1])*2)*0.5

    # Calculate height as the Euclidean distance between the other two opposite corners
    height = ((coordinates[1][0] - coordinates[3][0])*2 + (coordinates[1][1] - coordinates[3][1])*2)*0.5

    # Calculate the area as the product of width and height
    area = width * height'''
       


    return area, width
    



def aruco_display(corners, ids, rejected, image):
    
	if len(corners) > 0:
		
		ids = ids.flatten()
		
		for (markerCorner, markerID) in zip(corners, ids):
			
			corners = markerCorner.reshape((4, 2))
			(topLeft, topRight, bottomRight, bottomLeft) = corners
			
			topRight = (int(topRight[0]), int(topRight[1]))
			bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
			bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
			topLeft = (int(topLeft[0]), int(topLeft[1]))

			cv2.line(image, topLeft, topRight, (0, 255, 0), 2)
			cv2.line(image, topRight, bottomRight, (0, 255, 0), 2)
			cv2.line(image, bottomRight, bottomLeft, (0, 255, 0), 2)
			cv2.line(image, bottomLeft, topLeft, (0, 255, 0), 2)
			
			cX = int((topLeft[0] + bottomRight[0]) / 2.0)
			cY = int((topLeft[1] + bottomRight[1]) / 2.0)
			cv2.circle(image, (cX, cY), 4, (0, 0, 255), -1)
			
			cv2.putText(image, str(markerID),(topLeft[0], topLeft[1] - 10), cv2.FONT_HERSHEY_SIMPLEX,
				0.5, (0, 255, 0), 2)
			#print("[Inference] ArUco marker ID: {}".format(markerID))
			
	return image


def detect_aruco(image):
    '''
    Description:    Function to perform aruco detection and return each detail of aruco detected 
                    such as marker ID, distance, angle, width, center point location, etc.

    Args:
        image                   (Image):    Input image frame received from respective camera topic

    Returns:
        center_aruco_list       (list):     Center points of all aruco markers detected
        distance_from_rgb_list  (list):     Distance value of each aruco markers detected from RGB camera
        angle_aruco_list        (list):     Angle of all pose estimated for aruco marker
        width_aruco_list        (list):     Width of all detected aruco markers
        ids                     (list):     List of all aruco marker IDs detected in a single frame 
    '''

    ############ Function VARIABLES ############
    if image is None:
        return [], [], [], [], []
    # ->  You can remove these variables if needed. These are just for suggestions to let you get started

    # Use this variable as a threshold value to detect aruco markers of certain size.
    # Ex: avoid markers/boxes placed far away from arm's reach position  
    aruco_area_threshold = 1500

    # The camera matrix is defined as per camera info loaded from the plugin used. 
    # You may get this from /camer_info topic when camera is spawned in gazebo.
    # Make sure you verify this matrix once if there are calibration issues.
    cam_mat = np.array([[931.1829833984375, 0.0, 640.0], [0.0, 931.1829833984375, 360.0], [0.0, 0.0, 1.0]])

    # The distortion matrix is currently set to 0. 
    # We will be using it during Stage 2 hardware as Intel Realsense Camera provides these camera info.
    dist_mat = np.array([0.0,0.0,0.0,0.0,0.0])

    # We are using 150x150 aruco marker size
    size_of_aruco_m = 0.15

    # You can remove these variables after reading the instructions. These are just for sample.
    center_aruco_list = []
    distance_from_rgb_list = []
    angle_aruco_list = []
    width_aruco_list = []
    ids = []
 
    ############ ADD YOUR CODE HERE ############

    # INSTRUCTIONS & HELP : 

    #	->  Convert input BGR image to GRAYSCALE for aruco detection
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray_image", gray_image)
    cv2.waitKey(100)
    #   ->  Use these aruco parameters-
    #   ->  Dictionary: 4x4_50 (4x4 only until 50 aruco IDs)

    aruco_type = "DICT_4X4_50"

    #aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
    cv2.aruco_dict = cv2.aruco.getPredefinedDictionary(ARUCO_DICT[aruco_type])
    aruco_params = cv2.aruco.DetectorParameters()
   

    #   ->  Detect aruco marker in the image and store 'corners' and 'ids'
    #   ->  HINT: Handle cases for empty markers detection. 
    #corners, ids, _ = cv2.aruco.detectMarkers(gray_image, aruco_dict, parameters=aruco_params)
    #corners, ids, rejected= cv2.aruco.detectMarkers(gray_image, aruco_dict, parameters=aruco_params)
    (corners, ids, rejected) = cv2.aruco.detectMarkers(gray_image, cv2.aruco_dict,parameters=aruco_params)
    
    
    #image=aruco_display(corners, ids, rejected, gray_image)
    #   ->  Draw detected marker on the image frame which will be shown later

    #   ->  Loop over each marker ID detected in frame and calculate area using function defined above (calculate_rectangle_area(coordinates))
    #print('in detect aruco')
    if ids is not None and len(ids) > 0:
        #print('In if condition ofdetect aruco')
        for i, marker_id in enumerate(ids):
            #print('Infor loop ofdetect aruco')
           
            #cv2.aruco.drawFrameAxes(image, cam_mat, dist_mat, rvec, tvec, 0.1)
            
            # Calculate the area of the detected marker
            if corners is not None:
                 #print(corners[i])
                 area = calculate_rectangle_area(corners[i])
                 #print("areaa is")
                 #print(area)
                 
            else:
                 print("corners none")

            #   ->  Remove tags which are far away from arm's reach positon based on some threshold defined
            #print(area)
            if area[0] > aruco_area_threshold:
                # Draw the detected marker on the image
                #cv2.aruco.drawDetectedMarkers(image, corners)
                image_1=aruco_display(corners, ids, rejected, image)     

                #   ->  Calculate center points aruco list using math and distance from RGB camera using pose estimation of aruco marker
                #   ->  HINT: You may use numpy for center points and 'estimatePoseSingleMarkers' from cv2 aruco library for pose estimation
                # Estimate the pose of the detected marker
                rvec, tvec, _ = cv2.aruco.estimatePoseSingleMarkers(corners[i], 0.02, cam_mat, dist_mat)

                # Calculate the center point of the marker
                center = np.mean(corners[i][0], axis=0)

                # Calculate the distance from the RGB camera (assuming Z-axis is depth)
                #print("tves shape:",tvec)
                #tvec=tvec.reshape((3,1))
                distance = tvec[0][0][2]
                #print('no error in dis')

                # Calculate the angle (you may need to adjust this based on your requirements)
                angle = np.degrees(np.arctan2(tvec[0][0][1], tvec[0][0][0]))

                # Calculate the width of the marker (you may need to adjust this based on your requirements)
                width = np.linalg.norm(corners[i][0][0] - corners[i][0][1])

                
                # Draw frame axes
                rvec, tvec, _ = cv2.aruco.estimatePoseSingleMarkers(corners[i], 0.02, cam_mat, dist_mat)
                cv2.drawFrameAxes(image_1, cam_mat, dist_mat, rvec, tvec,0.1)
                x=center[0]
                y=center[1]
                c_x=round(x)
                c_y=round(y)
               
                cv2.circle(image_1, (c_x,c_y), 1, (0, 0, 0), -1)

              
                cv2.imshow('Detected Markers', image_1) 
                cv2.waitKey(100)


                print("data for arucoId: ",ids[i])
                print("x coordinate of centre: ",c_x)
                print("y coordinate of centre: ",c_y)
                print("angle is:  ",angle)
               # Append the details to the respective lists
                center_aruco_list.append(center)
                distance_from_rgb_list.append(distance)
                angle_aruco_list.append(angle)
                width_aruco_list.append(width)
            
    ############################################
    #print('detect aruco',center_aruco_list, distance_from_rgb_list, angle_aruco_list, width_aruco_list, ids)

    return center_aruco_list, distance_from_rgb_list, angle_aruco_list, width_aruco_list, ids


##################### CLASS DEFINITION #######################

class aruco_tf(Node):
    '''
    ___CLASS___

    Description:    Class which servers purpose to define process for detecting aruco marker and publishing tf on pose estimated.
    '''

    def __init__(self):
        '''
        Description:    Initialization of class aruco_tf
                        All classes have a function called __init__(), which is always executed when the class is being initiated.
                        The __init__() function is called automatically every time the class is being used to create a new object.
                        You can find more on this topic here -> https://www.w3schools.com/python/python_classes.asp
        '''

        super().__init__('aruco_tf_publisher')                                          # registering node

        ############ Topic SUBSCRIPTIONS ############

        self.color_cam_sub = self.create_subscription(Image, '/camera/color/image_raw', self.colorimagecb, 10)
        self.depth_cam_sub = self.create_subscription(Image, '/camera/aligned_depth_to_color/image_raw', self.depthimagecb, 10)

        ############ Constructor VARIABLES/OBJECTS ############

        image_processing_rate = 0.2                                                    # rate of time to process image (seconds)
        self.bridge = CvBridge()                                                        # initialise CvBridge object for image conversion
        self.tf_buffer = tf2_ros.buffer.Buffer()                                        # buffer time used for listening transforms
        self.listener = tf2_ros.TransformListener(self.tf_buffer, self)
        self.br = tf2_ros.TransformBroadcaster(self)                                    # object as transform broadcaster to send transform wrt some frame_id
        self.timer = self.create_timer(image_processing_rate, self.process_image)       # creating a timer based function which gets called on every 0.2 seconds (as defined by 'image_processing_rate' variable)
        
        
        self.cv_image = None                                               # colour raw image variable (from colorimagecb())
        self.depth_image = None                                                       # depth image variable (from depthimagecb())


    def depthimagecb(self, data):
        '''
        Description:    Callback function for aligned depth camera topic. 
                        Use this function to receive image depth data and convert to CV2 image

        Args:
            data (Image):    Input depth image frame received from aligned depth camera topic

        Returns:
        '''

        ############ ADD YOUR CODE HERE ############

        # INSTRUCTIONS & HELP : 

        #	->  Use data variable to convert ROS Image message to CV2 Image type
        try:   
             cv2_depth_image = self.bridge.imgmsg_to_cv2(data, desired_encoding="passthrough")
             cv2.imshow("Depth Image", cv2_depth_image)
             cv2.waitKey(100)

            #   ->  HINT: You may use CvBridge to do the same
            ############################################
        except Exception as e:
             print(f"Error converting depth image: {e}") 

        self.depth_image=cv2_depth_image
        

        if self.depth_image is None:
                     print('no depth in construct')
        return cv2_depth_image  



    def colorimagecb(self, data):
        '''
        Description:    Callback function for colour camera raw topic.
                        Use this function to receive raw image data and convert to CV2 image

        Args:
            data (Image):    Input coloured raw image frame received from image_raw camera topic

        Returns:
        '''

        ############ ADD YOUR CODE HERE ############

        # INSTRUCTIONS & HELP : 

        #	->  Use data variable to convert ROS Image message to CV2 Image type
        bridge = CvBridge()
        try:
            cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
            cv2.imshow("Color Image", cv_image)
            cv2.waitKey(100)  # Convert the ROS Image message to a CV2 image

            #   ->  HINT:   You may use CvBridge to do the same
            #               Check if you need any rotation or flipping image as input data maybe different than what you expect to be.
            #               You may use cv2 functions such as 'flip' and 'rotate' to do the same
        except Exception as e:
            print("Error converting ROS Image to CV2: %s", str(e))   #will show error you have to tun in python environment.

        self.cv_image=cv_image
        #self.get_logger().info("Received an image")

        return cv_image  # Handle the error as needed

       
        

        ############################################

    
    def process_image(self):
        '''
        Description:    Timer function used to detect aruco markers and publish tf on estimated poses.

        Args:
        Returns:
        '''

        ############ Function VARIABLES ############

        # These are the variables defined from camera info topic such as image pixel size, focalX, focalY, etc.
        # Make sure you verify these variable values once. As it may affect your result.
        # You can find more on these variables here -> http://docs.ros.org/en/melodic/api/sensor_msgs/html/msg/CameraInfo.html
        
        sizeCamX = 1280
        sizeCamY = 720
        centerCamX = 640 
        centerCamY = 360
        focalX = 931.1829833984375
        focalY = 931.1829833984375
            

        ############ ADD YOUR CODE HERE ############

        # INSTRUCTIONS & HELP : 

        #	->  Get aruco center, distance from rgb, angle, width and ids list from 'detect_aruco_center' defined above
        #center_aruco_list, distance_from_rgb_list, angle_aruco_list, width_aruco_list, ids = detect_aruco(self.cv_image)
        #print(self.cv_image)
        
        center_aruco_list, distance_from_rgb_list, angle_aruco_list, width_aruco_list, ids= detect_aruco(self.cv_image)
        
        #print("ids:", ids)
        #print("center_aruco_list:", center_aruco_list)
       
        #   ->  Loop over detected box ids received to calculate position and orientation transform to publish TF 
        if ids is not None: 
            i=0
            for marker_id in ids:
                 
                #if image_1 is not None:
                 #   cv2.imshow('Detected Markers', image_1) 
                 #   cv2.waitKey(0)
                #   ->  Use this equation to correct the input aruco angle received from cv2 aruco function 'estimatePoseSingleMarkers' here
                #       It's a correction formula- 
                #       angle_aruco = (0.788*angle_aruco) - ((angle_aruco**2)/3160)
                #print('Marker id is:', marker_id)
                #print(angle_aruco_list)
                angle=angle_aruco_list[i]
                
                corrected_angle = (0.788 * angle) - ((angle ** 2) / 3160)
                #   ->  Then calculate quaternions from roll pitch yaw (where, roll and pitch are 0 while yaw is corrected aruco_angle)
                quaternion = tf_transformations.quaternion_from_euler(0, 0, corrected_angle)

                #   ->  Use center_aruco_list to get realsense depth and log them down. (divide by 1000 to convert mm to m)
              
                distance_from_rgb = self.depth_image[int(center_aruco_list[i][1])][int(center_aruco_list[i][0])] / 1000
                #   ->  Use this formula to rectify x, y, z based on focal length, center value and size of image
                #       x = distance_from_rgb * (sizeCamX - cX - centerCamX) / focalX
                #       y = distance_from_rgb * (sizeCamY - cY - centerCamY) / focalY
                #       z = distance_from_rgb
                #       where, 
                #               cX, and cY from 'center_aruco_list'
                #               distance_from_rgb is depth of object calculated in previous step
                #               sizeCamX, sizeCamY, centerCamX, centerCamY, focalX and focalY are defined above
                x = distance_from_rgb * (sizeCamX - center_aruco_list[i][0] - centerCamX) / focalX
                y = distance_from_rgb * (sizeCamY - center_aruco_list[i][1] - centerCamY) / focalY
                z = distance_from_rgb

                #   ->  Now, mark the center points on image frame using cX and cY variables with help of 'cv2.cirle' function 
                #print(center_aruco_list[i][0])
                print("value of x is :",x)
                print("value of y is :",y)
                print("value of z is :",z)
                #   ->  Here, till now you receive coordinates from camera_link to aruco marker center position. 
                #       So, publish this transform w.r.t. camera_link using Geometry Message - TransformStamped 
                #       so that we will collect it's position w.r.t base_link in next step.
                #       Use the following frame_id-
                #           frame_id = 'camera_link'
                #           child_frame_id = 'cam_<marker_id>'          Ex: cam_20, where 20 is aruco marker ID
                

                # Transformation from camera_link to ArUco marker center
                tf_msg = TransformStamped()
                tf_msg.header.stamp = self.get_clock().now().to_msg()
                tf_msg.header.frame_id = 'camera_link'
                tf_msg.child_frame_id = 'cam_' + str(marker_id)
                tf_msg.transform.translation.x = x
                tf_msg.transform.translation.y = y
                tf_msg.transform.translation.z = z
                tf_msg.transform.rotation.x = quaternion[0]
                tf_msg.transform.rotation.y = quaternion[1]
                tf_msg.transform.rotation.z = quaternion[2]
                tf_msg.transform.rotation.w = quaternion[3]
		self.br.sendTransform(tf_msg)
                i=i+1
                try:
                    base_to_obj = self.tf_buffer.lookup_transform('base_link','cam_'+ str(marker_id), rclpy.Time())
                    #base_to_obj = self.tf_buffer.lookup_transform('base_link', f'obj_{aruco_marker["id"]}', rclpy.Time())
		    #we can use self.get_clock().now() instead of  rclpy.Time()
                    self.br.sendTransform(base_to_obj)

                    # Publish the object frame transform message
                    obj_tf_msg = TransformStamped()
                    #or use below 
                    #obj_tf_msg = tf2_geometry_msgs.TransformStamped()
                    obj_tf_msg.header.stamp = self.get_clock().now().to_msg()
                    obj_tf_msg.header.frame_id = 'base_link'
                    #obj_tf_msg.child_frame_id = f'obj_{aruco_marker["id"]}'
                    obj_tf_msg.child_frame_id ='obj_' + str(marker_id)
                    obj_tf_msg.transform = base_to_obj.transform

                    self.br.sendTransform(obj_tf_msg)

                except tf2_ros.LookupException as e:
                    self.get_logger().error(f'Error looking up transform: {e}')

                    


            #   ->  At last show cv2 image window having detected markers drawn and center points located using 'cv2.imshow' function.
            #       Refer MD book on portal for sample image -> https://portal.e-yantra.org/
            
               

        #   ->  NOTE:   The Z axis of TF should be pointing inside the box (Purpose of this will be known in task 1B)
        #               Also, auto eval script will be judging angular difference aswell. So, make sure that Z axis is inside the box (Refer sample images on Portal - MD book)

        ############################################


##################### FUNCTION DEFINITION #######################

def main():
    '''
    Description:    Main function which creates a ROS node and spin around for the aruco_tf class to perform it's task
    '''

    rclpy.init(args=sys.argv)                                       # initialisation

    node = rclpy.create_node('aruco_tf_process')                    # creating ROS node
	
    node.get_logger().info('Node created: Aruco tf process')        # logging information
	
    aruco_tf_class = aruco_tf()                                     # creating a new object for class 'aruco_tf'

    rclpy.spin(aruco_tf_class)                                      # spining on the object to make it alive in ROS 2 DDS

    aruco_tf_class.destroy_node()                                   # destroy node after spin ends

    rclpy.shutdown()                                                # shutdown process


if __name__ == '__main__':
    '''
    Description:    If the python interpreter is running that module (the source file) as the main program, 
                    it sets the special __name__ variable to have a value “__main__”. 
                    If this file is being imported from another module, __name__ will be set to the module’s name.
                    You can find more on this here -> https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/
    '''

    main()
