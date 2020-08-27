# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 20:19:40 2020

@author: Mohammad Wasil Saleem
"""

import os
import cv2
import numpy as np
from PIL import ImageGrab

PATH_TO_SAVE_IMAGES = "D:\ML\Self Driving Car\Self Driving Car with GTA 5\Images"


print("Grabbing Images... ")
image_counter = 0
while True:
        
    image_counter += 1
    # (left_x, top_y, right_x, bottom_y)
    captured_image = np.array(ImageGrab.grab(bbox=(0, 35, 1600, 925)))          # Taking the screenshot and convert to numpy array.
    
    # Path to save the file.
    path = r"{}".format(PATH_TO_SAVE_IMAGES)
    # A unique image name for eah individual image.
    imageName = r"train_{}.png".format(image_counter)
    
    # convert bgr to rgb.
    im_rgb = cv2.cvtColor(captured_image, cv2.COLOR_BGR2RGB)
    # Trying to save the image in the exact same directory.
    cv2.imwrite(os.path.join(path, imageName), im_rgb)
    
    '''if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
    '''

print("Done!")