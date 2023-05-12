import couchdb
import json
import time
import os.path
import math
import pandas as pd

# Login authentication
admin = 'admin'
password = 'Sjx991225'
url = f'http://{admin}:{password}@172.26.130.209:5984/'
server=couchdb.Server(url)
# get couchdb instance
db = server['test']

data = {'time': []}
df = pd.DataFrame(data)
for doc in db.view('_all_docs',include_docs=True):
    time = doc.doc['key'][:3]
    df = df.append({'time': time}, ignore_index=True)
print(df)