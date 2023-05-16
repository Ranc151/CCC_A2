import couchdb
from collections import Counter

# Login authentication
admin = 'admin'
password = 'Sjx991225'
url = f'http://{admin}:{password}@172.26.130.209:5984/'
server = couchdb.Server(url)

# 获取 couchdb 实例中的数据库
db = server['sudo(g)']

# 获取所有文档
all_docs = db.view('_all_docs', include_docs=True)

# 存储 pop_distribution 值的列表
pop_distribution_list = []

# 遍历每个文档
for row in all_docs:
    doc = row.doc
    if "Age-2020" in doc:
        age_data = doc["Age-2020"]
        for item in age_data:
            if "pop_distribution" in item:
                pop_distribution = item["pop_distribution"]
                pop_distribution_list.append(pop_distribution)

# 统计不同值的出现次数
pop_distribution_counts = Counter(pop_distribution_list)


gccsa_name_2016_list = []
# 将结果存储在列表中
result_list = []
for value, count in pop_distribution_counts.items():
    result_list.append({'pop_distribution': value, 'count': count})

# 输出结果列表
print(result_list)

for row in all_docs:
    doc = row.doc
    if "Age-2020" in doc:
        age_data = doc["Age-2020"]
        for item in age_data:
            if "gccsa_name_2016" in item:
                gccsa_name_2016 = item["gccsa_name_2016"]
                gccsa_name_2016_list.append(gccsa_name_2016)

# 统计不同值的出现次数
pop_distribution_counts = Counter(gccsa_name_2016_list)

# 将结果存储在列表中
gccsa_name_2016_list = []
for value, count in pop_distribution_counts.items():
    gccsa_name_2016_list.append({'gccsa_name_2016': value, 'count': count})

# 输出结果列表
print(gccsa_name_2016_list)

pop_counter = Counter()
for doc_id in db:
    doc = db[doc_id]
    if 'pop' in doc:
        pop_counter.update({doc['pop']})

# 输出统计结果
print(pop_counter)