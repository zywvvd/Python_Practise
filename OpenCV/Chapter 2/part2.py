import cv2
import numpy as np
import mtutils as mt
from mtutils import PIS


if __name__ == '__main__':
    
    ## cv2.exp() 
    # vector = np.ones([3, 3]) + 1
    # res = cv2.exp(vector)
    

    ## cv2.flip
    # image_1 = mt.cv_rgb_imread('img1.jpg')
    # y_flip = cv2.flip(image_1, flipCode=1)
    # x_flip = cv2.flip(image_1, flipCode=0)
    # xy_flip = cv2.flip(image_1, flipCode=-1)
    # PIS([image_1,'origin'], [y_flip, 'flipCode 1 y flip'], [x_flip, 'flipCode 0 x flip'], [xy_flip, 'flipCode -1 xy flip'])
    
    
    res = cv2.compare(vector_1, vector_2, cmpop=cv2.CMP_GE)

    res = cv2.completeSymm(vector_1, lowerToUpper=False)

    image_1 = mt.cv_rgb_imread('img1.jpg')
    image_2 = mt.cv_rgb_imread('img2.jpg')

    image_1 = mt.image_resize(image_1, [300, 300])
    image_2 = mt.image_resize(image_2, [300, 300])

    cv2.checkRange(image_1, False, 0, 255)

    
    pass