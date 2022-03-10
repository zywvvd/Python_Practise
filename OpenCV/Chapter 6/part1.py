import cv2
import numpy as np
import mtutils as mt
from mtutils import PIS


if __name__ == '__main__':
    
    
    ## cv2.circle()
    # canvas = np.zeros([400, 400, 3], dtype='uint8')
    # center = [150, 150]
    # radius = 50
    # color = [255, 255, 0]
    # thickness = 4
    # lineType = 8
    # shift = 0
    # cv2.circle(canvas, center, radius, color, thickness, lineType, shift)
    # PIS(canvas)
    
    
    ## cv2.clipLine() 
    # rec = [20, 20, 80, 80]
    # point1 = [210, 110]
    # point2 = [110, 110]
    # res = cv2.clipLine(rec, point1, point2) 
    
    
    ## cv2.ellipse
    # canvas = np.zeros([400, 400, 3], dtype='uint8')
    # center = [150, 150]
    # axes = [100, 70]
    # angle = 45
    # color = [255, 0, 255]
    # thickness = -1
    # cv2.ellipse(canvas, [center, axes, angle], color, thickness)
    # PIS(canvas)


    ## cv2.ellipse2Poly()
    # canvas = np.zeros([400, 400, 3], dtype='uint8')
    # center = [150, 150]
    # axes = [100, 70]
    # angle = 45
    # startAngle = 0
    # endAngle = 270
    # delta = 30
    # color = [0, 255, 255]
    # points = cv2.ellipse2Poly(center, axes, angle, startAngle, endAngle, delta)
    # cv2.fillPoly(canvas, [points], color)
    # PIS(canvas)


    ## cv2.fillConvexPoly() 
    # canvas = np.zeros([300, 300, 3], dtype='uint8')
    # porints = np.array([[20, 50], [130, 30], [125, 100]])
    # color = [0, 255, 0]
    # cv2.fillConvexPoly(canvas, porints, color) 
    # PIS(canvas)


    ## cv2.fillPoly()
    # canvas = np.zeros([300, 300, 3], dtype='uint8')
    # porints1 = np.array([[20, 50], [130, 30], [125, 100]])
    # porints2 = porints1[:, ::-1]
    # color = [0, 0, 255]
    # cv2.fillPoly(canvas, [porints1, porints2], color)
    # PIS(canvas)


    pass

