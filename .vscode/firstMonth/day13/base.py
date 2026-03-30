import pandas as pd
data = {
    "姓名": ["张三", "李四", "王五"],
    "年龄": [20, 21, 22],
    "成绩": [90, 85, 88]
}

df = pd.DataFrame(data)
print(df)