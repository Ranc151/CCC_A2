import couchdb
import json
import math
import matplotlib.pyplot as plt
import random

# Login authentication
admin = 'admin'
password = 'Sjx991225'
url = f'http://{admin}:{password}@172.26.130.209:5984/'
server = couchdb.Server(url)

# get couchdb instance
db = server['medical']

# 读取视图
view = db.view('_all_docs', include_docs=True)

features_data = {}

# 遍历视图结果
for row in view:
    doc = row.doc
    for i in doc:
        if i == "features":
            content = doc[i]
            for j in content:
                if j['dentists_2018_rate_per_100000_people'] not in features_data:
                    if j["properties"] not in
                        features_data[j["dentists_2018_rate_per_100000_people"]] = j['p']


print(features_data)


def generate_random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return r, g, b


# for k in [labour_21_em, labour_21_unem]:
#     key = []
#     items = []
#     for i in k:
#         key.append(i.split(" ")[1])
#     for i in k:
#         items.append(k[i])
#
#     fig, ax = plt.subplots()
#     color = generate_random_color()
#     ax.bar(key, items, color=color)
#
#     plt.show()
