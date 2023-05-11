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

# get couchdb instance
couch = couchdb.Server(url)

# 打开json文件导入
db = couch['twitter']
mydocument = db.get('twitter')
mydata = json.loads(mydocument)
print(mydata)