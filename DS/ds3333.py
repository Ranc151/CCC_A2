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
sudo_db = server['sudo(g)']
twitter_db = server['twitter_dataset']

# 获取数据库中的所有文档
docs = [row.doc for row in sudo_db.view('_all_docs', include_docs=True)]
for doc in docs:
   if 'Labour_2020' in doc.keys():
       for dict in doc['Labour_2020']:
           if dict['lbr_frc_stat'] == 'Unemployed Total':
               print(dict['gccsa_name_2016'])
               print(dict['p'])

map_fun ='''function(doc){
var bool = false;
for(obj in doc.data.entities.urls){
    if(obj.description.includes("Return")){
        bool = true;
        break;
    }
}
if(bool){
    emit("Return", doc);
}

}'''

for row in twitter_db.query(map_fun, reduce_fun=None, language='javascript', wrapper=None):
    print(row)
# merged_data = []
# for doc in docs:
#     merged_data.append(doc)
#
# # 将合并后的 JSON 对象写入文件
# with open('merged_docs.json', 'w') as f:
#     json.dump(merged_data, f, indent=4)
#
# # 读取合并后的 JSON 对象并打印
# with open('merged_docs.json', 'r') as f:
#     merged_data = json.load(f)
#
# print(json.dumps(merged_data, indent=4))

# dict1 = {}
# dict1_list = ['Sydney', 'Melbourne', 'Brisbane', 'Perth', 'Adelaide', 'Hobart', 'Darwin', 'Canberra', 'Australian', 'Australia']
# for keyword_area in merged_data.keys():
#     dict1_list[keyword_area] = merged_data.get(keyword_area).get("city").lower().replace(" ", "")
#
# for sub in list(dict1.keys()):
#     if dict1.get(sub) not in dict1_list:
#         del dict1[sub]
