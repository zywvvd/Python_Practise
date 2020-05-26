import tensorflow as tf
from keras import backend as K
import numpy as np

def iou_keras(y_true, y_pred):
    """
    Return the Intersection over Union (IoU).
    Args:
        y_true: the expected y values as a one-hot
        y_pred: the predicted y values as a one-hot or softmax output
    Returns:
        the IoU for the given label
    """
    label = 1
    # extract the label values using the argmax operator then
    # calculate equality of the predictions and truths to the label
    y_true = K.cast(K.equal(y_true, label), K.floatx())
    y_pred = K.cast(K.equal(y_pred, label), K.floatx())
    # calculate the |intersection| (AND) of the labels
    intersection = K.sum(y_true * y_pred)
    # calculate the |union| (OR) of the labels
    union = K.sum(y_true) + K.sum(y_pred) - intersection
    # avoid divide by zero - if the union is zero, return 1
    # otherwise, return the intersection over union
    return K.switch(K.equal(union, 0), 1.0, intersection / union)

def mean_iou_keras(y_true, y_pred):
    """
    Return the mean Intersection over Union (IoU).
    Args:
        y_true: the expected y values as a one-hot
        y_pred: the predicted y values as a one-hot or softmax output
    Returns:
        the mean IoU
    """
    label = 1
    # extract the label values using the argmax operator then
    # calculate equality of the predictions and truths to the label
    y_true = K.cast(K.equal(y_true, label), K.floatx())
    
    mean_iou = K.variable(0)
    
    thre_list = list(np.arange(0.0000001,0.99,0.05))
    
    for thre in thre_list:
        
        y_pred_temp = K.cast(y_pred >= thre, K.floatx())
        y_pred_temp = K.cast(K.equal(y_pred_temp, label), K.floatx())
        # calculate the |intersection| (AND) of the labels
        intersection = K.sum(y_true * y_pred_temp)
        # calculate the |union| (OR) of the labels
        union = K.sum(y_true) + K.sum(y_pred_temp) - intersection
        iou = K.switch(K.equal(union, 0), 1.0, intersection / union)
        mean_iou = mean_iou + iou
    
    return mean_iou / len(thre_list)


def iou_numpy(y_true,y_pred):
    
    intersection = np.sum(np.multiply(y_true.astype('bool'),y_pred == 1))
    union = np.sum((y_true.astype('bool')+y_pred.astype('bool'))>0)    
    
    return intersection/union


def mean_iou_numpy(y_true,y_pred):
    
    iou_list = []
    for thre in list(np.arange(0.0000001,0.99,0.05)):
        y_pred_temp = y_pred >= thre
        iou = iou_numpy(y_true, y_pred_temp)
        iou_list.append(iou)
        
    #print(iou_list)
    return np.mean(iou_list)


## 随机生成预测值
y_true_np = np.ones([10,10])
y_pred_np = np.random.rand(10,10)

## 真实IoU值
print(f' iou : {iou_numpy(y_true_np, y_pred_np)}')
print(f' mean_iou_numpy : {mean_iou_numpy(y_true_np, y_pred_np)}')

y_true = tf.Variable(y_true_np)
y_pred = tf.Variable(y_pred_np)

## 计算节点
iou_res = iou_keras (y_true, y_pred)
m_iou_res = mean_iou_keras (y_true, y_pred)

## 变量初始化
init_op = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init_op)
    
    result = sess.run(iou_res)
    print(f'result : {result} \nsame with ground truth: {abs(iou_numpy(y_true_np, y_pred_np) - result)< 0.0000001}')
    
    result = sess.run(m_iou_res)
    print(f'result : {result} \nsame with ground truth: {abs(mean_iou_numpy(y_true_np, y_pred_np) - result) < 0.0000001}')   
