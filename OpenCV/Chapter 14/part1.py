import mtutils as mt
import cv2
import numpy as np
from mtutils import *


##  findContours()
# img = 255 - mt.cv_rgb_imread('conc.png', gray=True)
# contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# contours = mt.get_list_from_list(contours, lambda x: np.squeeze(x))
# points = np.vstack(contours)
# res = np.zeros_like(img)
# res[points[:, 1], points[:, 0]] = 255
# mt.PIS(img, res)


## drawContours()
# img = 255 - mt.cv_rgb_imread('conc.png', gray=True)
# contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# res = np.zeros_like(img)
# cv2.drawContours(res, contours, 2, [200], -1)
# PIS(img, res)


## cv2.connectedComponents
# img = 255 - mt.cv_rgb_imread('conc.png', gray=True)
# retval, labels = cv2.connectedComponents(img)
# PIS(labels)


## cv2.connectedComponentsWithAlgorithm
# img = 255 - mt.cv_rgb_imread('conc.png', gray=True)
# retval, labels = cv2.connectedComponentsWithAlgorithm(img, 8, cv2.CV_32S, cv2.CCL_WU)
# PIS(labels)


## cv2.approxPolyDP
# img = 255 - mt.cv_rgb_imread('conc.png', gray=True)
# contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# cout_res = cv2.approxPolyDP(contours[0], 10, True)
# res1 = np.zeros_like(img)
# res2 = np.zeros_like(img)
# cv2.drawContours(res1, [contours[0]], -1, [200], 3)
# cv2.drawContours(res2, [cout_res], -1, [200], 3)
# print(len(contours[0]), len(cout_res))
# PIS(res1, res2)


## cv2.arcLength
# contour = np.array([
#     [[0], [0]],
#     [[10], [0]],
#     [[10], [10]],
#     [[0], [10]]
# ])
# length= cv2.arcLength(contour, True)


## cv2.boundingRect
# contour = np.array([
#     [[0], [0]],
#     [[10], [0]],
#     [[20], [10]],
#     [[0], [10]]
# ])
# bbox = cv2.boundingRect(contour)


## cv2.minAreaRect
# contour = np.array([
#     [[5], [0]],
#     [[0], [5]],
#     [[10], [5]],
#     [[5], [10]]
# ])
# cv.minAreaRect(contour)


## cv2.minEnclosingCircle
# contour = np.array([
#     [[5], [0]],
#     [[0], [5]],
#     [[10], [5]],
#     [[5], [10]]
# ])
# center, radius = cv2.minEnclosingCircle(contour)


## cv2.fitEllipse
# contour = np.array([
#     [[5, 0]],
#     [[0, 16]],
#     [[0, 24]],
#     [[10, 16]],
#     [[5, 40]],
#     [[10, 24]]
# ]).astype('float32')
# ellipse = cv2.fitEllipse(contour)
# img = np.zeros([60, 30, 3], dtype='uint8')
# cv2.ellipse(img, ellipse, color=[255, 255, 0], thickness=2)
# PIS(img)


## cv2.fitLine
# contour = np.array([
#     [[5, 5]],
#     [[14, 16]],
#     [[28, 24]],
#     [[10, 11]],
#     [[42, 40]],
#     [[31, 34]]
# ]).astype('int32')
# line = cv2.fitLine(contour, cv2.DIST_L2, 0, 0.01, 0.01)
# pt1 = mt.vvd_round(((line[2] - 100*line[0])[0], (line[3] - 100*line[1])[0]))
# pt2 = mt.vvd_round(((line[2] + 100*line[0])[0], (line[3] + 100*line[1])[0]))

# img = np.zeros([50, 50, 3], dtype='uint8')

# img = cv2.line(img, pt1, pt2, [255, 255, 0], 1)
# img[contour[:,0,0], contour[:,0,1], 2] = 255
# PIS(img)


## cv2.convexHull
# img = 255 - mt.cv_rgb_imread('conc.png', gray=True)
# contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# hull = cv2.convexHull(contours[0])
# res1 = np.zeros_like(img)
# res2 = np.zeros_like(img)
# cv2.drawContours(res1, [contours[0]], -1, [200], 3)
# cv2.drawContours(res2, [hull], -1, [200], 3)
# PIS(res1, res2)


## cv2.pointPolygonTest
# img = 255 - mt.cv_rgb_imread('conc.png', gray=True)
# contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# hull = cv2.convexHull(contours[0])
# point_in = [200, 400]
# point_out = [100, 200]
# res1 = np.zeros_like(img)
# res1[point_in[1]-2:point_in[1]+2, point_in[0]-2:point_in[0]+2] = 255
# res1[point_out[1]-2:point_out[1]+2, point_out[0]-2:point_out[0]+2] = 255
# cv2.drawContours(res1, [contours[0]], -1, [200], 3)
# print(cv2.pointPolygonTest(contours[0], point_in, False))
# print(cv2.pointPolygonTest(contours[0], point_out, False))
# PIS(res1)


## cv2.isContourConvex
# img = 255 - mt.cv_rgb_imread('conc.png', gray=True)
# contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# hull = cv2.convexHull(contours[0])
# res1 = np.zeros_like(img)
# res2 = np.zeros_like(img)
# cv2.drawContours(res1, [contours[0]], -1, [200], 3)
# cv2.drawContours(res2, [hull], -1, [200], 3)
# print(cv2.isContourConvex(contours[0]))
# print(cv2.isContourConvex(hull))
# PIS(res1, res2)
pass


