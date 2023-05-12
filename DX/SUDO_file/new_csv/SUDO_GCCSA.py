import os
import json
import couchdb

admin = 'admin'
password = 'Sjx991225'
url = f'http://{admin}:{password}@172.26.130.209:5984/'

# get couchdb instance
couch = couchdb.Server(url)

# set the db name
db_name = 'sudo(g)'

# Whether the database exists
if db_name in couch:
    db = couch[db_name]
else:
    db = couch.create(db_name)

# JSON文件所在的目录路径
json_dir = 'GCCSA_json'

# 读取并插入每个JSON文件的数据到数据库
for filename in os.listdir(json_dir):

    if filename.endswith('.json'):
        file_path = os.path.join(json_dir, filename)

        with open(file_path, 'r') as file:
            json_data = json.load(file)
            result = ','.join(str(x) for x in json_data[0:3])
            # 将JSON数据插入数据库
            doc_id, doc_rev = db.save(result)
            print(f'Inserted document with ID: {doc_id} and revision: {doc_rev}')

print('All JSON files inserted into the database.')
