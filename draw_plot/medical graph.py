import couchdb
import matplotlib.pyplot as plt
import numpy as np

# Login authentication
admin = 'admin'
password = 'Sjx991225'
url = f'http://{admin}:{password}@172.26.130.209:5984/'
server = couchdb.Server(url)
# get couchdb instance
adelaide_medical = server['adelaide_medical']
ballarat_medical = server['ballarat_medical']
bri_medical = server['bri_medical']
central_coast_medical = server['central_coast_medical']
hobart_medical = server['hobart_medical']
mel_medical = server['mel_medical']
perth_medical = server['perth_medical']
riverina_medical = server['riverina_medical']
syn_medical = server['syn_medical']
townsville_medical = server['townsville_medical']

medical_dbs = [adelaide_medical,
               mel_medical,
               perth_medical,
               syn_medical,
               bri_medical,
               ballarat_medical,
               central_coast_medical,
               hobart_medical,
               riverina_medical,
               townsville_medical]

greater_citys = ['adelaide', 'mel', 'perth', 'syn', 'bri', 'ballarat', 'central', 'hobart', 'riverina', 'townsville']
medical_datas = []

for twitter_db in medical_dbs:
    for row in twitter_db.view('A2/count', group_level="1"):
        medical_datas.append(row.value)



plt.figure(figsize=(10, 6))
x = np.arange(len(greater_citys))

plt.bar(x, medical_datas)
plt.xticks(x, greater_citys)

plt.suptitle('Medical Analyse')
plt.savefig('medical.png')