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
        twitter_employed.append(row.value)

for twitter_db in twitter_umemployed_dbs:
    for row in twitter_db.view('A2/count', group_level="1"):
        twitter_unemployed.append(row.value)

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

# calculate rate
sudo_employ_rate = []
sudo_unemploy_rate = []
twitter_employ_rate = []
twitter_unemploy_rate = []
for i in range(len(greater_citys_employed)):
    sudo_total = greater_citys_employed[i]+greater_citys_unemployed[i]
    twitter_total = twitter_employed[i]+twitter_unemployed[i]
    sudo_employ_rate.append(greater_citys_employed[i]/sudo_total)
    twitter_employ_rate.append(twitter_employed[i]/twitter_total)
    sudo_unemploy_rate.append(greater_citys_unemployed[i] / sudo_total)
    twitter_unemploy_rate.append(twitter_unemployed[i] / twitter_total)


plt.figure(figsize=(10, 6))
plt.subplot(211)

x = np.arange(len(greater_citys))

plt.plot(x, sudo_employ_rate, label='SUDO-Employed Rate', linewidth=5)
plt.plot(x, twitter_employ_rate, label='Twitter-Employed Rate', linewidth=5)
plt.scatter(x, sudo_employ_rate, color='red', label='SUDO-Employed Points',s=75)
plt.scatter(x, twitter_employ_rate, color='blue', label='Twitter-Employed Points',s=75)
plt.xticks(x, greater_citys)
plt.legend()

plt.subplot(212)
x = np.arange(len(greater_citys))

plt.plot(x, sudo_unemploy_rate, label='SUDO-Unemployed Rate', linewidth=5)
plt.plot(x, twitter_unemploy_rate, label='Twitter-Unemployed Rate', linewidth=5)
plt.scatter(x, sudo_unemploy_rate, color='red', label='SUDO-Unemployed Points',s=75)
plt.scatter(x, twitter_unemploy_rate, color='blue', label='Twitter-Unemployed Points',s=75)
plt.xticks(x, greater_citys)

plt.legend()
plt.suptitle('SUDO VS Twitter')
plt.show()
