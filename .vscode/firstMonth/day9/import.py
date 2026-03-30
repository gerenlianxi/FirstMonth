# 格式：import 模块名 [as 别名]
# 示例1：导入Python内置的math模块（数学工具）
import math
# 调用模块里的功能：模块名.功能名
print(math.sqrt(16))  # sqrt是平方根函数，输出：4.0
# 示例2：导入模块并起别名（简化书写）
import math as m
print(m.sqrt(25))  # 输出：5.0
# 格式1：from 模块名 import 功能1, 功能2
from math import sqrt, pow  # 导入math里的sqrt（平方根）和pow（幂运算）
print(sqrt(9))  # 直接用功能名，输出：3.0
print(pow(2, 3))  # 2的3次方，输出：8.0
# 格式2：导入模块的所有功能（不推荐，易重名）
from math import *
print(sin(0))  # sin是正弦函数，输出：0.0
# 格式3：导入功能并起别名
from math import sqrt as square_root
print(square_root(36))  # 输出：6.0