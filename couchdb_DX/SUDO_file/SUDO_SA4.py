import os
import json
import couchdb

admin = 'admin'
password = 'Sjx991225'
url = f'http://{admin}:{password}@172.26.130.209:5984/'

# get couchdb instance
couch = couchdb.Server(url)

# set the db name
db_name = 'sudo(s)'

# Whether the database exists
if db_name in couch:
    db = couch[db_name]
else:
    db = couch.create(db_name)

# JSON文件所在的目录路径
json_dir = 'new_csv/SA4_json'

# 读取并插入每个JSON文件的数据到数据库
for filename in os.listdir(json_dir):

    if filename.endswith('.json'):
        file_path = os.path.join(json_dir, filename)

        with open(file_path, 'r') as file:
            json_data = json.load(file)
            filename, doc_rev = db.save(json_data)
            print(f'Inserted document with ID: {filename} and revision: {doc_rev}')

print('All JSON files inserted into the database.')
