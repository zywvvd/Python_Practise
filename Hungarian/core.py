from scipy.optimize import linear_sum_assignment
import numpy as np
  
cost =np.array(
    [
        [12,7,9,7,9],
        [8,9,6,6,6],
        [7,17,12,14,9],
        [15,14,6,6,10],
        [4,10,7,10,9]
    ])
row_ind, col_ind=linear_sum_assignment(cost)
res = np.zeros_like(cost)
res[row_ind, col_ind] = 1
print(res)                          # 结果矩阵
print(cost[row_ind,col_ind].sum())  # 数组求和，求得总花费

pass