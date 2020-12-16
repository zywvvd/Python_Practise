import cv2
import numpy as np


def get_point(event, x, y, flags, param):
    # 鼠标单击事件
    if event == cv2.EVENT_LBUTTONDOWN:
        # 输出坐标
        print('clicking: ', x, y)
        # 在传入参数图像上画出该点
        cv2.circle(param, (x, y), 1, (255, 255, 255), thickness=-1)


if __name__ == "__main__":
    # 定义两幅图像
    image_1 = np.zeros((200, 200, 3), dtype='uint8')
    image_2 = np.zeros((200, 200, 3), dtype='uint8')

    # 定义两个窗口 并绑定事件 传入各自对应的参数
    cv2.namedWindow('image_1')
    cv2.setMouseCallback('image_1', get_point, image_1)

    cv2.namedWindow('image_2')
    cv2.setMouseCallback('image_2', get_point, image_2)

    # 显示图像
    while(True):
        cv2.imshow('image_1', image_1)
        cv2.imshow('image_2', image_2)
        if cv2.waitKey(20) & 0xFF == 27:
            break

    # 销毁窗口
    cv2.destroyAllWindows()
