# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 19:09:26 2020

@author: wasil
"""

import keyboard

# W, A, S, D, SPACE
keys = [0, 0, 0, 0, 0]

while True:
    try:
        # If we steer right, angle towrds the right increases.
        if keyboard.is_pressed('D'):
            # To limit the angle between 0 and 90.
            #if(Steering_angle >= 0 and Steering_angle < MAXIMUM_ANGLE):
            #    Steering_angle += 1 * STEERING_FACTOR
            #elif Steering_angle > MAXIMUM_ANGLE:
            #    Steeing_angle = MAXIMUM_ANGLE
            #print(Steering_angle)
            
            # one zero - Keyboard inputs.
            print([0, 0, 0, 1, 0])
        
        # If we steer left, angle towrds the right increases.
        elif keyboard.is_pressed('A'):
            
            # To limit the angle between 0 and 90.
            #if Steering_angle <= 0 and Steering_angle > -MAXIMUM_ANGLE:
            #    Steering_angle -= 1 * STEERING_FACTOR
            #elif Steering_angle < -MAXIMUM_ANGLE:
            #    Steeing_angle = -MAXIMUM_ANGLE
            #print(Steering_angle)
            
            # one zero
            print([0, 1, 0, 0, 0])
        
        # Accelerate
        elif keyboard.is_pressed('W'):
            #velocity += 1 * 0.05
            #if velocity > 90:
            #    velocity = 90
            #print(velocity)
        
            print([1, 0, 0, 0, 0])
            
        # Reverse
        elif keyboard.is_pressed('W'):
            #velocity += 1 * 0.05
            #if velocity > 90:
            #    velocity = 90
            #print(velocity)
        
            print([0, 0, 1, 0, 0])
        
        elif keyboard.is_pressed('SPACE'):
            print([0, 0, 0, 0, 1])
            
       
        
    except:
        pass

    if keyboard.is_pressed("Q"):
        break




