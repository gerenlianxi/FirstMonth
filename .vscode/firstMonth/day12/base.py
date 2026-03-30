import pandas as pd
# 最简单创建方式
s = pd.Series([1, 2, 3])
print(s)

s = pd.Series([10, 20, 30], index=["A", "B", "C"])
print(s)
print(s.values)   # 查看数据（变成 numpy 数组）
print(s.index)    # 查看索引
print(s.dtype)    # 数据类型

# 按位置
print(s[0])
# 按自定义索引
print(s["A"])
# 切片
print(s[0:2])

print(s + 10)
print(s * 2)
print(s.sum())   # 求和
print(s.mean())  # 平均值