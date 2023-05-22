import couchdb
import matplotlib.pyplot as plt
import numpy as np
import csv

# Login authentication
admin = 'admin'
password = 'Sjx991225'
url = f'http://{admin}:{password}@172.26.130.209:5984/'
server = couchdb.Server(url)
# get couchdb instance

title = ["City", "Number of Use"]
data = []

sydney1 = server['syd_em']
sydney2 = server['syd_unem']
sydney3 = server['syn_medical']
sydney4 = server['sydney_price']
sydney = [sydney1, sydney2, sydney3, sydney4]
total = 0
for i in sydney:
    for row in i.view('Users/total', group_level="1"):
        total += row.value
a_list = ["Sydney", total + 4]
data.append(a_list)


mel1 = server['mel_em']
mel2 = server['mel_unem']
mel3 = server['mel_medical']
mel4 = server['melbourne_price']
mel = [mel1, mel2, mel3, mel4]
total = 0
for i in mel:
    for row in i.view('Users/total', group_level="1"):
        total += row.value
a_list = ["Melbourne", total + 4]
data.append(a_list)

per1 = server['per_em']
per2 = server['per_unem']
per3 = server['perth_medical']
per4 = server['perth_price']
per = [per1, per2, per3, per4]
total = 0
for i in per:
    for row in i.view('Users/total', group_level="1"):
        total += row.value
a_list = ["Perth", total + 4]
data.append(a_list)

bri1 = server['bri_em']
bri2 = server['bri_unem']
bri3 = server['bri_medical']
bri4 = server['bri_price']
bri = [bri1, bri2, bri3, bri4]
total = 0
for i in bri:
    for row in i.view('Users/total', group_level="1"):
        total += row.value
a_list = ["Brisbane", total + 4]
data.append(a_list)


ade1 = server['ade_em']
ade2 = server['ade_unem']
ade3 = server['adelaide_medical']
ade4 = server['adelaide_price']
ade = [ade1, ade2, ade3, ade4]
total = 0
for i in ade:
    for row in i.view('Users/total', group_level="1"):
        total += row.value
a_list = ["Adelaide", total + 4]
data.append(a_list)

ball1 = server['ballarat_medical']
ball2 = server['ballarat_price']
ball = [ball1, ball2]
total = 0
for i in ball:
    for row in i.view('Users/total', group_level="1"):
        total += row.value
a_list = ["Ballarat", total]
data.append(a_list)

bun1 = server['bun_em']
bun2 = server['bun_unem']
bun = [bun1, bun2]
total = 0
for i in bun:
    for row in i.view('Users/total', group_level="1"):
        total += row.value
a_list = ["bunbury", total]
data.append(a_list)

num1 = server['cen_em']
num2 = server['cen_unem']
num = [num1, num2]
total = 0
for i in num:
    for row in i.view('Users/total', group_level="1"):
        total += row.value
a_list = ["Central Coast", total]
data.append(a_list)

num1 = server['dar_em']
num2 = server['dar_unem']
num = [num1, num2]
total = 0
for i in num:
    for row in i.view('Users/total', group_level="1"):
        total += row.value
a_list = ["Darwin", total]
data.append(a_list)

num1 = server['hob_em']
num2 = server['hob_unem']
num3 = server['hobart_medical']
num4 = server['hobart_price']
num = [num1, num2, num3, num4]
total = 0
for i in num:
    for row in i.view('Users/total', group_level="1"):
        total += row.value
a_list = ["Darwin", total]
data.append(a_list)

num1 = server['riv_em']
num2 = server['riv_unem']
num3 = server['riverina_medical']
num4 = server['riverina_price']
num = [num1, num2, num3, num4]
total = 0
for i in num:
    for row in i.view('Users/total', group_level="1"):
        total += row.value
a_list = ["Riverina", total]
data.append(a_list)

num1 = server['sun_em']
num2 = server['sun_unem']
num = [num1, num2]
total = 0
for i in num:
    for row in i.view('Users/total', group_level="1"):
        total += row.value
a_list = ["Sunshine Coast", total]
data.append(a_list)

num3 = server['townsville_medical']
num4 = server['townsville_price']
num = [num3, num4]
total = 0
for i in num:
    for row in i.view('Users/total', group_level="1"):
        total += row.value
a_list = ["Townsville", total]
data.append(a_list)

# Specifies the CSV file path to save
filename = 'data.csv'

# Create and write csv files using the CSV module
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f'CSV file "{filename}" has been created and data has been written.')
