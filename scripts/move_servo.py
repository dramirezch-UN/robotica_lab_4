#!/usr/bin/env python

import rospy
from dynamixel_workbench_msgs.srv import DynamixelCommand
import time

wait_time = 1
rospy.init_node('dynamixel_command_client')

# Define the service client
dynamixel_command = rospy.ServiceProxy('/dynamixel_workbench/dynamixel_command', DynamixelCommand)

# Define the parameters for the service request
params_1 = {
    'id': 1,  # ID of the servo to control
    'addr_name': 'Goal_Position',  # Address name of the control table
    'value': 400  # Desired position of the servo (0-1023)
}

params_2 = {
    'id': 2,  # ID of the servo to control
    'addr_name': 'Goal_Position',  # Address name of the control table
    'value': 400  # Desired position of the servo (0-1023)
}

params_3 = {
    'id': 3,  # ID of the servo to control
    'addr_name': 'Goal_Position',  # Address name of the control table
    'value': 400  # Desired position of the servo (0-1023)
}

params_4 = {
    'id': 4,  # ID of the servo to control
    'addr_name': 'Goal_Position',  # Address name of the control table
    'value': 400  # Desired position of the servo (0-1023)
}

params_5 = {
    'id': 5,  # ID of the servo to control
    'addr_name': 'Goal_Position',  # Address name of the control table
    'value': 400  # Desired position of the servo (0-1023)
}

params = [params_1, params_2, params_3, params_4, params_5]

# Call the service with the defined parameters
for param in params:
    time.sleep(wait_time)

    response = dynamixel_command(**param)

    if response.comm_result:
        print('Servo with ID {} position set to: {}'.format(param['id'], param['value']))
    else:
        print('Failed to set servo position')
