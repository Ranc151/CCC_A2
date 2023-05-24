import couchdb
import matplotlib.pyplot as plt
import numpy as np

# Login authentication
admin = 'admin'
password = 'Sjx991225'
url = f'http://{admin}:{password}@172.26.130.209:5984/'
server = couchdb.Server(url)
# get couchdb instance
mastodon = server['mastodon']

city = []
city2 = []
city_em = []
city_unem = []
a = []
for row in mastodon.view('Users/mel_em', group_level="1"):
    a.append(row.value)
city.append(a)
a = []
for row in mastodon.view('Users/mel_unem', group_level="1"):
    a.append(row.value)
city2.append(a)
a = []
for row in mastodon.view('Users/syn_em', group_level="1"):
    a.append(row.value)
a = [a[1], a[0]]
city.append(a)
a = []
for row in mastodon.view('Users/syn_unem', group_level="1"):
    a.append(row.value)
city2.append(a)
a = []
for row in mastodon.view('Users/Ade_em', group_level="1"):
    a.append(row.value)
city.append(a)
a = []
for row in mastodon.view('Users/Ade_umem', group_level="1"):
    a.append(row.value)
city2.append(a)
a = []
for row in mastodon.view('Users/bri_em', group_level="1"):
    a.append(row.value)
city.append(a)
a = []
for row in mastodon.view('Users/bri_unem', group_level="1"):
    a.append(row.value)
city2.append(a)
a = []
for row in mastodon.view('Users/Central Coast_em', group_level="1"):
    a.append(row.value)
city.append(a)
a = []
for row in mastodon.view('Users/Central Coast_unem', group_level="1"):
    a.append(row.value)
city2.append(a)
a = []
for row in mastodon.view('Users/sunshine coast_em', group_level="1"):
    a.append(row.value)
city.append(a)
a = []
for row in mastodon.view('Users/sunshine coast_unem', group_level="1"):
    a.append(row.value)
city2.append(a)


for i in city:
    city_em.append(i[1] / i[0] * 100)


for i in city:
    city_unem.append((i[0]-i[1]) / i[0] * 100)


x = np.arange(len(city_em))

total_width, n = 0.8, 2
# 每种类型的柱状图宽度
width = total_width / n

# 重新设置x轴的坐标
x = x - (total_width - width) / 2

plt.bar(x, city_em, width=width, label='Employed Full-Time')
plt.bar(x+width, city_unem, width=width, label='Unemployed Total')

xlable = ["Melbourne", "Sydney", "Adelaide", "Brisbane", "Central Coast", "Sunshine Coast"]
plt.xticks(x, xlable)


plt.xticks(fontsize=7)
plt.legend()
plt.savefig('mastodon_em.png')

w = []
work = []
unwork = []
a = []
for row in mastodon.view('A2/Melbourne', group_level="1"):
    a.append(row.value)
w.append(a)
a = []
for row in mastodon.view('A2/Sydney', group_level="1"):
    a.append(row.value)
w.append(a)
a = [0]
for row in mastodon.view('A2/Adelaide', group_level="1"):
    a.append(row.value)
w.append(a)
a = []
for row in mastodon.view('A2/Brisbane', group_level="1"):
    a.append(row.value)
w.append(a)
a = [0]
for row in mastodon.view('A2/Central Coast', group_level="1"):
    a.append(row.value)
w.append(a)


for i in w:
    result = i[0] + i[1]
    work.append(i[0] / result * 100)
for i in w:
    result = i[0] + i[1]
    unwork.append(i[1] / result * 100)

x = np.arange(len(work))

total_width, n = 0.8, 2
# 每种类型的柱状图宽度
width = total_width / n

# 重新设置x轴的坐标
x = x - (total_width - width) / 2

plt.bar(x, work, width=width, label='work_time')
plt.bar(x+width, unwork, width=width, label='Unwork_time')

xlable = ["Melbourne", "Sydney", "Adelaide", "Brisbane", "Central Coast"]
plt.xticks(x, xlable)


plt.xticks(fontsize=7)
plt.legend()
plt.savefig('mastodon_work.png')