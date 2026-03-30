import pandas as pd

# 1. 读取脏数据
df = pd.read_csv(".vscode\\day14\\dirty_data.csv", encoding="utf-8")
print("===== 原始数据 =====")
print(df)

# 2. 查看缺失值
print("\n===== 每列缺失值数量 =====")
print(df.isnull().sum())

# 3. 删除有空值的行
df_drop = df.dropna()
print("\n===== 删除空值后 =====")
print(df_drop)

# 4. 填充空值（成绩填60，年龄填20）
df_fill = df.copy()
df_fill["年龄"].fillna(20, inplace=True)
df_fill["成绩"].fillna(60, inplace=True)
print("\n===== 填充空值后 =====")
print(df_fill)

# 5. 去重
df_no_dup = df_fill.drop_duplicates()
print("\n===== 去重后最终干净数据 =====")
print(df_no_dup)