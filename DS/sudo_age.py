import couchdb
import json
import math
import matplotlib.pyplot as plt
import random
import numpy as np

# Login authentication
admin = 'admin'
password = 'Sjx991225'
url = f'http://{admin}:{password}@172.26.130.209:5984/'
server = couchdb.Server(url)

## GCCSA
# get couchdb instance
db = server['sudo(g)']

sudo_age = {}
# Read view
view = db.view('_all_docs', include_docs=True)
for row in view:
    doc = row.doc
    for i in doc:
        if i == "Age_2021":
            content = doc[i]
            for j in content:
                if j['gccsa_name_2016'] not in sudo_age:
                    sudo_age[j['gccsa_name_2016']] = []
                sudo_age[j['gccsa_name_2016']].append(j['pop'])
print(sudo_age)

key = []
for i in sudo_age:
    key.append(i)

# Sets the width of the bar chart
bar_width = 0.5

# Set the scale position on the x axis
x = np.arange(len(key))


def generate_random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return r, g, b


g15_to_24 = []
g25_to_34 = []
g35_to_44 = []
g45_to_54 = []
g55_to_64 = []
g65_and_over = []


for j in key:
    g15_to_24.append(int(sudo_age[j][0]))
    g25_to_34.append(int(sudo_age[j][1]))
    g35_to_44.append(int(sudo_age[j][2]))
    g45_to_54.append(int(sudo_age[j][3]))
    g55_to_64.append(int(sudo_age[j][4]))
    g65_and_over.append(int(sudo_age[j][5]))

color = generate_random_color()
plt.bar(x, g15_to_24, width=bar_width, label='g15_to_24', color=color)
color = generate_random_color()
plt.bar(x, g25_to_34, width=bar_width, label='g25_to_34', bottom=g15_to_24, color=color)
color = generate_random_color()
plt.bar(x, g35_to_44, width=bar_width, label='g35_to_44', bottom=np.array(g15_to_24) + np.array(g25_to_34), color=color)
color = generate_random_color()
plt.bar(x, g45_to_54, width=bar_width, label='g45_to_54',
        bottom=np.array(g15_to_24) + np.array(g25_to_34) + np.array(g35_to_44), color=color)
color = generate_random_color()
plt.bar(x, g55_to_64, width=bar_width, label='g55_to_64',
        bottom=np.array(g15_to_24) + np.array(g25_to_34) + np.array(g35_to_44) + np.array(g45_to_54), color=color)
color = generate_random_color()
plt.bar(x, g65_and_over, width=bar_width, label='g65_and_over',
        bottom=np.array(g15_to_24) + np.array(g25_to_34) + np.array(g35_to_44) + np.array(g45_to_54) + np.array(
            g55_to_64), color=color)

# Set the scale position on the x axis
plt.xticks(rotation=45)
plt.xticks(x, key)

# Add icon
plt.legend()

# display icon
plt.show()


##SA4
db2 = server['sudo(s)']

sudo_age2 = {}
# Read view
view2 = db2.view('_all_docs', include_docs=True)
for row in view2:
    doc = row.doc
    for i in doc:
        if i == "Age_2021":
            content = doc[i]
            for j in content:
                if j['sa4_name_2016'] not in sudo_age2:
                    sudo_age2[j['sa4_name_2016']] = []
                sudo_age2[j['sa4_name_2016']].append(j['pop'])
print(sudo_age2)

key2 = []
for i in sudo_age2:
    key2.append(i)

# Sets the width of the bar chart
bar_width = 0.5

# Set the scale position on the x axis
x = np.arange(len(key2[0:5]))


def generate_random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return r, g, b


g15_to_24 = []
g25_to_34 = []
g35_to_44 = []
g45_to_54 = []
g55_to_64 = []
g65_and_over = []


for j in key2[0:5]:
    g15_to_24.append(int(sudo_age2[j][0]))
    g25_to_34.append(int(sudo_age2[j][1]))
    g35_to_44.append(int(sudo_age2[j][2]))
    g45_to_54.append(int(sudo_age2[j][3]))
    g55_to_64.append(int(sudo_age2[j][4]))
    g65_and_over.append(int(sudo_age2[j][5]))

color = generate_random_color()
plt.bar(x, g15_to_24, width=bar_width, label='g15_to_24', color=color)
color = generate_random_color()
plt.bar(x, g25_to_34, width=bar_width, label='g25_to_34', bottom=g15_to_24, color=color)
color = generate_random_color()
plt.bar(x, g35_to_44, width=bar_width, label='g35_to_44', bottom=np.array(g15_to_24) + np.array(g25_to_34), color=color)
color = generate_random_color()
plt.bar(x, g45_to_54, width=bar_width, label='g45_to_54',
        bottom=np.array(g15_to_24) + np.array(g25_to_34) + np.array(g35_to_44), color=color)
color = generate_random_color()
plt.bar(x, g55_to_64, width=bar_width, label='g55_to_64',
        bottom=np.array(g15_to_24) + np.array(g25_to_34) + np.array(g35_to_44) + np.array(g45_to_54), color=color)
color = generate_random_color()
plt.bar(x, g65_and_over, width=bar_width, label='g65_and_over',
        bottom=np.array(g15_to_24) + np.array(g25_to_34) + np.array(g35_to_44) + np.array(g45_to_54) + np.array(
            g55_to_64), color=color)


# Set the scale position on the x axis
plt.xticks(rotation=45)
plt.xticks(x, key2[0:5])

# Add icon
plt.legend()

# display icon
plt.show()

