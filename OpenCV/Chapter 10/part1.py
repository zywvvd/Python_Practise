import cv2
import numpy as np
import mtutils as mt
from mtutils import PIS


if __name__ == '__main__':
    
    
    ## cv2.copyMakeBorder()
    # image = mt.cv_rgb_imread('img1.jpg')
    # res = cv2.copyMakeBorder(image, 1, 1, 1, 1, borderType=cv2.BORDER_CONSTANT, value=(255, 255, 0))
    # res = cv2.copyMakeBorder(res, 180, 180, 180, 180, borderType=cv2.BORDER_REFLECT)
    # PIS(res)

    
    ## cv2.borderInterpolate()
    # cv2.borderInterpolate(10, 1000, cv2.BORDER_REFLECT)
    
    
    ## cv2.threshold()
    # img = mt.cv_rgb_imread('img1.jpg')
    # res = cv2.threshold(img, 120, 200, cv2.THRESH_BINARY)
    # PIS(res[1])
    
    # img = mt.cv_rgb_imread('img1.jpg')
    # res = cv2.threshold(img[:,:,0], 0, 255, cv2.THRESH_OTSU)
    # PIS(res[1])


    ## cv2.adaptiveThreshold()
    # img = mt.cv_rgb_imread('img1.jpg', gray=True)
    # res = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 0)
    # PIS(res)

    # img = mt.cv_rgb_imread('img1.jpg', gray=True)
    # res = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 0)
    # PIS(res)


    ## cv2.blur()
    # img = mt.cv_rgb_imread('img1.jpg', gray=True)
    # res = cv2.blur(img, [17, 17])
    # PIS(img, res)


    ## cv2.medianBlur()
    # img = mt.cv_rgb_imread('img1.jpg', gray=False)
    # res = cv2.medianBlur(img, 17)
    # PIS(img, res)
    
    
    ## cv2.GaussianBlur()
    # img = mt.cv_rgb_imread('img1.jpg', gray=False)
    # res = cv2.GaussianBlur(img, [17, 17], 10, 10)
    # PIS(img, res)
    
    
    ## cv2.boxFilter()
    # img = mt.cv_rgb_imread('img1.jpg', gray=False)
    # res = cv2.boxFilter(img, 3, [17, 17])
    # PIS(img, res)
    
    
    ## cv2.bilateralFilter()
    # img = mt.cv_rgb_imread('img1.jpg', gray=False)
    # res = cv2.bilateralFilter(img, 15, 100, 1000)
    # PIS(img, res)


    ## cv2.Sobel()
    # img = mt.cv_rgb_imread('img1.jpg', gray=False)
    # x0y2k7 = cv2.Sobel(img, -1, 0, 2, ksize=7)
    # x2y0k7 = cv2.Sobel(img, -1, 2, 0, ksize=7)
    # x3y3k7 = cv2.Sobel(img, -1, 3, 3, ksize=7)
    # PIS(img, [x0y2k7, 'x0y2k7'], [x2y0k7, 'x2y0k7'], [x3y3k7, 'x3y3k7'])

    # img = mt.cv_rgb_imread('img1.jpg', gray=False)
    # res = cv2.Sobel(img, -1, 1, 0, ksize=cv2.FILTER_SCHARR)
    # PIS(img, res)

    ## cv2.Laplacian()
    # img = mt.cv_rgb_imread('img1.jpg', gray=False)
    # res3 = cv2.Laplacian(img, -1, ksize = 3)
    # res5 = cv2.Laplacian(img, -1, ksize = 5)
    # res7 = cv2.Laplacian(img, -1, ksize = 7)
    # PIS(img, res3, res5, res7)
    
    ## cv2.erode
    # img = mt.cv_rgb_imread('img1.jpg', gray=False)
    # kernal = np.ones([1, 58])
    # res = cv2.erode(img, kernal)
    # PIS(img, res)
    
    ## cv2.dilate
    # img = mt.cv_rgb_imread('img1.jpg', gray=False)
    # kernal = np.ones([1, 58])
    # res = cv2.dilate(img, kernal)
    # PIS(img, res)
    
    
    ## cv2.morphologyEx()
    # img = mt.cv_rgb_imread('test.jpg', gray=True)
    # kernal_1d = cv2.getGaussianKernel(5, 1)
    # kernal_2d = kernal_1d* kernal_1d.T
    # erode = cv2.morphologyEx(img, cv2.MORPH_ERODE, kernal_2d)
    # dilate = cv2.morphologyEx(img, cv2.MORPH_DILATE, kernal_2d)
    # open = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernal_2d)
    # close = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernal_2d)
    # gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernal_2d)
    # tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernal_2d)
    # blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernal_2d)
    # PIS([img, 'origin'], [erode, 'erode'], [dilate, 'dilate'], [open, 'open'], [close, 'close'], [gradient, 'gradient'], [tophat, 'tophat'], [blackhat, 'blackhat'])
    
    # binary_array = (np.random.random([20, 20]) > 0.5).astype('uint8')
    # kernal = np.array([[1, -1, 1], [-1, 1, 1], [1, 1, 0]])
    # res = cv2.morphologyEx(binary_array, cv2.MORPH_HITMISS, kernal)
    # PIS(binary_array, res, kernal)
    
    
    ## cv2.getStructuringElement
    # cross = cv2.getStructuringElement(cv2.MORPH_CROSS, [5,5])
    # rect = cv2.getStructuringElement(cv2.MORPH_RECT, [5,5])
    # ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, [5,5])
    # PIS(cross, rect, ellipse)


    ## cv2.filter2D()
    # img = mt.cv_rgb_imread('img1.jpg', gray=False)
    # kernal = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    # sob_res = cv2.Sobel(img, -1, 1, 0, ksize=3)
    # cus_res = cv2.filter2D(img, -1, kernal)
    # PIS(sob_res, cus_res)


    ## cv2.sepFilter2D(
    # img = mt.cv_rgb_imread('img1.jpg', gray=False)
    # kernal_x = np.array([[-1, 0, 1]])
    # kernal_y = np.array([[1], [2], [1]])
    # sob_res = cv2.Sobel(img, -1, 1, 0, ksize=3)
    # cus_res = cv2.sepFilter2D(img, -1, kernal_x, kernal_y)
    # PIS(sob_res, cus_res)


    ## cv2.getDerivKernels()
    # kx, ky = cv2.getDerivKernels(1, 0, cv2.FILTER_SCHARR, normalize=False, ktype=cv2.CV_64F)


    ## cv2.getGaussianKernel
    # g1d = cv2.getGaussianKernel(9, 3)
    # g2d = np.matmul(g1d, g1d.T)
    # PIS(g2d)
    pass

