# main.py
# 方式1：import 模块名
import tools

# 调用is_even函数
print(tools.is_even(8))  # 输出：True
print(tools.is_even(7))  # 输出：False

# 调用sum_list函数
nums = [1,2,3,4,5]
print(f"列表{nums}的和：{tools.sum_list(nums)}")  # 输出：15

# 访问常量
print(f"最大数值限制：{tools.MAX_NUM}")  # 输出：1000

# 方式2：from...import 精准导入
from tools import is_even, MAX_NUM
print(is_even(10))  # 直接调用，输出：True
print(MAX_NUM)      # 输出：1000

# 方式3：导入并起别名
from tools import sum_list as list_sum
print(list_sum([10,20,30]))  # 输出：60