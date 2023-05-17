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
db = server['sudo(s)']

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

