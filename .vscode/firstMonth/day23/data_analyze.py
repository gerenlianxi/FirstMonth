import json

# 1. 读取记账数据
def load_data():
    try:
        with open(".vscode\\day23\\records.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

# 2. 数据分析核心函数（今天重点！）
def analyze_data(records):
    if not records:
        print("暂无数据可分析")
        return

    # 统计总金额 
    total = 0
    for r in records:
        total += float(r["amount"])  # 字符串转数字

    # 统计平均
    avg = total / len(records)

    # 找金额最大的记录
    max_record = records[0]
    for r in records:
        if float(r["amount"]) > float(max_record["amount"]):
            max_record = r

    # 输出结果
    print("\n====== 📊 数据分析报告 ======")
    print(f"总记录数：{len(records)} 条")
    print(f"总支出：{total:.2f} 元")
    print(f"平均每笔：{avg:.2f} 元")
    print(f"最大开销：{max_record['note']} - {max_record['amount']} 元")
    print("==============================\n")

# 3. 主程序
def main():
    records = load_data()
    print("✅ 数据加载成功！")
    analyze_data(records)

if __name__ == "__main__":
    main()