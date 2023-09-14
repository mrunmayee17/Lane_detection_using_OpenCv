import numpy as np
import cv2

def region_of_interest(image):
    height = image.shape[0]
    # for finding path lines
    # triangle = np.array([(200,height), (1100,height), (550,250)])
    polygons = np.array([[(200,height), (1100,height), (550,250)]])
    # Mask creating an 0 intensity image same as dimenions of the original image. 
    mask = np.zeros_like(image) 
    cv2.fillPoly(mask, polygons, 255)
    masked_img = cv2.bitwise_and(mask,image)
    return masked_img