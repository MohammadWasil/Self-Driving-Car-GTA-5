# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 17:50:22 2020

@author: wasil
"""

import keyboard


velocity = 0

while True:
    # Accelerate
    if keyboard.is_pressed('W'):
        velocity += 1 * 0.05
        
        if velocity > 90:
            velocity = 90
        #print(velocity)
        
        print([1, 0, 0, 0, 0])
    
    # Reverse
    elif keyboard.is_pressed('S'):
        velocity -= 1 * 0.05
        
        # Reverse acceleration.
        if velocity < -25:
            velocity = -25
        
        #print(velocity)
        
        print([0, 0, 1, 0, 0])
    
    # Apply brakes.
    elif keyboard.is_pressed('space'):
        velocity -= 1 * 0.1
        
        if velocity < 0:
            velocity = 0
        
        #print(velocity)
        
        print([0, 0, 0, 0, 1])
        
    # Car is still, not moving, zero velocity.
    else:
        velocity -= 1*0.001
        
        if velocity < 0:
            velocity = 0
        #print(velocity)
    
    
    
    if keyboard.is_pressed('Q'):
        break  