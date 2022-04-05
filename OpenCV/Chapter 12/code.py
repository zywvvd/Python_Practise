import mtutils as mt
import cv2
import numpy as np
from mtutils import PIS


if __name__ == '__main__':
    #  cv2.dft / cv2.idft
    # image = mt.cv_rgb_imread('img1.jpg')
    # image = mt.image_resize(image, [300, 300]).astype('float32')
    # image = mt.to_gray_image(image)

    # dft_res = cv2.dft(image)
    # res = cv2.idft(dft_res)
    # PIS(res)


    # cv2.mulSpectrums
    # a = np.array([[[1, 1], [1, -1]]], dtype='float32')
    # b = np.array([[[2, 1], [1, -2]]], dtype='float32')
    # mul_res = cv2.mulSpectrums(a, b, 0)


    # dft conv
    # # 测试灰度图像
    # image = mt.cv_rgb_imread('img1.jpg', gray=True)
    # image = mt.image_resize(image, [300, 300]).astype('float32')

    # # 卷积核
    # kernal = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype='float32')
    # # Sobel 操作
    # sob_res = cv2.Sobel(image, -1, 1, 0, ksize=3)
    # # 自定义空域卷积操作
    # cus_res = cv2.filter2D(image, -1, kernal)

    # # 频域卷积公式中下标为负，调整卷积核
    # kernal = kernal[:, ::-1]

    # # 获取最佳 DFT 计算尺寸
    # dft_width = cv2.getOptimalDFTSize(image.shape[1] + kernal.shape[1] -1)
    # dft_height = cv2.getOptimalDFTSize(image.shape[0] + kernal.shape[0] -1)

    # # 预留 DFT 空间
    # tempA = np.zeros([dft_height, dft_width], dtype='float32')
    # tempA[:image.shape[0], :image.shape[1]] = image
    # tempB = np.zeros([dft_height, dft_width], dtype='float32')
    # tempB[:kernal.shape[0], :kernal.shape[1]] = kernal

    # # DFT 变换
    # dft_res_A = cv2.dft(tempA, flags=0, nonzeroRows=image.shape[0])
    # dft_res_B = cv2.dft(tempB, flags=0, nonzeroRows=kernal.shape[0])

    # # 频域乘法
    # mul_res = cv2.mulSpectrums(dft_res_A, dft_res_B, flags=cv2.DFT_COMPLEX_OUTPUT)

    # # DFT 反变换
    # inverse_res = cv2.dft(mul_res, flags=cv2.DFT_INVERSE + cv2.DFT_SCALE, nonzeroRows=image.shape[0]-kernal.shape[0] + 1)

    # # 获取计算结果
    # conv_res = inverse_res[:image.shape[0]-kernal.shape[0] + 1, :image.shape[1]-kernal.shape[1] + 1]
    # PIS(sob_res[1:-1, 1:-1], cus_res[1:-1, 1:-1], conv_res)


    ## 图像滤波
    # img = mt.cv_rgb_imread('img1.jpg', gray=True)
        
    # # 第二步：进行数据类型转换
    # img_float = np.float32(img)
    # # 第三步：使用cv2.dft进行傅里叶变化
    # dft = cv2.dft(img_float, flags=cv2.DFT_COMPLEX_OUTPUT)
    # # 第四步：使用np.fft.fftshift将低频转移到图像中心
    # dft_center = np.fft.fftshift(dft)

    # # 第五步：定义掩模：生成的掩模中间为1周围为0，这是保留低频区域
    # crow, ccol = int(img.shape[0] / 2), int(img.shape[1] / 2)  # 求得图像的中心点位置
    # mask_low = np.zeros((img.shape[0], img.shape[1], 2), np.uint8)
    # mask_low[crow - 30:crow + 30, ccol - 30:ccol + 30] = 1

    # mask_hight = np.ones((img.shape[0], img.shape[1], 2), np.uint8)
    # mask_hight[crow - 30:crow + 30, ccol - 30:ccol + 30] = 0

    # # 第六步：将掩模与傅里叶变化后图像相乘
    # # 保留中间部分 低通滤波器
    # mask_img_low = dft_center * mask_low
    # # 保留周围部分 高通滤波器
    # mask_img_hight = dft_center * mask_hight

    # # 第七步：使用np.fft.ifftshift
    # img_idf_low = np.fft.ifftshift(mask_img_low)  # (将低频移动到原来的位置)
    # img_idf_hight = np.fft.ifftshift(mask_img_hight)  # (将高频移动到原来的位置)

    # # 第八步：使用cv2.idft进行傅里叶的反变化
    # img_idf_low = cv2.idft(img_idf_low)
    # img_idf_hight = cv2.idft(img_idf_hight)

    # # 第九步：使用cv2.magnitude转化为空间域内
    # img_idf_low = cv2.magnitude(img_idf_low[:, :, 0], img_idf_low[:, :, 1])
    # img_idf_hight = cv2.magnitude(img_idf_hight[:, :, 0], img_idf_hight[:, :, 1])

    # PIS([img_idf_low, 'Lowpass'], [img_idf_hight, 'Highpass'])


    ## cv2.integral()
    # map = np.ones([5, 5]) + 1
    # sum1 = cv2.integral(map)
    # sum2, sqsum2 = cv2.integral2(map)
    # sum3, sqsum3, tilted = cv2.integral3(map)
    # assert (sum1 == sum2).all() and (sum1 == sum3).all()
    # assert (sqsum2 == sqsum3).all()


    ## cv2.canny
    # img = mt.cv_rgb_imread('img1.jpg', gray=True)
    # res = cv2.Canny(img, 17430, 9000, apertureSize=7, L2gradient=True)
    # PIS(img, res)


    ## cv2.HoughLines
    # img = mt.cv_rgb_imread('hough_line.jpeg')
    # ori_img = img.copy()
    # gray = mt.to_gray_image(img)
    # edge = cv2.Canny(gray, 17430, 34000, apertureSize=7, L2gradient=True)
    # lines = cv2.HoughLines(edge, rho=1, theta=np.pi/180, threshold=170)

    # for line in lines:
    #     rho,theta = line[0]
    #     a = np.cos(theta)
    #     b = np.sin(theta)
    #     x0 = a*rho
    #     y0 = b*rho
    #     x1 = int(x0 + 1000*(-b))
    #     y1 = int(y0 + 1000*(a))
    #     x2 = int(x0 - 1000*(-b))
    #     y2 = int(y0 - 1000*(a))
    
    #     cv2.line(img,(x1,y1),(x2,y2),(250,250,40),2)
    # PIS(ori_img, img)


    ## cv2.HoughLinesP
    # img = mt.cv_rgb_imread('hough_line.jpeg')
    # ori_img = img.copy()
    # gray = mt.to_gray_image(img)
    # edge = cv2.Canny(gray, 17430, 34000, apertureSize=7, L2gradient=True)
    # lines = cv2.HoughLinesP(edge, rho=1, theta=np.pi/180, threshold=30, minLineLength=30, maxLineGap=20)
    # for line in lines:
    #     x1,y1,x2,y2 = line[0]
    #     cv2.line(img,(x1,y1),(x2,y2),(250,255,70),2)
    # PIS(ori_img, img)

    
    ## cv2.HoughCircles
    # img_org = mt.cv_rgb_imread('hough_circles.jpeg', gray=False)
    # img_org = mt.image_resize(img_org, factor=0.4)
    # img = mt.to_gray_image(img_org)

    # res = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1.2, 100, param1=360, param2=120, minRadius=50, maxRadius=300)
    # for circle in res[0]:
    #     x, y, radius = circle
    #     cv2.circle(img_org, mt.vvd_round([x, y]), mt.vvd_round(radius), color=[255, 0, 0], thickness=2)
    # PIS(img_org)


    ## cv2.HoughCircles
    # img_org = mt.cv_rgb_im, read('hough_circles.jpeg', gray=False)
    # img_org = mt.image_resize(img_org, factor=0.4)
    # img = mt.to_gray_image(img_org)

    # res = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT_ALT, 1.2, 120, param1=500, param2=0.85, minRadius=50, maxRadius=300)
    # for circle in res:
    #     x, y, radius = circle[0]
    #     cv2.circle(img_org, mt.vvd_round([x, y]), mt.vvd_round(radius), color=[255, 0, 0], thickness=2)
    # PIS(img_org)


    ## cv2.distanceTransform()
    # img_org = mt.cv_rgb_imread('dis_trans.jpg', gray=True)
    # img = (img_org > 100).astype('uint8')
    # res = cv2.distanceTransform(img, distanceType=cv2.DIST_L2, maskSize=3)
    # PIS(img>0, res)


    ## cv2.distanceTransformWithLabels()
    # img_org = mt.cv_rgb_imread('dis_trans.jpg', gray=True)
    # img = (img_org > 100).astype('uint8')
    # res_ccomp = cv2.distanceTransformWithLabels(img, distanceType=cv2.DIST_L2, maskSize=0, labelType=cv2.DIST_LABEL_CCOMP)
    # res_pixel = cv2.distanceTransformWithLabels(img, distanceType=cv2.DIST_L2, maskSize=0, labelType=cv2.DIST_LABEL_PIXEL)
    # PIS(img_org, res_ccomp[0], res_ccomp[1] % 17, res_pixel[1] % 17)


    ## cv2.floodFill()
    # image = mt.cv_rgb_imread('img1.jpg', gray=True)
    # mask = cv2.Canny(image, 50, 150)
    # mask = cv2.copyMakeBorder(mask,1, 1, 1, 1,cv2.BORDER_CONSTANT, value=1)

    # retval, image, mask, rect = cv2.floodFill(image, mask, seedPoint=[500, 650], newVal=255, loDiff=5, upDiff=5)
    # PIS(image, mask)
    
    ## watershed
    # img = mt.cv_rgb_imread('water.png',)
    # gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # ret,thresh=cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    # kernel=np.ones((3,3),np.uint8)
    # opening=cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel,iterations=2)# 形态开运算
    # sure_bg=cv2.dilate(opening,kernel,iterations=3)

    # dist_transform=cv2.distanceTransform(opening,cv2.DIST_L2,5)
    # ret,sure_fg=cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)
    # sure_fg=np.uint8(sure_fg)
    # unknown=cv2.subtract(sure_bg,sure_fg)
    # ret,connected=cv2.connectedComponents(sure_fg)
    # markers=connected+1
    # markers[unknown==255]=0
    # input_markers = markers.copy()
    # cv2.watershed(img,markers) 

    # PIS(
    #     [img, 'raw image'], 
    #     [thresh, 'threshold'], 
    #     [sure_bg, 'morphology'], 
    #     [dist_transform, 'dist_transform'], 
    #     [sure_fg, 'center'], 
    #     [unknown, 'target_area'],
    #     [connected, 'connected'], 
    #     [input_markers, 'input markers'],
    #     [markers, 'result']
    # )

    # img[markers==-1]=[0, 0, 0]
    # PIS(img)


    ## cv2.grabCut
    # img = mt.cv_rgb_imread('img1.jpg')
    # img = mt.image_resize(img, factor=0.3)
    # OLD_IMG = img.copy()
    # mask = np.zeros(img.shape[:2], np.uint8)
    # SIZE = (1, 65)
    # bgdModle = np.zeros(SIZE, np.float64)
    # fgdModle = np.zeros(SIZE, np.float64)
    # rect = (1, 1, img.shape[1], img.shape[0])
    # cv2.grabCut(img, mask, rect, bgdModle, fgdModle, iterCount=1, mode=cv2.GC_INIT_WITH_RECT)
    # img_1 = img * (mask == 3)[:,:,None]
    # res_dict = dict()
    # res_dict[1] = img_1
    # loop_num = 1
    # iter_each = 1
    # for index in mt.tqdm(range(7)):
    #     cv2.grabCut(img, mask, rect, bgdModle, fgdModle, iterCount=iter_each, mode=cv2.GC_INIT_WITH_MASK)
    #     loop_num += iter_each
    #     res_dict[loop_num] = (img * (mask == 3)[:,:,None])

    # res_list = mt.get_list_from_list(list(res_dict), lambda x: [res_dict[x], 'loop_'+str(x)])
    # res_list = [[OLD_IMG, 'raw image']] + res_list
    # PIS(*res_list)


    ## cv2.pyrMeanShiftFiltering
    # img = mt.cv_rgb_imread('img1.jpg')
    # img = mt.image_resize(img, factor=0.3)
    # res_20_20 = cv2.pyrMeanShiftFiltering(img, sp=20, sr=20, maxLevel=3)
    # res_20_50 = cv2.pyrMeanShiftFiltering(img, sp=20, sr=50, maxLevel=3)
    # res_50_20 = cv2.pyrMeanShiftFiltering(img, sp=50, sr=20, maxLevel=3)
    # res_50_50 = cv2.pyrMeanShiftFiltering(img, sp=50, sr=50, maxLevel=3)
    # res_80_80 = cv2.pyrMeanShiftFiltering(img, sp=80, sr=80, maxLevel=3)
    # PIS([img, 'raw img'], [res_20_20, 'sp: 20 sr:20'], [res_20_50, 'sp: 20 sr:50'], [res_50_20, 'sp: 50 sr:20'], [res_50_50, 'sp: 50 sr:50'], [res_80_80, 'sp: 80 sr:80'])
    pass