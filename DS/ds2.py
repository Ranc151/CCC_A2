import couchdb
import json
import time
import os.path
import math
import pandas

# Login authentication
admin = 'admin'
password = 'Sjx991225'
url = f'http://{admin}:{password}@172.26.130.209:5984/'
server=couchdb.Server(url)
# get couchdb instance
db = server['twitter']

# 获取数据库中的所有文档
docs = [row.doc for row in db.view('_all_docs', include_docs=True)]

merged_data = []
for doc in docs:
    merged_data.append(doc)

# 将合并后的 JSON 对象写入文件
with open('merged_docs.json', 'w') as f:
    json.dump(merged_data, f, indent=4)

# 读取合并后的 JSON 对象并打印
with open('merged_docs.json', 'r') as f:
    merged_data = json.load(f)

print(json.dumps(merged_data, indent=4))

dict1 = {}
dict1_list = ['Sydney', 'Melbourne', 'Brisbane', 'Perth', 'Adelaide', 'Hobart', 'Darwin', 'Canberra', 'Australian', 'Australia']
for keyword_area in merged_data.keys():
    dict1_list[keyword_area] = merged_data.get(keyword_area).get("city").lower().replace(" ", "")

for sub in list(dict1.keys()):
    if dict1.get(sub) not in dict1_list:
        del dict1[sub]