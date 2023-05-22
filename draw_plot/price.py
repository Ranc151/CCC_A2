import couchdb
import matplotlib.pyplot as plt
import numpy as np

# Login authentication
admin = 'admin'
password = 'Sjx991225'
url = f'http://{admin}:{password}@172.26.130.209:5984/'
server = couchdb.Server(url)
# get couchdb instance

sydney_price = server['sydney_price']
melbourne_price = server['melbourne_price']
bri_price = server['bri_price']
adelaide_price = server['adelaide_price']
perth_price = server['perth_price']
townsville_price = server['townsville_price']
riverina_price = server['riverina_price']
ballarat_price = server['ballarat_price']
central_coast_price = server['central_coast_price']
hobart_price = server['hobart_price']
city_g = [sydney_price, melbourne_price, bri_price, adelaide_price, perth_price]
city_s = [townsville_price,
          ballarat_price,
          central_coast_price,
          hobart_price,
          riverina_price]

great_city = []
small_city = []
name1 = []
name2 = []


for i in city_g:
    for row in i.view('Users/total', group_level="1"):
        great_city.append(row.value)
        name1.append(row.key)


for i in city_s:

    for row in i.view('Users/total', group_level="1"):
        small_city.append(row.value)
        name2.append(row.key)

plt.figure(figsize=(10, 6))
plt.subplot(211)

x = np.arange(len(great_city))

total_width, n = 0.8, 2
# 每种类型的柱状图宽度
width = total_width / n

plt.bar(x+width, great_city, width=width, label='Great city', color="red")

plt.xticks(x + 0.4, name1)

plt.legend()

plt.subplot(212)
x = np.arange(len(great_city))

total_width, n = 0.8, 2
# 每种类型的柱状图宽度
width = total_width / n

plt.bar(x+width, small_city, width=width, label='small city')
plt.xticks(x + 0.4, name2)
plt.legend()
plt.suptitle('Price in Twitter')
plt.savefig('price.png')