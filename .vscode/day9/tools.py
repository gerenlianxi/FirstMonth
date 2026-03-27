# tools.py（保存到当前文件夹）
"""自定义工具模块：包含常用功能"""

def is_even(num):
    """判断是否是偶数"""
    return num % 2 == 0

def sum_list(num_list):
    """计算列表所有元素的和"""
    total = 0
    for num in num_list:
        total += num
    return total

# 定义常量
MAX_NUM = 1000