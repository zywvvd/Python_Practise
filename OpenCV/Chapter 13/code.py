import cv2
import mtutils as mt
from mtutils import PIS
import numpy as np

# def hist2d_demo(image):
#     # 图像转换为HSV
#     hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#     # 计算图像的直方图
#     hist = cv2.calcHist([image], [0, 1], None, [32, 32], [0, 180, 0, 256])


## cv2.normalize
# img = mt.cv_rgb_imread('img.jpg', gray=True)
# hist = cv2.calcHist([img], [0], None, [256], [0, 255]) 
# res = cv2.normalize(hist, None, alpha=1, norm_type=cv2.NORM_L2)
# PIS(hist[:, 0], res[:, 0])


## cv2.threshold
# img = mt.cv_rgb_imread('img.jpg', gray=True)
# hist = cv2.calcHist([img], [0], None, [256], [0, 255])
# res = cv2.normalize(hist, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
# thre, res_hist = cv2.threshold(res, 50, 0, cv2.THRESH_TOZERO)
# PIS(hist[:, 0], res_hist[:, 0])


## cv2.minMaxLoc
# img = mt.cv_rgb_imread('img.jpg', gray=True)
# hist = cv2.calcHist([img], [0], None, [256], [0, 255])
# min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(hist)


## cv2.compareHist
# hist1 = np.random.random([80]).astype('float32')
# hist2 = np.random.random([80]).astype('float32')
# dis = cv2.compareHist(hist1, hist2, method=cv2.HISTCMP_KL_DIV)


## cv2.EMD
# hist1 = np.array([0,0,1,2,3,4,5,6,0,0], dtype='float32')
# hist2 = np.array([1,2,3,4,5,6,0,0,0,0], dtype='float32')

# cost = np.ones([len(hist1), len(hist1)], dtype='float32')

# retval, lowerBound, flow = cv2.EMD(hist1, hist2, cv2.DIST_USER, cost)
# hist1 = np.array([0,0,1,2,3,4,5,6,0,0], dtype='float32')
# hist2 = np.array([1,2,3,4,5,6,0,0,0,0], dtype='float32')

# signature_1 = np.concatenate([[hist1], [np.arange(len(hist1))]]).astype('float32').T
# signature_2 = np.concatenate([[hist2], [np.arange(len(hist2))]]).astype('float32').T

# retval, lowerBound, flow = cv2.EMD(signature_1, signature_2, cv2.DIST_L1)


##cv2.calcBackProject
# # 读取图片
# sample = cv2.imread("sample.jpeg")
# target = cv2.imread("target.jpeg")
# # 转换为HSV格式
# roi_hsv = cv2.cvtColor(sample, cv2.COLOR_BGR2HSV)
# target_hsv = cv2.cvtColor(target, cv2.COLOR_BGR2HSV)

# # show images
# cv2.imshow("sample", sample)
# cv2.imshow("target", target)
# # 计算图像直方图
# roiHist = cv2.calcHist([roi_hsv], [0, 1], None, [64, 64], [0, 180, 0, 256])
# # 图像归一化处理
# cv2.normalize(roiHist, roiHist, 0, 255, cv2.NORM_MINMAX)
# # 获取直方图的反向投影
# dst = cv2.calcBackProject([target_hsv], [0, 1], roiHist, [0, 180, 0, 256], 1)

# PIS(dst, cmap='gray')




pass