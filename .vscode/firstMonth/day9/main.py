# main.py（和my_calc.py同文件夹）
# 方式1：import 模块名
import my_calc
print(my_calc.add(5, 3))  # 输出：8
print(my_calc.PI)         # 输出：3.14159

# 方式2：from...import
from my_calc import subtract, PI
print(subtract(10, 4))    # 输出：6