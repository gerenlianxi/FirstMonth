# 练习4：结合模块实现“随机抽奖程序”
import random
from datetime import datetime

def lottery(participants):
    """抽奖函数：从参与者列表中随机选1个中奖者"""
    if not participants:
        return "暂无参与者！"
    winner = random.choice(participants)
    # 获取当前时间作为抽奖时间
    draw_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"【{draw_time}】中奖者：{winner}"

# 参与者列表
participants = ["张三", "李四", "王五", "赵六"]
# 调用抽奖函数
print(lottery(participants))  # 输出示例：【2026-03-24 10:10:00】中奖者：李四