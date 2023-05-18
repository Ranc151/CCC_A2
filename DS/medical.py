import couchdb
import json
import math
import matplotlib.pyplot as plt
import random

import pandas as pd


# 定义生成随机颜色的函数
def generate_random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

# Login authentication
admin = 'admin'
password = 'Sjx991225'
url = f'http://{admin}:{password}@172.26.130.209:5984/'
server = couchdb.Server(url)

# get couchdb instance
db = server['medical']
view = db.view('_all_docs', include_docs=True)

dentists_rates_list=[]
phn_name_list = []
city_dentists_rate={}
for row in view:
    doc = row.doc
    for i in doc:
        if i == "features":
            content = doc[i]
            for j in content:
                dentists_rates_list.append(j['properties']['dentists_2018_rate_per_100000_people'])
                phn_name_list.append(j['properties']['phn_name'])

#创建一个dict，key是phn_name，value是dentists_rates_list
city_dentists_rate = dict(zip(phn_name_list,dentists_rates_list))

for i in range(len(phn_name_list)):
    plt.bar(phn_name_list[i],dentists_rates_list[i])
plt.title('city dentists rate per 100000 person')
plt.xlabel('city')
plt.ylabel('dentists rate %')
plt.xticks(rotation=90)
plt.show()





