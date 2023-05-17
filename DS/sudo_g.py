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
        if i == "Labour_2021":
            content = doc[i]
            for j in content:
                if j['gccsa_name_2016'] not in labour_21_em:
                    if j['lbr_frc_stat'] == 'Employed Full-Time':
                        labour_21_em[j['gccsa_name_2016']] = j['p']
                if j['gccsa_name_2016'] not in labour_21_unem:
                    if j['lbr_frc_stat'] == 'Unemployed Total':
                        labour_21_unem[j['gccsa_name_2016']] = j['p']
print(labour_21_unem)
print(labour_21_em)


def generate_random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return r, g, b


employer = ["Employed Full-Time", "Unemployed Total"]
k = [labour_21_em, labour_21_unem]
for p in range(2):
    key = []
    items = []
    for i in k[p]:
        key.append(i.split(" ")[1])
    for i in k[p]:
        items.append(k[p][i])
    fig, ax = plt.subplots()
    color = generate_random_color()
    fig.patch.set_facecolor('lightgray')
    ax.bar(key, items, color=color)
    ax.set(xlabel="city", ylabel="Population", title=employer[p]+" Grand capital")
    plt.xticks(rotation=45)
    for o in range(len(key)):
        plt.text(key[o], items[o], str(items[o]), ha='center', va='bottom')

    plt.show()


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
        if i == "Labour_2021":
            content = doc[i]
            for j in content:
                if j['sa4_name_2016'] not in labour_21_ems:
                    if j['lbr_frc_stat'] == 'Employed Full-Time':
                        labour_21_ems[j['sa4_name_2016']] = j['p']
                if j['sa4_name_2016'] not in labour_21_unems:
                    if j['lbr_frc_stat'] == 'Unemployed Total':
                        labour_21_unems[j['sa4_name_2016']] = j['p']
print(labour_21_unems)
print(labour_21_ems)

k = [labour_21_ems, labour_21_unems]
for p in range(2):
    key = []
    items = []
    for i in k[p]:
        key.append(i.split(" ")[-1])
    for i in k[p]:
        items.append(k[p][i])
    fig, ax = plt.subplots()
    color = generate_random_color()
    fig.patch.set_facecolor('lightgray')
    ax.bar(key[0:10], items[0:10], color=color)
    plt.xticks(rotation=45)
    ax.set(xlabel="city", ylabel="Population", title=employer[p]+" Small city", )
    for o in range(len(key[0:10])):
        plt.text(key[o], items[o], str(items[o]), ha='center', va='bottom')

    plt.show()

sum1 = sum()


