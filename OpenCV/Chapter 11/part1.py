import cv2
import numpy as np
import mtutils as mt
from mtutils import PIS
from matplotlib import pyplot as plt


if __name__ == '__main__':
    
    
    ## cv2.resize()
    # image = mt.cv_rgb_imread('img1.jpg')
    # res1=cv2.resize(image, [600, 300])
    # res2=cv2.resize(image, None,  fx=0.5,fy = 1.5)
    # PIS(res1, res2)


    ## cv.pyrDown
    # image = mt.cv_rgb_imread('img1.jpg')
    # res = cv2.pyrDown(image)
    # PIS(image, res)
    
    ## cv.pyrUp
    # image = mt.cv_rgb_imread('img1.jpg')
    # res = cv2.pyrUp(image)
    # PIS(image, res)


    ## laplacian
    # image = mt.cv_rgb_imread('img1.jpg')
    # gaussian = cv2.pyrDown(image)
    # laplacian = image - cv2.pyrUp(gaussian)
    # PIS(image, laplacian)


    ## 	cv2.warpAffine
    # image = mt.cv_rgb_imread('img1.jpg')
    # M = np.array([[2, 0, 200], [0, 1, 200]], dtype='float32')
    # res = cv2.warpAffine(image, M , [3000, 1500])
    # PIS(res)


    ## cv2.getAffineTransform()
    # src = np.array([
    #     [100, 100],
    #     [100, 200],
    #     [200, 200]
    # ], dtype='float32')

    # tar = (src * np.array([2, 1]) + np.array([100, 100])).astype('float32')
    # retval = cv2.getAffineTransform(src, tar)


    ## cv2.transform()
    # src = np.array([
    #     [100, 100],
    #     [100, 200],
    #     [200, 200]
    # ], dtype='float32')
    # M = np.array([
    #    [  2.,   0., 100.],
    #    [  0.,   1., 100.]
    #    ])
    # src = src.reshape((-1, 1, 2))
    # trans_tar = cv2.transform(src, M)


    ## cv2.invertAffineTransform()
    # M = np.array([
    #    [  2.,   0., 100.],
    #    [  0.,   1., 100.]
    #    ])
    # inv_M = cv2.invertAffineTransform(M)


    ## cv2.getPerspectiveTransform()
    # src_points = np.array([
    #     [100, 100],
    #     [100, 200],
    #     [200, 200],
    #     [200, 100]
    # ], dtype='float32')

    # tar_points = np.array([
    #     [76, 91],
    #     [113, 209],
    #     [169, 188],
    #     [156, 77]
    # ], dtype='float32')
    # M =cv2.getPerspectiveTransform(src_points, tar_points)


    ## cv2.warpPerspective()
    # image = mt.cv_rgb_imread('img1.jpg')
    # M = np.array([
    #    [1.2, -0.5, 1.],
    #    [1., 0.5, 1.],
    #    [0.001, -0.001, 1]
    #    ])
    # res = cv2.warpPerspective(image, M, [800, 2000])
    # PIS(res)


    ## cv2.perspectiveTransform()
    # src_points = np.array([
    #     [100, 100],
    #     [100, 200],
    #     [200, 200],
    #     [200, 100]
    # ], dtype='float32').reshape(-1, 1, 2)
    # M = np.array([[ 2.18177483e+00,  1.75775497e+00, -2.30653642e+02],
    #    [-7.23642384e-02,  4.31608940e+00, -2.28843046e+02],
    #    [ 2.96688742e-03,  8.51986755e-03,  1.00000000e+00]], dtype='float32')
    # tar_points = cv2.perspectiveTransform(src_points, M)


    ## cv2.warpPolar()
    # polar_img = mt.cv_rgb_imread('polar.jpg')
    # center = (185, 166)
    # radius = 161
    # polar_res = cv2.warpPolar(polar_img, [-1, -1], center, radius, flags=cv2.INTER_CUBIC + cv2.WARP_POLAR_LINEAR)
    # inverse = cv2.warpPolar(polar_res, [350, 350], center, radius, flags=cv2.INTER_CUBIC + cv2.WARP_POLAR_LINEAR+ cv2.WARP_INVERSE_MAP)
    # PIS(inverse)

    # polar_img = mt.cv_rgb_imread('polar.jpg')
    # center = (185, 166)
    # radius = 161
    # polar_res = cv2.warpPolar(polar_img, [-1, -1], center, radius, flags=cv2.INTER_CUBIC + cv2.WARP_POLAR_LINEAR + cv2.WARP_POLAR_LOG)
    # inverse = cv2.warpPolar(polar_res, [350, 350], center, radius, flags=cv2.INTER_CUBIC + cv2.WARP_POLAR_LINEAR+ cv2.WARP_INVERSE_MAP + cv2.WARP_POLAR_LOG)
    # PIS(polar_res, inverse)


    ## cv2.remap()
    # img = mt.cv_rgb_imread('img1.jpg')
    # img = mt.image_resize(img, [400, 300])
    # y_map = np.arange(300).astype('float32')
    # x_map = np.arange(400).astype('float32')
    # x_map = x_map[::-1]
    # xmap, ymap = np.meshgrid(x_map, y_map)
    # res = cv2.remap(img, xmap, ymap, cv2.INTER_LINEAR)
    # PIS(res)


    ## cv2.inpaint()
    # img = mt.cv_rgb_imread('img1_inpaint.png')
    # mask = (img[:,:, 0] > 254).astype('uint8')
    # res_1 = cv2.inpaint(img, mask, 12, cv2.INPAINT_NS)
    # res_2 = cv2.inpaint(img, mask, 12, cv2.INPAINT_TELEA)
    # PIS(img, mask, [res_1, 'cv2.INPAINT_NS'], [res_2, 'cv2.INPAINT_TELEA'])

    # img = mt.cv_rgb_imread('img2_gray.jpg', gray=True)
    # hist = cv2.calcHist(img, [0], None, [256], [0,255]) 
    # PIS(img, hist[:, 0])


    ## cv2.equalizeHist()
    # img = mt.cv_rgb_imread('img2_gray.jpg', gray=True)
    # hist = cv2.calcHist(img, [0], None, [256], [0,255]) 
    # res = cv2.equalizeHist(img)
    # res_hist = cv2.calcHist(res, [0], None, [256], [0,255]) 
    # PIS(img, hist[:, 0], res, res_hist[:, 0], cmap='gray')
    pass

