import couchdb
import json
import time
import os.path
import math

import numpy as np
import pandas
import matplotlib.pyplot as plt

# Login authentication
admin = 'admin'
password = 'Sjx991225'
url = f'http://{admin}:{password}@172.26.130.209:5984/'
server = couchdb.Server(url)
# get couchdb instance
sudo_db = server['sudo(g)']
twitter_db = server['mastodon']

greater_citys = []
greater_citys_employed = []
greater_citys_unemployed = []
fid_set = set()

# 获取数据库中的所有文档
docs = [row.doc for row in sudo_db.view('_all_docs', include_docs=True)]
for doc in docs:
    if 'Labour_2020' in doc.keys():
        print(doc)
        for dict in doc['Labour_2020']:
            if dict['lbr_frc_stat'] == 'Unemployed Total':
                greater_citys.append(dict['gccsa_name_2016'])
                greater_citys_unemployed.append(int(dict['p']))
            elif dict['lbr_frc_stat'] == 'Employed Full-Time':
                fid = dict['fid']
                if fid not in fid_set:
                    greater_citys_employed.append(int(dict['p']))
                    fid_set.add(fid)


x = np.arange(len(greater_citys))

total_width, n = 0.8, 2
# 每种类型的柱状图宽度
width = total_width / n

# 重新设置x轴的坐标
x = x - (total_width - width) / 2

plt.bar(x, greater_citys_employed, width=width, label='Employed Full-Time')
plt.bar(x+width, greater_citys_unemployed, width=width, label='Unemployed Total')

plt.xticks(x, greater_citys)
plt.legend()
plt.show()

opts = {"group_level": "1"}
for row in twitter_db.view('A2/judge', group_level="1"):
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
