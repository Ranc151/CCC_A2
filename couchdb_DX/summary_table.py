import pandas as pd

# 创建一个示例数据框
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)

# 将数据框转换为表格形式
table = df.to_string(index=False)

# 打印表格
print(table)
