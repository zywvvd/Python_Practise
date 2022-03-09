import cv2
import numpy as np
import mtutils as mt
from mtutils import PIS


if __name__ == '__main__':
    
    
    ## cv2.circle()
    canvas = np.zeros([400, 400, 3], dtype='uint8')
    center = [150, 150]
    radius = 50
    color = [255, 255, 0]
    thickness = 4
    lineType = 8
    shift = 0
    cv2.circle(canvas, center, radius, color, thickness, lineType, shift=5)
    
    
    
    
    
    
    
    
    ## cv2.checkRange
    # image_1 = mt.cv_rgb_imread('img1.jpg')
    # image_2 = mt.cv_rgb_imread('img2.jpg')

    # image_1 = mt.image_resize(image_1, [300, 300])
    # image_2 = mt.image_resize(image_2, [300, 300])

    # cv2.checkRange(image_1, False, 0, 255)


    pass

