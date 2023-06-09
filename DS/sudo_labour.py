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

## GCCSA
# get couchdb instance
db = server['sudo(g)']

# Read view
view = db.view('_all_docs', include_docs=True)
labour_21_em = {}
labour_21_unem = {}
# # Iterate over the view result
for row in view:
    doc = row.doc
    for i in doc:
        if i == "Labour_2020":
            content = doc[i]
            for j in content:
                if j['gccsa_name_2016'] not in labour_21_em:
                    if j['lbr_frc_stat'] == 'Employed Full-Time':
                        labour_21_em[j['gccsa_name_2016']] = j['p']
                if j['gccsa_name_2016'] not in labour_21_unem:
                    if j['lbr_frc_stat'] == 'Unemployed Total':
                        labour_21_unem[j['gccsa_name_2016']] = j['p']
# print(labour_21_unem)
# print(labour_21_em)


def generate_random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return r, g, b


sum_g = [0, 0]
sum_s = [0, 0]
employer = ["Employed Full-Time", "Unemployed Total"]
k = [labour_21_em, labour_21_unem]
for p in range(2):
    key = []
    items = []
    for i in k[p]:
        key.append(i.split(" ")[1])
    for i in k[p]:
        items.append(int(k[p][i]))
        sum_g[p] = sum_g[p] + int(k[p][i])
    fig, ax = plt.subplots()
    color = generate_random_color()
    ax.bar(key, items, color=color, width=0.6)
    ax.set(xlabel="Great city", ylabel="Population", title=employer[p] + " Grand capital")
    plt.xticks(rotation=35)
    for o in range(len(key)):
        plt.text(key[o], items[o], str(items[o]), ha='center', va='bottom')
    fig.subplots_adjust(left=0.2, bottom=0.2, right=0.9, top=0.9)
    ax.set_facecolor('lightcyan')
    for i, val in enumerate(items):
        ax.axhline(val, color='white', linestyle='--', linewidth=0.7)

    if p == 0:
        plt.savefig('sudo_Labourem_g20.png')
    else:
        plt.savefig('sudo_Labourunem_g20.png')

## SA4
# get couchdb instance
db2 = server['sudo(s)']

# Read view
view2 = db2.view('_all_docs', include_docs=True)

labour_21_ems = {}
labour_21_unems = {}
# Iterate over the view result
for row in view2:
    doc = row.doc
    for i in doc:
        if i == "Labour_2020":
            content = doc[i]
            for j in content:
                if j['sa4_name_2016'] not in labour_21_ems:
                    if j['lbr_frc_stat'] == 'Employed Full-Time':
                        labour_21_ems[j['sa4_name_2016']] = j['p']
                if j['sa4_name_2016'] not in labour_21_unems:
                    if j['lbr_frc_stat'] == 'Unemployed Total':
                        labour_21_unems[j['sa4_name_2016']] = j['p']
# print(labour_21_unems)
# print(labour_21_ems)

k = [labour_21_ems, labour_21_unems]
for p in range(2):
    key = []
    items = []
    for i in k[p]:
        key.append(i)
        # key.append(i.split(" ")[-1])
    print(key)
    for i in k[p]:
        items.append(int(k[p][i]))
    for w in range(7):
        sum_s[p] = sum_s[p] + int(items[w])

    fig, ax = plt.subplots()
    color = generate_random_color()
    ax.bar(key[0:5], items[0:5], color=color, width=0.6)
    plt.xticks(rotation=35)
    ax.set(xlabel="Great city", ylabel="Population", title=employer[p] + " Small city", )
    for o in range(len(key[0:5])):
        plt.text(key[o], items[o], str(items[o]), ha='center', va='bottom')
    fig.subplots_adjust(left=0.2, bottom=0.2, right=0.9, top=0.9)
    ax.set_facecolor('lightcyan')
    for i, val in enumerate(items[0:5]):
        ax.axhline(val, color='white', linestyle='--', linewidth=0.7)
    if p == 0:
        plt.savefig('sudo_Labourem_s20.png')
    else:
        plt.savefig('sudo_Labourunem_s20.png')



# print(sum_g, sum_s)
data = ["Employer in Great City", "Unemployer in Great City", "Employer in Small City", "Unemployer in Small City"]
values = [sum_g[0], sum_g[1], sum_s[0], sum_s[1]]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
# pie chart

fig, ax = plt.subplots()
wedges, texts, autotexts = ax.pie(values, labels=data, colors=colors, autopct='%1.1f%%')
ax.axis('equal')
# title
plt.title('Pie Chart')

for w in wedges:
    w.set_linewidth(2)
    w.set_edgecolor('white')

for t in autotexts:
    t.set_color('black')

ax.legend(loc="best")

# display plot
plt.savefig('sudo_Labour_pie20.png')


