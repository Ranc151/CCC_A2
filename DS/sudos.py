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
db = server['sudo(s)']

# 读取视图
view = db.view('_all_docs', include_docs=True)

labour_21_em = {}
labour_21_unem = {}

# 遍历视图结果
for row in view:
    doc = row.doc
    for i in doc:
        if i == "Labour_2021":
            content = doc[i]
            for j in content:
                if j['sa4_name_2016'] not in labour_21_em:
                    if j['lbr_frc_stat'] == 'Employed Full-Time':
                        labour_21_em[j['sa4_name_2016']] = j['p']
                if j['sa4_name_2016'] not in labour_21_unem:
                    if j['lbr_frc_stat'] == 'Unemployed Total':
                        labour_21_unem[j['sa4_name_2016']] = j['p']

print(labour_21_unem)
print(labour_21_em)


def generate_random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return r, g, b


for k in [labour_21_em, labour_21_unem]:
    key = []
    items = []
    for i in k:
        split_result = i.split(" ")
        if len(split_result) > 1:
            key.append(split_result[1])
        else:
            key.append(i)
    for i in k:
        items.append(k[i])

    fig, ax = plt.subplots()
    color = generate_random_color()
    ax.bar(key, items, color=color)

    plt.show()
