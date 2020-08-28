# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 02:18:27 2020

@author: wasil
"""

import keyboard

Steering_angle = 0
STEERING_FACTOR = 0.05
MAXIMUM_ANGLE = 45

# W, A, S, D
keys = [0, 0, 0, 0]

# code: https://stackoverflow.com/questions/24072790/detect-key-press-in-python
while True:
    try:       # if user pressed other than the given key error will not be shown
        
        # If we steer right, angle towrds the right increases.
        if keyboard.is_pressed('D'):
            # To limit the angle between 0 and 90.
            if(Steering_angle >= 0 and Steering_angle < MAXIMUM_ANGLE):
                Steering_angle += 1 * STEERING_FACTOR
            elif Steering_angle > MAXIMUM_ANGLE:
                Steeing_angle = MAXIMUM_ANGLE

            #print(Steering_angle)
            
            # one zero - Keybiard inouts.
            print([0, 0, 0, 1, 0])
        
        # If we steer left, angle towrds the right increases.
        elif keyboard.is_pressed('A'):
            
            # To limit the angle between 0 and 90.
            if Steering_angle <= 0 and Steering_angle > -MAXIMUM_ANGLE:
                Steering_angle -= 1 * STEERING_FACTOR
            elif Steering_angle < -MAXIMUM_ANGLE:
                Steeing_angle = -MAXIMUM_ANGLE
                
            #print(Steering_angle)
            
            # one zero
            print([0, 1, 0, 0, 0])
             
        # or else steer angle goes to zero.
        else:
            Steering_angle = 0
            #print(Steering_angle)
            
            # one zero
            print([0, 0, 0, 0, 0])
    except:
        pass

    
    if keyboard.is_pressed('Q'):
        break    