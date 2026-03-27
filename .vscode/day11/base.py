import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)   # [5 7 9]
print(a - b)   # [-3 -3 -3]
print(a * b)   # [ 4 10 18]
print(a / b)   # [0.25 0.4 0.5]
print(a @ b)

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
print(a * b)

# 两种写法都可以
c = np.dot(a, b)
c = a @ b  # 推荐
print(c)
arr = np.array([[1,2,3],
                [4,5,6]])

print(np.sum(arr))    # 总和
print(np.mean(arr))   # 均值
print(np.var(arr))    # 方差
print(np.std(arr))    # 标准差
print(np.max(arr))    # 最大值
print(np.min(arr))    # 最小值

print(np.sum(arr, axis=0))  # 每列求和
print(np.sum(arr, axis=1))  # 每行求和