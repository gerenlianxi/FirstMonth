import numpy as np
# 1. 创建一维数组
arr1 = np.array([1,2,3,4,5])
print(arr1)
# 2. 创建二维数组
arr2 = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(arr2)
# 3. 创建全0、全1数组
zeros = np.zeros((2,3))
ones = np.ones((3,2))
print(zeros)
print(ones)
# 4. 创建有序数组 0~9
arr_range = np.arange(10)
print(arr_range)
arr = np.array([[10,20,30],
                [40,50,60],
                [70,80,90]])
# 取值练习
print(arr[0,0])   # 10
print(arr[1,1])   # 50
print(arr[2,2])   # 90
# 取第一行
print(arr[0, :])
# 取第一列
print(arr[:, 0])
# 取左上角 2x2
print(arr[0:2, 0:2])