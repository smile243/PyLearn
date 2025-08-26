import pandas as pd 
data = {
    '姓名': ['张三', '李四', '王五'],
    '年龄': [20, 21, 19],
    '成绩': [88, 92, 85]
}

df = pd.DataFrame(data)
# 写入 CSV
# df.to_csv('data_out.csv', index=False)
# 年龄 > 20 的行
print(df[df['年龄'] > 20])

# 成绩大于85且年龄小于21
print(df[(df['成绩'] > 85) & (df['年龄'] < 21)])