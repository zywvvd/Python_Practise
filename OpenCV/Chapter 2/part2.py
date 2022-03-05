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
    
    ## cv2.gemm
    # mat_1 = np.ones([3,5])
    # mat_2 = np.ones([3,5])
    # mat_3 = np.ones([5,5])
    
    # res = cv2.gemm(mat_1, mat_2, 2, mat_3, 3, flags=cv2.GEMM_1_T)
    

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


    ## cv2.inrange()
    # mat = np.random.random([3,3,3,3])
    # res = cv2.inRange(mat, lowerb=0.1, upperb=0.5)
    
    
    ## cv2.invert()
    # mat_1 = np.random.random([3, 3])
    # res_1 = cv2.invert(mat_1)
    # print(np.matmul(mat_1, res_1[1]))
    

    ## cv2.log()
    # mat = np.array([2.71828, 1, 2.7182 ** 2])
    # res = cv2.log(mat)
    
    ## cv2.LUT
    # image = mt.cv_rgb_imread('img1.jpg')
    # image = mt.image_resize(image, factor=0.3)
    # table = np.array([i * 1.5 for i in range (0,256)]).clip(0, 255).astype('uint8')
    # res = cv2.LUT(image, table)
    # PIS(image, res)
    
    
    ## cv2.magnitude()
    # mat_1 = np.ones([3,3])
    # mat_2 = np.ones([3,3])
    
    # res = cv2.magnitude(mat_1, mat_2)
    
    
    ## cv2.Mahalanobis()
    # vector1 =  np.ones([20])
    # vector2 =  np.ones([20])
    # icovar = np.ones([20, 20])
    # cv2.Mahalanobis(vector1, vector2, icovar)
    
    ## cv2.max()
    # vector1 = np.random.random([3, 3])
    # vector2 = np.random.random([3, 3])
    # max_vec = cv2.max(vector1, vector2)
    
    
    ## cv2.mean()
    # vector1 =  np.random.random([3, 3, 3, 3])
    # res = cv2.mean(vector1)
    
    
    ## cv2.meanStdDev()
    # vector1 =  np.random.random([3, 3, 3, 3])
    # res = cv2.meanStdDev(vector1)
    
    
    ## cv2.merge()
    # vector1 = np.zeros([3,4,2])
    # vector2 = np.zeros([3,4,2])
    # vector3 = np.zeros([3,4,2])
    # res = cv2.merge([vector1, vector2, vector3])
    
    
    ## cv2.min()
    # vector1 = np.random.random([3, 3])
    # vector2 = np.random.random([3, 3])
    # min_vec = cv2.min(vector1, vector2)
    
    
    ## cv2.minMaxLoc()
    # vector1 = np.random.random([9, 9])
    # res = cv2.minMaxLoc(vector1)
    
    
    ## mixChannels
    # image_1 = mt.cv_rgb_imread('img1.jpg')
    # image_2 = np.zeros_like(image_1)
    # res = cv2.mixChannels([image_1], [image_2], [0,2,1,1,2,0])
    # PIS(image_1, res[0])
    
    
    ## cv2.multiply()
    # mat_1 = np.ones([3,3]) + 1
    # mat_2 = np.ones([3,3]) + 2
    
    # res = cv2.multiply(mat_1, mat_2)
    
    
    ## cv2.mulTransposed()
    
    # mat_1 = np.reshape(np.arange(9), [3,3]).astype('float32')
    # delta = np.ones_like(mat_1)
    # res = cv2.mulTransposed(mat_1, aTa=True, scale=3, delta=delta)
    
    # np_res = np.matmul(mat_1.T, mat_1)
    
    ## cv2.norm()
    # mat_1 = np.reshape(np.arange(9), [3,3]).astype('float32')
    # res = cv2.norm(mat_1, normType=cv2.NORM_L2)
    
    # mat_1 = np.reshape(np.arange(9), [3,3]).astype('float32')
    # mat_2 = np.ones([3,3]).astype('float32')
    # res = cv2.norm(mat_1, mat_2, normType=cv2.NORM_L1)
    
    
    ##  cv2.normalize()
    # vector1 = np.random.random([3, 3])
    # vector2 = np.zeros_like(vector1)
    
    # res = cv2.normalize(vector1, vector2, norm_type = cv2.NORM_MINMAX, alpha=5, beta=2)
    



    res = cv2.completeSymm(vector_1, lowerToUpper=False)

    image_1 = mt.cv_rgb_imread('img1.jpg')
    image_2 = mt.cv_rgb_imread('img2.jpg')

    image_1 = mt.image_resize(image_1, [300, 300])
    image_2 = mt.image_resize(image_2, [300, 300])

    cv2.checkRange(image_1, False, 0, 255)

    
    pass