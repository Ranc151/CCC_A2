import couchdb
from mastodon import Mastodon, StreamListener
import json
from mpi4py import MPI

# authentication
admin = 'admin'
password = 'Sjx991225'
url = f'http://{admin}:{password}@172.26.130.209:5984/'

# get couchdb instance
couch = couchdb.Server(url)

# indicate the db name
db_name = 'mastodon'

# if not exist, create one
if db_name not in couch:
    db = couch.create(db_name)
else:
    db = couch[db_name]

# optional, better not hardcode here
token = '_a0u5oZfyz5AFL896YEglRPZc08zzV-2QKPcR5fzmfw'
m = Mastodon(
    # your server here
    api_base_url=f'https://mastodon.cloud',
    access_token=token
)
# token = '44vF0WecDpS34kI_HQuwTCYu4XE1GbH_kKK0B7G-nLQ'
# m = Mastodon(
#     # your server here
#     api_base_url=f'https://mastodon.au',
#     access_token=token
# )

# token = 'Bf-Cjcq3Gdnhz8LmZmPU4uzB2QN0_Kq7gYZty0LQRwg'
# m = Mastodon(
#     # your server here
#     api_base_url=f'https://mastodon.social',
#     access_token=token
# )


# listen on the timeline
class Listener(StreamListener):
    # called when receiving new post or status update
    def on_update(self, status):
        # do sth
        json_str = json.dumps(status, indent=2, sort_keys=True, default=str)
        doc_id, doc_rev = db.save(json.loads(json_str))
        print(f'Document saved with ID: {doc_id} and revision: {doc_rev}')


# make it better with try-catch and error-handling
m.stream_public(Listener())
