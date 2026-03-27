# 实战：学习记录读写工具
def add_record(content):
    """添加学习记录到文件（追加模式）"""
    # 拼接时间+内容（简化版，新手先写固定时间）
    record = f"2026-03-23：{content}\n"
    # 追加写入（a模式，不会清空原有记录）
    with open(".vscode\\day7+day8\\study.txt", "a", encoding="utf-8") as f:
        f.write(record)
    print("记录添加成功！")

def view_records():
    """查看所有学习记录"""
    try:
        # 读取文件（r模式）
        with open(".vscode\\day7+day8\\study.txt", "r", encoding="utf-8") as f:
            records = f.read()
        if not records:  # 如果文件为空
            print("暂无学习记录！")
        else:
            print("===== 我的学习记录 =====")
            print(records)
    except FileNotFoundError:
        # 处理文件不存在的情况
        print("暂无学习记录！")

# 主逻辑：选择功能
print("===== 学习记录工具 =====")
choice = input("请选择操作（1-添加记录，2-查看记录）：")
if choice == "1":
    content = input("请输入学习记录内容：")
    add_record(content)
elif choice == "2":
    view_records()
else:
    print("无效选择！")