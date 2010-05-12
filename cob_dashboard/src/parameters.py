#!/usr/bin/python

import rospy
from trajectory_msgs.msg import *
from cob_msgs.msg import *

class torsoParameter:
	action_goal_topic = 'torso/JointTrajectory'
	joint_names = ["torso_lower_neck_pan_joint","torso_lower_neck_tilt_joint","torso_upper_neck_pan_joint","torso_upper_neck_tilt_joint"]

	home = JointTrajectory()
	home.joint_names = joint_names
	point=JointTrajectoryPoint()
	point.positions=[0,0,0,0]
	point.velocities=[0,0,0,0]
	point.time_from_start=rospy.Duration(3)
	home.points.append(point)

	front = JointTrajectory()
	front.joint_names = joint_names
	point=JointTrajectoryPoint()
	point.positions=[0.0,0.05,0.0,0.1]
	point.velocities=[0,0,0,0]
	point.time_from_start=rospy.Duration(3)
	front.points.append(point)
	
	back = JointTrajectory()
	back.joint_names = joint_names
	point=JointTrajectoryPoint()
	point.positions=[0.0,-0.05,0.0,-0.1]
	point.velocities=[0,0,0,0]
	point.time_from_start=rospy.Duration(3)
	back.points.append(point)
	
	right = JointTrajectory()
	right.joint_names = joint_names
	point=JointTrajectoryPoint()
	point.positions=[0.05,0.0,0.1,0.0]
	point.velocities=[0,0,0,0]
	point.time_from_start=rospy.Duration(3)
	right.points.append(point)
	
	left = JointTrajectory()
	left.joint_names = joint_names
	point=JointTrajectoryPoint()
	point.positions=[-0.05,0.0,-0.1,0.0]
	point.velocities=[0,0,0,0]
	point.time_from_start=rospy.Duration(3)
	left.points.append(point)

	nod = JointTrajectory()
	nod.joint_names = joint_names
	point=JointTrajectoryPoint()
	point.positions=[0,0.05,0,0.1]
	point.velocities=[0,0,0,0]
	point.time_from_start=rospy.Duration(3)
	nod.points.append(point)
	point=JointTrajectoryPoint()
	point.positions=[0,0,0,0]
	point.velocities=[0,0,0,0]
	point.time_from_start=rospy.Duration(6)
	nod.points.append(point)
	point=JointTrajectoryPoint()
	point.positions=[0,0.05,0,0.1]
	point.velocities=[0,0,0,0]
	point.time_from_start=rospy.Duration(9)
	nod.points.append(point)
	point=JointTrajectoryPoint()
	point.positions=[0,0,0,0]
	point.velocities=[0,0,0,0]
	point.time_from_start=rospy.Duration(12)
	nod.points.append(point)
	
	shake = JointTrajectory()
	shake.joint_names = joint_names
	point=JointTrajectoryPoint()
	point.positions=[0.05,0,0.1,0]
	point.velocities=[0,0,0,0]
	point.time_from_start=rospy.Duration(3)
	shake.points.append(point)
	point=JointTrajectoryPoint()
	point.positions=[-0.05,0,-0.1,0]
	point.velocities=[0,0,0,0]
	point.time_from_start=rospy.Duration(3)
	shake.points.append(point)
	point=JointTrajectoryPoint()
	point.positions=[0.05,0,0.1,0]
	point.velocities=[0,0,0,0]
	point.time_from_start=rospy.Duration(3)
	shake.points.append(point)
	point=JointTrajectoryPoint()
	point.positions=[0,0,0,0]
	point.velocities=[0,0,0,0]
	point.time_from_start=rospy.Duration(3)
	shake.points.append(point)
	
class trayParameter:
	action_goal_topic = 'tray/JointTrajectory'
	joint_names = ["torso_tray_joint"]

	up = JointTrajectory()
	up.joint_names = joint_names
	point=JointTrajectoryPoint()
	point.positions=[0]
	point.velocities=[0]
	point.time_from_start=rospy.Duration(3)
	up.points.append(point)
	
	down = JointTrajectory()
	down.joint_names = joint_names
	point=JointTrajectoryPoint()
	point.positions=[-3.1415926]
	point.velocities=[0]
	point.time_from_start=rospy.Duration(3)
	down.points.append(point)

class armParameter:
	action_goal_topic = 'arm_controller/joint_trajectory_action'
	joint_names = ["arm_1_joint","arm_2_joint","arm_3_joint","arm_4_joint","arm_5_joint","arm_6_joint","arm_7_joint"]

	home = JointTrajectory()
	home.joint_names = joint_names
	point=JointTrajectoryPoint()
	point.positions=[0,0,0,0,0,0,0]
	point.velocities=[0,0,0,0,0,0,0]
	point.time_from_start=rospy.Duration(3)
	home.points.append(point)

	folded = JointTrajectory()
	folded.joint_names = joint_names
	point=JointTrajectoryPoint()
	point.positions=[0,0.7,1.5,1.5,0.7,1.5,0]
	point.velocities=[0,0,0,0,0,0,0]
	point.time_from_start=rospy.Duration(3)
	folded.points.append(point)

class lbrParameter:
	action_goal_topic = 'lbr_controller/joint_trajectory_action'
	joint_names = ["arm_1_joint","arm_2_joint","arm_3_joint","arm_4_joint","arm_5_joint","arm_6_joint","arm_7_joint"]

	home = JointTrajectory()
	home.joint_names = joint_names
	point=JointTrajectoryPoint()
	point.positions=[0,0,0,0,0,0,0]
	point.velocities=[0,0,0,0,0,0,0]
	point.time_from_start=rospy.Duration(3)
	home.points.append(point)

	folded = JointTrajectory()
	folded.joint_names = joint_names
	point=JointTrajectoryPoint()
	point.positions=[-1.16, -2.10, -2.53, -1.78, -2.84, -0.97, 1.76]
	point.velocities=[0,0,0,0,0,0,0]
	point.time_from_start=rospy.Duration(3)
	folded.points.append(point)

	pregrasp = JointTrajectory()
	pregrasp.joint_names = joint_names
	point=JointTrajectoryPoint()
	point.positions=[-1.46, -2.10, -1.79, -1.42, -2.41, -0.91, 2.54]
	point.velocities=[0,0,0,0,0,0,0]
	point.time_from_start=rospy.Duration(3)
	pregrasp.points.append(point)

	grasp = JointTrajectory()
	grasp.joint_names = joint_names
	point=JointTrajectoryPoint()
	point.positions=[-0.82, -2.01, -1.23, -1.00, -2.62, -0.62, 2.78]
	point.velocities=[0,0,0,0,0,0,0]
	point.time_from_start=rospy.Duration(3)
	grasp.points.append(point)

	graspTOtablet = JointTrajectory()
	graspTOtablet.joint_names = joint_names
	point=JointTrajectoryPoint()
	point.positions=[-0.87, -1.76, -1.35, -0.91, -2.61, -1.09, 2.97]
	point.velocities=[0,0,0,0,0,0,0]
	point.time_from_start=rospy.Duration(3)
	graspTOtablet.points.append(point)
	point=JointTrajectoryPoint()
	point.positions=[-0.94, -1.74, -1.18, -1.68, -2.81, -1.45, 2.90]
	point.velocities=[0,0,0,0,0,0,0]
	point.time_from_start=rospy.Duration(6)
	graspTOtablet.points.append(point)
	point=JointTrajectoryPoint()
	point.positions=[-0.15, -1.15, -0.82, -2.10, -2.93, -1.37, 2.97]
	point.velocities=[0,0,0,0,0,0,0]
	point.time_from_start=rospy.Duration(9)
	graspTOtablet.points.append(point)
	point=JointTrajectoryPoint()
	point.positions=[1.99, -0.77, -2.00, -2.10, -2.83, -0.27, 2.96]
	point.velocities=[0,0,0,0,0,0,0]
	point.time_from_start=rospy.Duration(12)
	graspTOtablet.points.append(point)
	point=JointTrajectoryPoint()
	point.positions=[2.52, -1.12, -2.36, -1.90, -2.83, -0.25, 2.83]
	point.velocities=[0,0,0,0,0,0,0]
	point.time_from_start=rospy.Duration(12)
	graspTOtablet.points.append(point)
	
	overTablet=JointTrajectory()
	overTablet.joint_names = joint_names
	point=JointTrajectoryPoint()
	point.positions=[2.52, -1.12, -2.36, -1.90, -2.83, -0.25, 2.83]
	point.velocities=[0,0,0,0,0,0,0]
	point.time_from_start=rospy.Duration(3)
	overTablet.points.append(point)
	
	foldedTopregrasp = JointTrajectory()
	foldedTopregrasp.joint_names = joint_names
	point=JointTrajectoryPoint()
	point.positions=[-1.44, -2.08, -1.74, -1.44, -2.72, -1.77, 2.92]
	point.velocities=[0,0,0,0,0,0,0]
	point.time_from_start=rospy.Duration(3)
	foldedTopregrasp.points.append(point)
	point=JointTrajectoryPoint()
	point.positions=[-1.46, -2.10, -1.79, -1.42, -2.41, -0.91, 2.54]
	point.velocities=[0,0,0,0,0,0,0]
	point.time_from_start=rospy.Duration(6)
	foldedTopregrasp.points.append(point)

	tabletTOfolded = JointTrajectory()
	tabletTOfolded.joint_names = joint_names
	point=JointTrajectoryPoint()
	point.positions=[2.01, -0.72, -2.15, -1.89, -2.78, -0.74, 2.82]
	point.velocities=[0,0,0,0,0,0,0]
	point.time_from_start=rospy.Duration(3)
	tabletTOfolded.points.append(point)
	point=JointTrajectoryPoint()
	point.positions=[0.89, -1.73, -1.98, -1.67, -2.90, -0.89, 2.24]
	point.velocities=[0,0,0,0,0,0,0]
	point.time_from_start=rospy.Duration(6)
	tabletTOfolded.points.append(point)
	point=JointTrajectoryPoint()
	point.positions=[-1.16, -2.10, -2.53, -1.78, -2.84, -0.97, 1.76]
	point.velocities=[0,0,0,0,0,0,0]
	point.time_from_start=rospy.Duration(6)
	tabletTOfolded.points.append(point)
	
	tablet = JointTrajectory()
	tablet.joint_names = joint_names
	point=JointTrajectoryPoint()
	point.positions=[2.47, -1.14, -2.43, -1.87, -2.82, -0.33, 2.78]
	point.velocities=[0,0,0,0,0,0,0]
	point.time_from_start=rospy.Duration(3)
	tablet.points.append(point)

	coolerButton = JointTrajectory()
	coolerButton.joint_names = joint_names
	point=JointTrajectoryPoint()
	point.positions=[-1.26, -2.10, -1.43, -1.58, -1.47, -0.37, -1.47]
	point.time_from_start=rospy.Duration(3)
	coolerButton.points.append(point)
	
	coolerPreGrasp = JointTrajectory()
	coolerPreGrasp.joint_names = joint_names
	point=JointTrajectoryPoint()
	point.positions=[-1.33, -2.10, -1.58, -1.83, -0.73, -0.55, 0.88]
	point.time_from_start=rospy.Duration(3)
	coolerPreGrasp.points.append(point)
	
	coolerGrasp = JointTrajectory()
	coolerGrasp.joint_names = joint_names
	point=JointTrajectoryPoint()
	point.positions=[-1.02, -2.09, -1.44, -1.55, -0.72, -0.56, 0.89]
	point.time_from_start=rospy.Duration(3)
	coolerGrasp.points.append(point)

	coolerPostGrasp = JointTrajectory()
	coolerPostGrasp.joint_names = joint_names
	point=JointTrajectoryPoint()
	point.positions=[-1.19, -2.08, -1.46, -1.65, -0.72, -0.45, 0.90]
	point.time_from_start=rospy.Duration(3)
	coolerPostGrasp.points.append(point)
	
	cupTOtablet = JointTrajectory()
	cupTOtablet.joint_names = joint_names
	point=JointTrajectoryPoint()
	point.positions=[-1.50, -2.10, -1.47, -2.02, -1.58, -0.23, 1.78]
	point.velocities=[0,0,0,0,0,0,0]
	point.time_from_start=rospy.Duration(6)
	cupTOtablet.points.append(point)
	point=JointTrajectoryPoint()
	point.positions=[-0.15, -1.15, -0.82, -2.10, -2.93, -1.37, 2.97]
	point.velocities=[0,0,0,0,0,0,0]
	point.time_from_start=rospy.Duration(9)
	cupTOtablet.points.append(point)
	point=JointTrajectoryPoint()
	point.positions=[1.99, -0.77, -2.00, -2.10, -2.83, -0.27, 2.96]
	point.velocities=[0,0,0,0,0,0,0]
	point.time_from_start=rospy.Duration(12)
	cupTOtablet.points.append(point)
	point=JointTrajectoryPoint()
	point.positions=[2.52, -1.12, -2.36, -1.90, -2.83, -0.25, 2.83]
	point.velocities=[0,0,0,0,0,0,0]
	point.time_from_start=rospy.Duration(12)
	cupTOtablet.points.append(point)
	
class armParameter_pr2:
	action_goal_topic = 'r_arm_controller/joint_trajectory_action'
	joint_names = ["r_shoulder_pan_joint","r_shoulder_lift_joint","r_upper_arm_roll_joint","r_elbow_flex_joint","r_forearm_roll_joint","r_wrist_flex_joint","r_wrist_roll_joint"]

	home = JointTrajectory()
	home.joint_names = joint_names
	point=JointTrajectoryPoint()
	point.positions=[0,0,0,0,0,0,0]
	point.velocities=[0,0,0,0,0,0,0]
	point.time_from_start=rospy.Duration(3)
	home.points.append(point)

	folded = JointTrajectory()
	folded.joint_names = joint_names
	point=JointTrajectoryPoint()
	point.positions=[-1.07,-0.29,0.44,0.62,0.42,-0.00,0.10]
	point.velocities=[0,0,0,0,0,0,0]
	point.time_from_start=rospy.Duration(3)
	folded.points.append(point)
	
class sdhParameter:
	action_goal_topic = 'sdh/JointCommand'
    #-->[not_used, joint_thumb1_thumb2, joint_thumb2_thumb3, joint_palm_finger11, joint_finger11_finger12, joint_finger12_finger13, not_used, joint_finger21_finger22, joint_finger22_finger23]
	joint_names = ["joint_palm_thumb1", "joint_thumb1_thumb2", "joint_thumb2_thumb3", "joint_palm_finger11", "joint_finger11_finger12", "joint_finger12_finger13", "joint_palm_finger21", "joint_finger21_finger22", "joint_finger22_finger23"]

	home = JointCommand()
	home.joint_names = joint_names
	home.positions=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
	home.velocities=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]

	cylClose = JointCommand()
	cylClose.joint_names = joint_names
	cylClose.positions=[0.0,0.0,1.0472,0.0,0.0,1.0472,0.0,0.0,1.0472]
	cylClose.velocities=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]

	cylOpen = JointCommand()
	cylOpen.joint_names = joint_names
	cylOpen.positions=[0.0,-0.7854,1.0472,0.0,-0.7854,1.0472,0.0,-0.7854,1.0472]
	cylOpen.velocities=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]

	spherClose = JointCommand()
	spherClose.joint_names = joint_names
	spherClose.positions=[0.0,-0.2618,1.0472,1.0472,-0.2618,1.0472,0.0,-0.2618,1.0472]
	spherClose.velocities=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]

	spherOpen = JointCommand()
	spherOpen.joint_names = joint_names
	spherOpen.positions=[0.0,-0.7854,1.0472,1.0472,-0.7854,1.0472,0.0,-0.7854,1.0472]
	spherOpen.velocities=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
	
	trainObjects = JointCommand()
	trainObjects.joint_names = joint_names
	trainObjects.positions=[0.0,-1.5700,-1.5700,1.0472,-1.5700,-1.5700,0.0,-1.5700,-1.5700]
	trainObjects.velocities=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
	
	trainObjectsParallel = JointCommand()
	trainObjectsParallel.joint_names = joint_names
	trainObjectsParallel.positions=[0.0,-1.5700,-1.5700,0.0,-1.5700,-1.5700,0.0,-1.5700,-1.5700]
	trainObjectsParallel.velocities=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
	
	cupHome = JointCommand()
	cupHome.joint_names = joint_names
	cupHome.positions=[0.0,0.0,0.0,1.5700,-0.2094,0.6108,0.0,-0.2094,0.6108]
	
	cupOpen = JointCommand()
	cupOpen.joint_names = joint_names
	cupOpen.positions=[0.0,-1.3962,1.3962,1.5700,-0.2094,-0.5235,0.0,-0.2094,-0.5235]
	
	cupClose = JointCommand()
	cupClose.joint_names = joint_names
	cupClose.positions=[0.0,-1.3962,1.3962,1.5700,-0.2094,0.6108,0.0,-0.2094,0.6108]
	
	cupRelease = JointCommand()
	cupRelease.joint_names = joint_names
	cupRelease.positions=[0.0,-1.3962,1.3962,1.5700,-0.5235,0.5235,0.0,-0.5235,0.5235]
		
	coolerButtonUp = JointCommand()
	coolerButtonUp.joint_names = joint_names
	coolerButtonUp.positions=[0.0,0.0,1.5700,0.0,0.0,1.5700,0.0,-0.087,0.0]
	
	coolerButtonDown = JointCommand()
	coolerButtonDown.joint_names = joint_names
	coolerButtonDown.positions=[0.0,0.0,1.5700,0.0,0.0,1.5700,0.0,0.160,0.0]
	
	coolerCupOpen = JointCommand()
	coolerCupOpen.joint_names = joint_names
	coolerCupOpen.positions=[0.0, -1.5700, 0.0, 1.5700, -0.2000, 0.2400, 1.5700, -0.2000, 0.2400]
	
	coolerCupClose = JointCommand()
	coolerCupClose.joint_names = joint_names
	coolerCupClose.positions=[0.0, -1.5700, -0.0, 1.5700, -0.2000, 0.3500, 1.5700, -0.2000, 0.3500]
