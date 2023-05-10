import couchdb
import json

# Login authentication
admin = 'admin'
password = 'Sjx991225'
url = f'http://{admin}:{password}@172.26.130.209:5984/'

# get couchdb instance
couch = couchdb.Server(url)

# set the db name
db_name = 'twitter'

# Whether the database exists
if db_name in couch:
    db = couch[db_name]
else:
    db = couch.create(db_name)

# start to store the data
with open('twitter-huge.json', 'r', encoding='utf-8') as file:
    line_count = sum(1 for line in file)
    text = ""
    new_line = file.readline()
    for i in range(1):
        new_line = file.readline()

        text = text + new_line

    t = json.loads(text[:-2])
    db.save(t)
    print(line_count)


