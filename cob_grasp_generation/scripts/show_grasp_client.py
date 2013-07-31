#! /usr/bin/env python

import roslib; roslib.load_manifest('cob_grasp_generation')
import rospy

import actionlib
import manipulation_msgs.msg
import cob_grasp_generation.msg 

def show_grasp_client():
    client = actionlib.SimpleActionClient('show_grasp', cob_grasp_generation.msg.ShowGraspAction)
    client.wait_for_server()

    object_name = raw_input("Insert object name: ")
    grasp_id = int(raw_input("Insert grasp_id: "))

    while not rospy.is_shutdown():
        print grasp_id
        
        # Set the goal here: Object-Name, Grasp ID
        goal = cob_grasp_generation.msg.ShowGraspGoal(object_name, grasp_id, True)

        # Sends the goal to the action server.
        client.send_goal(goal)

        # Waits for the server to finish performing the action.
        client.wait_for_result()

        # Prints out the result of executing the action
        print client.get_result()
        
        raw_input("Enter for next grasp...")
        grasp_id = grasp_id + 1
    
    
if __name__ == '__main__':
    try:
        rospy.init_node('show_grasp_client')
        result = show_grasp_client()
        print "Result:"
        print result
    except rospy.ROSInterruptException:
        print "program interrupted before completion"
