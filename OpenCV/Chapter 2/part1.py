import cv2
import numpy as np
import mtutils as mt
from mtutils import PIS


if __name__ == '__main__':
    
    ## cv2.checkRange
    # image_1 = mt.cv_rgb_imread('img1.jpg')
    # image_2 = mt.cv_rgb_imread('img2.jpg')

    # image_1 = mt.image_resize(image_1, [300, 300])
    # image_2 = mt.image_resize(image_2, [300, 300])

    # cv2.checkRange(image_1, False, 0, 255)


    ## cv2.convertScaleAbs
    # vector = np.random.random([100, 100]) * 200
    # res = cv2.convertScaleAbs(vector, alpha=1.0, beta=0.0)


    ## cv2.countNonZero
    # vector = np.random.random([100, 100]) 
    # vector = np.clip(vector - 0.3, 0, 1)
    
    # num = cv2.countNonZero(vector)

    ## cv2.cvtColor()
    # image = mt.cv_rgb_imread('img1.jpg')
    # bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    # PIS(image, bgr)

    ## cv2.dct()
    # image = mt.cv_rgb_imread('img1.jpg')
    # image = mt.image_resize(image, [300, 300]).astype('float32')
    # image = mt.to_gray_image(image)
    
    # dct_res = cv2.dct(image)
    # inverse_img = cv2.dct(dct_res, flags=cv2.DCT_INVERSE)

    # PIS(image, (dct_res*150).astype('uint8'), inverse_img.astype('uint8'))
    
    ## cv2.determinant()
    # vector =(np.random.random([3, 3]) * 5).astype('int32').astype('float32')
    # res = cv2.determinant(vector)
    
    ## cv2.dft()
    # image = mt.cv_rgb_imread('img1.jpg')
    # image = mt.image_resize(image, [300, 300]).astype('float32')
    # image = mt.to_gray_image(image)
    
    # dft_res = cv2.dft(image)
    # inverse_img = cv2.dft(dft_res, flags=cv2.DFT_INVERSE)

    # PIS(image, dft_res, inverse_img)
    
    ## cv2.divide()  
    # mat_1 = np.random.random([5, 5, 5, 5])
    # mat_2 = np.random.random([5, 5, 5, 5])
    
    # res = cv2.divide(mat_1,mat_2)  
    
    ## cv2.eigen()
    # mat = np.random.random([5, 5])
    # res = cv2.eigen(mat)
    pass

