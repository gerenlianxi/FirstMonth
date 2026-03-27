import pandas as pd
df = pd.read_excel(".vscode\\day13\\data.xlsx", engine="openpyxl")
print("===== 1. 前5行 =====")
print(df.head())
