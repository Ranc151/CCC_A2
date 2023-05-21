import couchdb
import json

# 登录认证
admin = 'admin'
password = 'Sjx991225'
url = f'http://{admin}:{password}@172.26.130.209:5984/'
server = couchdb.Server(url)

# 获取 CouchDB 实例
db = server['final_gcc']

# 从数据库中读取文档
docs = db.view('_all_docs', include_docs=True)

# 合并所有文档的内容
merged_data = []
for row in docs:
    doc = row['doc']
    merged_data.append(doc)

# 输出合并后的内容
for data in merged_data:
    print(json.dumps(data, indent=4, ensure_ascii=False))
