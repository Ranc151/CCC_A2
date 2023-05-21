import pandas as pd
import couchdb
import json
import math
import matplotlib.pyplot as plt
import random
import numpy as np

# Login authentications
admin = 'admin'
password = 'Sjx991225'
url = f'http://{admin}:{password}@172.26.130.209:5984/'
server = couchdb.Server(url)

## GCCSA
# get couchdb instance
key = ['sa4_name_2016', 'working_age_pop_15_64', 'mpy_rt_15_64', 'unemp_rt_15']
title = ["city_name", "working_age_pop_15_64", 'mpy_rt_15_64', 'unemp_rt_15']
data = [title]
db = server['sudo(s)']
view = db.view('_all_docs', include_docs=True)

for row in view:
    doc = row.doc
    for i in doc:
        if i == 'summary_2021':
            content = doc[i]
            for j in content:
                new_con = j['properties']
                a_list = [new_con[key[0]], new_con[key[1]], new_con[key[2]], new_con[key[3]]]
                data.append(a_list)


# Create charts and subgraphs
fig, ax = plt.subplots()

# Hide the axes
ax.axis('off')

# Create table
table = ax.table(cellText=data[0:6], loc='center', cellLoc='center')

# Set the table style
table.set_fontsize(14)
table.scale(1.2, 1.2)  # Resize the table

# Save as picture
plt.savefig('summary_2021s.png', bbox_inches='tight', pad_inches=0.2)

title2 = ["city_name", "working_age_pop_15_64", 'mpy_rt_15_64', 'unemp_rt_15']
data2 = [title2]
for row in view:
    doc = row.doc
    for i in doc:
        if i == 'summary_2020':
            content = doc[i]
            for j in content:
                new_con = j['properties']
                a_list = [new_con[key[0]], new_con[key[1]], new_con[key[2]], new_con[key[3]]]
                data2.append(a_list)


# Create charts and subgraphs
fig, ax = plt.subplots()

# Hide the axes
ax.axis('off')

# Create table
table = ax.table(cellText=data2[0:6], loc='center', cellLoc='center')

# Set the table style
table.set_fontsize(14)
table.scale(1.2, 1.2)  # Resize the table

# Save as picture
plt.savefig('summary_2020s.png', bbox_inches='tight', pad_inches=0.2)

