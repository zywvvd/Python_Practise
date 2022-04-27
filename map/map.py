import mtutils as mt
import cv2
import numpy as np


def get_circle(img):
    bg = (img != 0).astype('uint8')
    bg = cv2.morphologyEx(bg, cv2.MORPH_CLOSE, np.ones([19, 19]))
    canny_res = cv2.Canny(bg * 255, 50, 150)
    Xs, Ys = canny_res.nonzero()
    ring_contours = np.stack((Xs, Ys), axis=1).astype('float32')
    ellipse, _ = mt.FitEllipse_RANSAC(ring_contours, max_itts=5, max_refines=2, graphics=True)
    center = ellipse[0][::-1]
    radius = np.mean(ellipse[1]) / 2

    return center, radius


if __name__ == '__main__':
    img_1 = mt.cv_rgb_imread('1.png', gray=True)
    circle_1 = get_circle(img_1)
    img_2 = mt.cv_rgb_imread('2.png', gray=True)
    circle_2 = get_circle(img_2)
    img_3 = mt.cv_rgb_imread('3.png', gray=True)
    circle_3 = get_circle(img_3)
    img_4 = mt.cv_rgb_imread('4.png', gray=True)
    circle_4 = get_circle(img_4)

    log_polar_res1 = cv2.warpPolar(img_1, [500, 1000], circle_1[0], 420, flags=cv2.INTER_CUBIC + cv2.WARP_POLAR_LINEAR + cv2.WARP_POLAR_LOG)
    log_polar_res2 = cv2.warpPolar(img_2, [500, 1000], circle_1[0], 420, flags=cv2.INTER_CUBIC + cv2.WARP_POLAR_LINEAR + cv2.WARP_POLAR_LOG)
    log_polar_res3 = cv2.warpPolar(img_3, [500, 1000], circle_1[0], 420, flags=cv2.INTER_CUBIC + cv2.WARP_POLAR_LINEAR + cv2.WARP_POLAR_LOG)
    log_polar_res4 = cv2.warpPolar(img_4, [500, 1000], circle_1[0], 420, flags=cv2.INTER_CUBIC + cv2.WARP_POLAR_LINEAR + cv2.WARP_POLAR_LOG)

    polar_res1 = cv2.warpPolar(img_1, [500, 1000], circle_1[0], 420, flags=cv2.INTER_CUBIC + cv2.WARP_POLAR_LINEAR)
    polar_res2 = cv2.warpPolar(img_2, [500, 1000], circle_1[0], 420, flags=cv2.INTER_CUBIC + cv2.WARP_POLAR_LINEAR)
    polar_res3 = cv2.warpPolar(img_1, [500, 1000], circle_1[0], 420, flags=cv2.INTER_CUBIC + cv2.WARP_POLAR_LINEAR)
    polar_res4 = cv2.warpPolar(img_2, [500, 1000], circle_1[0], 420, flags=cv2.INTER_CUBIC + cv2.WARP_POLAR_LINEAR)

    mt.PIS(img_1, img_2, img_3, img_4)
    mt.PIS(log_polar_res1, log_polar_res2, log_polar_res3, log_polar_res4)
    mt.PIS(polar_res1, polar_res2, polar_res3, polar_res4)
    pass