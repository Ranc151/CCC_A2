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

# Create two empty lists and an empty dictionary dentists_rates_list=[]: used to store dental rate data.
# phn_name_list = []: Name of the storage area. city_dentists_rate={}: Used to store city dentists_rate data.
dentists_rates_list = []
phn_name_list = []
city_dentists_rate = {}

# The purpose of this code is to extract the values of specific properties from the database view and store
# them in the dentists_rates_list and phn_name_list lists, respectively. These attribute values are
# extracted from the elements in the "features" attribute in each document, which contain data about
# dental rates and region names.
for row in view:
    doc = row.doc
    for i in doc:
        if i == "features":
            content = doc[i]
            for j in content:
                dentists_rates_list.append(j['properties']['dentists_2018_rate_per_100000_people'])
                phn_name_list.append(j['properties']['phn_name'])

# First, the region name and dentists_rate data are stored in the city_dentists_rate dictionary.
# Then, the phn_name_list and dentists_rates_list lists were iterated, and a bar graph was plotted each time.
# The axis and ordinates were the dentists_rates_list. Thus, dental rates in each region can be visualized
# in the form of a bar chart.
city_dentists_rate = dict(zip(phn_name_list, dentists_rates_list))
fig, ax = plt.subplots()
data = []
data2 = []
data3 = []
data4 = []
for k in range(len(phn_name_list)):
    if "Melbourne" in phn_name_list[k] or  "Sydney" in phn_name_list[k] or "Brisbane" in phn_name_list[k] or "Adelaide" in phn_name_list[k] or "Perth" in phn_name_list[k]:
        data.append(phn_name_list[k])
        data2.append(dentists_rates_list[k])
    else:
        data3.append(phn_name_list[k])
        data4.append(dentists_rates_list[k])

data = data + data3
data2 = data2 + data4
color = "blue"
for i in range(len(data)):
    if i == 24:
        color = "red"
    plt.bar(data[i], data2[i], color=color)
    ax.axhline(data2[i], color='white', linestyle='--', linewidth=0.3)

ax.set_facecolor('lightcyan')


plt.title('city dentists rate per 100000 person')
plt.xlabel('city')
plt.ylabel('dentists rate %')
# Rotate the scale label on the x-axis to vertical.
plt.xticks(rotation=80)
# Set x font size
plt.xticks(fontsize=4)

plt.savefig('sudo_medical.png')
