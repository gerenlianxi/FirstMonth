import numpy as np  # 行业标准写法，必须记住
a = np.array([[1,2,3], [4,5,6],[7,8,9]])  # 创建一个2行3列的二维数组

print(a.shape)   # 形状 (2行3列)
print(a.ndim)    # 维度 2
print(a.dtype)   # 数据类型 int64
print(a[0, 1])   # 第0行第1列 → 2
print(a[1, 2])   # 第1行第2列 → 6
# 取第0行所有
print(a[0, :])
# 取所有行的第1列
print(a[:, 1])
# 取 0~1行，1~2列
print(a[0:2, 1:2])