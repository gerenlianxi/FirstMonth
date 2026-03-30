# 练习5：读取文件并统计行数
def count_lines(filename):
    """统计文件的行数"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
            print(f"文件{filename}共有{len(lines)}行内容")
    except FileNotFoundError:
        print(f"错误：文件{filename}不存在！")

# 调用：统计study_record.txt的行数
count_lines(".vscode\\day7+day8\\last.txt")
# 练习6：批量写入列表内容到文件
# 把学习计划列表写入文件
study_plan = [
    "Day1：基础语法",
    "Day2：变量、字符串",
    "Day3：列表、字典",
    "Day4：if判断",
    "Day5：for/while循环",
    "Day6：函数",
    "Day7：文件读写"
]
with open(".vscode\\day7+day8\\last.txt", "w", encoding="utf-8") as f:
    # 遍历列表，逐行写入
    for plan in study_plan:
        f.write(plan + "\n")
print("学习计划已写入study_plan.txt！")