import json
import time

# 文件名（自动创建）
FILENAME = ".vscode\\day23\\records.json"

# 1. 加载文件中的记录
def load_records():
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

# 2. 保存记录到文件
def save_records(records):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=4)

# 3. 添加记录
def add_record(records):
    amount = input("请输入金额：")
    note = input("请输入备注（吃饭/交通/工资）：")
    t = time.strftime("%Y-%m-%d %H:%M")
    
    record = {
        "amount": amount,
        "note": note,
        "time": t
    }
    records.append(record)
    save_records(records)
    print("✅ 添加成功！")

# 4. 查看所有记录
def show_records(records):
    print("\n====== 所有记录 ======")
    if not records:
        print("暂无记录")
        return
    for i, r in enumerate(records):
        print(f"{i+1}. 【{r['time']}】 {r['note']}：{r['amount']} 元")
    print("========================\n")

# 主程序菜单
def main():
    records = load_records()
    while True:
        print("====== 命令行记账本 ======")
        print("1. 添加记录")
        print("2. 查看记录")
        print("3. 退出")
        choice = input("请输入功能序号：")

        if choice == "1":
            add_record(records)
        elif choice == "2":
            show_records(records)
        elif choice == "3":
            print("👋 退出成功，数据已保存！")
            break
        else:
            print("❌ 输入错误，请重新输入！")

if __name__ == "__main__":
    main()