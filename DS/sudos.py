import couchdb
import json
import math
import matplotlib.pyplot as plt
import random

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
                sa4_name = j['sa4_name_2016']
                if 'Melbourne' in sa4_name:
                    if j['lbr_frc_stat'] == 'Employed Full-Time':
                        labour_21_em[sa4_name] = j['p']
                    if j['lbr_frc_stat'] == 'Unemployed Total':
                        labour_21_unem[sa4_name] = j['p']

print(labour_21_unem)
print(labour_21_em)

# 提取键和值，并进行排序
key1 = sorted(labour_21_unem.keys())
value1 = [labour_21_unem[key] for key in key1]

# 生成随机颜色1
color1 = generate_random_color()

# 创建柱状图'Unemployed Total'
plt.bar(key1, value1, color=color1)
plt.xlabel('SA4 Name')
plt.ylabel('Unemployed Total')
plt.title('Unemployed Total in Melbourne SA4 Areas')

# 设置 y 轴范围从 0 开始
plt.ylim(bottom=0)

plt.xticks(rotation=90)  # 旋转 x 轴标签
plt.tight_layout()  # 调整布局

plt.show()

# 提取键和值，并进行排序
key2 = sorted(labour_21_em.keys())
value2 = [labour_21_em[key] for key in key2]

# 生成随机颜色2
color2 = generate_random_color()

# 创建柱状图'Employed Total'
plt.bar(key2, value2, color=color2)
plt.xlabel('SA4 Name')
plt.ylabel('Employed Total')
plt.title('Employed Total in Melbourne SA4 Areas')

# 设置 y 轴范围从 0 开始
plt.ylim(bottom=0)

plt.xticks(rotation=90)  # 旋转 x 轴标签
plt.tight_layout()  # 调整布局

plt.show()
