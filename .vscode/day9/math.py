# 练习1：使用math模块（基础import）
import math

# 1. 计算圆的面积（面积=π×r²）
r = 5
area = math.pi * math.pow(r, 2)
print(f"半径为{r}的圆面积：{area:.2f}")  # 保留2位小数，输出：78.54

# 2. 计算绝对值、向上取整
print(math.fabs(-10))  # 绝对值，输出：10.0
print(math.ceil(3.2))  # 向上取整，输出：4
print(math.floor(3.9)) # 向下取整，输出：3

# 练习2：使用random模块（from...import）
from random import randint, choice

# 1. 生成1-100的随机整数
random_num = randint(1, 100)
print(f"1-100的随机数：{random_num}")

# 2. 从列表中随机选一个元素
fruits = ["苹果", "香蕉", "橙子"]
random_fruit = choice(fruits)
print(f"随机水果：{random_fruit}")

# 练习3：使用datetime模块（起别名）
import datetime as dt

# 获取当前时间
now = dt.datetime.now()
print(f"当前时间：{now}")  # 输出：2026-03-24 10:00:00...
# 格式化时间（年-月-日）
print(f"格式化时间：{now.strftime('%Y-%m-%d')}")