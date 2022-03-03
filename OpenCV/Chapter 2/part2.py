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
    
    

    ## cv2.idct()
    # image = mt.cv_rgb_imread('img1.jpg')
    # image = mt.image_resize(image, [300, 300]).astype('float32')
    # image = mt.to_gray_image(image)
    
    # dct_res = cv2.dct(image)

    # res = cv2.idct(dct_res)
    # PIS(res)


    ## cv2.idft()
    # image = mt.cv_rgb_imread('img1.jpg')
    # image = mt.image_resize(image, [300, 300]).astype('float32')
    # image = mt.to_gray_image(image)
    
    # dft_res = cv2.dft(image)
    # res = cv2.idft(dft_res)
    # PIS(res)

    res = cv2.compare(vector_1, vector_2, cmpop=cv2.CMP_GE)

    res = cv2.completeSymm(vector_1, lowerToUpper=False)

    image_1 = mt.cv_rgb_imread('img1.jpg')
    image_2 = mt.cv_rgb_imread('img2.jpg')

    image_1 = mt.image_resize(image_1, [300, 300])
    image_2 = mt.image_resize(image_2, [300, 300])

    cv2.checkRange(image_1, False, 0, 255)

    
    pass