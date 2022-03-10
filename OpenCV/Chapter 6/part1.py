import cv2
import numpy as np
import mtutils as mt
from mtutils import PIS
from sqlalchemy import false


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


    ## cv2.line()
    # canvas = np.zeros([300, 300, 3], dtype='uint8')
    # pt1 = [12, 186]
    # pt2 = [192, 399]
    # color = [255, 255, 255]
    # cv2.line(canvas, pt1, pt2, color, thickness=5) 
    # PIS(canvas)


    ## cv2.rectangle() 
    # canvas = np.zeros([300, 300, 3], dtype='uint8')
    # pt1 = [12, 186]
    # pt2 = [192, 199]
    # color = [255, 255, 255]
    # cv2.rectangle(canvas, pt1, pt2, color, thickness=5) 
    # PIS(canvas)


    ## cv2.polyLines()
    # canvas = np.zeros([300, 300, 3], dtype='uint8')
    # pts1 =np.array([[12, 186], [56, 96], [156, 198], [222, 29]])
    # pts2 = np.array([[192, 199], [98, 65], [299, 365], [55, 99]])
    # color = [255, 255, 255]
    # cv2.polylines(canvas, [pts1, pts2], True, color, thickness=5)
    # PIS(canvas)


    ## cv2.putText() 
    # canvas = np.zeros([200, 600, 3], dtype='uint8')
    # text = 'hello world! 表独立兮山之上'
    # origin = [20, 100]
    # fontFace=cv2.FONT_HERSHEY_TRIPLEX
    # fontScale = 1.3
    # color = [255, 255, 0]
    # thickness = 2
    # lineType = 8
    # bottomLeftOrigin = False
    # cv2.putText(canvas, text, origin, fontFace, fontScale, color, thickness, lineType, bottomLeftOrigin) 
    # PIS(canvas)


    ##  cv2.getTextSize() 
    # text = 'hello world!'
    # origin = [20, 100]
    # fontFace=cv2.FONT_HERSHEY_TRIPLEX
    # fontScale = 1.3
    # thickness = 2

    # res = cv2.getTextSize(text, fontFace, fontScale, thickness) 

    pass

