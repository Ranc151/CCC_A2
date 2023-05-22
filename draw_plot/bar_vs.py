import couchdb
import matplotlib.pyplot as plt
import numpy as np

# Login authentication
admin = 'admin'
password = 'Sjx991225'
url = f'http://{admin}:{password}@172.26.130.209:5984/'
server = couchdb.Server(url)
# get couchdb instance
sudo_db = server['sudo(g)']
sydney_twitter_employed = server['syd_em']
sydney_twitter_unemployed = server['syd_unem']
melbourne_twitter_employed = server['mel_em']
melbourne_twitter_unemployed = server['mel_unem']
brisbane_twitter_employed = server['bri_em']
brisbane_twitter_unemployed = server['bri_unem']
adelaide_twitter_employed = server['ade_em']
adelaide_twitter_unemployed = server['ade_unem']
perth_twitter_employed = server['per_em']
perth_twitter_unemployed = server['per_unem']
twitter_employed_dbs = [sydney_twitter_employed,
                        melbourne_twitter_employed,
                        brisbane_twitter_employed,
                        adelaide_twitter_employed,
                        perth_twitter_employed]
twitter_umemployed_dbs = [sydney_twitter_unemployed,
                          melbourne_twitter_unemployed,
                          brisbane_twitter_unemployed,
                          adelaide_twitter_unemployed,
                          perth_twitter_unemployed]

greater_citys = []
greater_citys_employed = []
greater_citys_unemployed = []
fid_set = set()
twitter_employed = []
twitter_unemployed = []

for twitter_db in twitter_employed_dbs:
    for row in twitter_db.view('A2/count', group_level="1"):
        twitter_employed.append(row.value*100)

for twitter_db in twitter_umemployed_dbs:
    for row in twitter_db.view('A2/count', group_level="1"):
        twitter_unemployed.append(row.value*100)

# 获取数据库中的所有文档
docs = [row.doc for row in sudo_db.view('_all_docs', include_docs=True)]
for doc in docs:
    if 'Labour_2021' in doc.keys():
        for dict in doc['Labour_2021']:
            if dict['lbr_frc_stat'] == 'Unemployed Total':
                greater_citys.append(dict['gccsa_name_2016'])
                greater_citys_unemployed.append(int(dict['p']))
            elif dict['lbr_frc_stat'] == 'Employed Full-Time':
                fid = dict['fid']
                if fid not in fid_set:
                    greater_citys_employed.append(int(dict['p']))
                    fid_set.add(fid)

plt.figure(figsize=(10, 6))
plt.subplot(211)

x = np.arange(len(greater_citys))

total_width, n = 0.8, 2
# 每种类型的柱状图宽度
width = total_width / n

# 重新设置x轴的坐标
x = x - (total_width - width) / 2

plt.bar(x, greater_citys_employed, width=width, label='SUDO-Employed')
plt.bar(x+width, twitter_employed, width=width, label='Twitter-Employed * 100')
plt.xticks(x, greater_citys)
plt.legend()

plt.subplot(212)
x = np.arange(len(greater_citys))

total_width, n = 0.8, 2
# 每种类型的柱状图宽度
width = total_width / n

# 重新设置x轴的坐标
x = x - (total_width - width) / 2

plt.bar(x, greater_citys_unemployed, width=width, label='SUDO-Unemployed')
plt.bar(x+width, twitter_unemployed, width=width, label='Twitter-Unemployed * 100')
plt.xticks(x, greater_citys)

plt.legend()
plt.suptitle('SUDO VS Twitter')
plt.savefig('sVt_bar.png')


