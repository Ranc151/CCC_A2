import os
import json
import couchdb

admin = 'admin'
password = 'Sjx991225'
url = f'http://{admin}:{password}@172.26.130.209:5984/'

# get couchdb instance
couch = couchdb.Server(url)

# set the db name
db_name = 'medical'

# Whether the database exists
if db_name in couch:
    db = couch[db_name]
else:
    db = couch.create(db_name)

# Path to the directory where the JSON file is located
json_dir = 'new_csv/medical_science'

# Read and insert data from each JSON file into the database
for filename in os.listdir(json_dir):

    if filename.endswith('.json'):
        file_path = os.path.join(json_dir, filename)

        with open(file_path, 'r') as file:
            json_data = json.load(file)
            filename, doc_rev = db.save(json_data)
            print(f'Inserted document with ID: {filename} and revision: {doc_rev}')

print('All JSON files inserted into the database.')
