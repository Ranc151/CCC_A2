import couchdb
from mastodon import Mastodon, StreamListener
import json
import csv, os, time

# Login authentication
admin = 'admin'
password = 'Sjx991225'
url = f'http://{admin}:{password}@172.26.130.209:5984/'

# get couchdb instance
couch = couchdb.Server(url)

# set the db name
db_name = 'mastodon'

# Whether the database exists
if db_name in couch:
    db = couch[db_name]
else:
    db = couch.create(db_name)

token = 'hSX3gkvQ18YnyQKNIv25zuBJu6cTP8uWSKUjanOUr8U'
mastodon = Mastodon(
    api_base_url=f'https://mastodon.social',
    access_token=token
)


class Listener(StreamListener):
    def on_update(self, status):

        json_str = json.dumps(status, indent=2, sort_key=True, default=str)
        doc_id, doc_rev = db.save(json.load(json_str))
        print(f'Document: {doc_id} and rev: {dov_rev}')


mastodon.stream_public(Listener())
