import csv
import json

csv_file = 'Labour_2020.csv'  # 输入的CSV文件路径
json_file = '../GCCSA_json/Labour_2020.json'  # 输出的JSON文件路径

data = []

# 读取CSV文件
with open(csv_file, 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        data.append(row)

# 写入JSON文件
with open(json_file, 'w') as file:
    json.dump(data, file, indent=4)

print('CSV file converted to JSON successfully.')
