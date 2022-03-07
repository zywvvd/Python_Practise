import cv2
import numpy as np
import mtutils as mt
from mtutils import PIS


if __name__ == '__main__':
    
    
    ## cv2.phase
    # x = np.array([1, 0, -1], dtype='float32')
    # y = np.array([1, -1, 1], dtype='float32')
    # res = cv2.phase(x, y)
    
    
    ##cv2.polarToCart
    # mag = np.array(2**0.5)
    # angle = np.array(np.pi/4)
    # res = cv2.polarToCart(mag, angle)
    
    
    ## cv2.pow()
    # data = np.reshape(np.arange(20), [4, 5])
    # res = cv2.pow(data, 2)
    
    
    ## cv2.randu() 
    # data = np.zeros([5, 5])
    # cv2.randu(data, low=2, high=3) 
    
    
    ## cv2.randn
    # data = np.zeros([5, 5])
    # cv2.randn(data, mean=5, stddev=1) 
    
    
    ## cv2.randShuffle() 
    # data = np.reshape(np.arange(25), [5, 5])
    # cv2.randShuffle(data) 
    
    
    ## cv2.reduce()
    # data = np.reshape(np.arange(25, dtype='float32'), [5, 5])
    # res = cv2.reduce(data, 0, rtype=cv2.REDUCE_SUM)
    
    
    ## cv2.repeat()
    # data = np.reshape(np.arange(4, dtype='float32'), [2, 2])
    # res = cv2.repeat(data, 2, 3)
    
    
    ## cv2.setIdentity()
    # mtx = np.random.random([5,6])
    # res = cv2.setIdentity(mtx)
    
    
    ## cv2.solve()
    # A = np.array([[1,2], [2,1]], dtype='float32')
    # B = np.array([[0], [1]], dtype='float32')
    # res = cv2.solve(A, B, flags=cv2.DECOMP_SVD)
    
    
    ## cv2.solveCubic()
    # coeffs = np.array([1,1,-12,0], dtype='float32')
    # res = cv2.solveCubic(coeffs)
    
    
    ## cv2.solvePoly()
    # coeffs = np.array([4, 0, 1], dtype='float32')
    # res = cv2.solvePoly(coeffs)
    

    ## cv2.sort()
    # data = cv2.randShuffle(np.reshape(np.arange(36), [6,6]))
    # res = cv2.sort(data, flags=cv2.SORT_EVERY_ROW)


    ## cv2.sortIdx()  
    # data = cv2.randShuffle(np.reshape(np.arange(36), [6,6]))
    # res = cv2.sortIdx(data,  flags=cv2.SORT_EVERY_ROW)


    ## cv2.split()
    # image = mt.cv_rgb_imread('img1.jpg')
    # res = cv2.split(image)
    # PIS(image, *res)


    ## cv2.sqrt()
    # data = cv2.randShuffle(np.reshape(np.arange(16, dtype='float32'), [4, 4]))
    # res = cv2.sqrt(data) 
    pass
