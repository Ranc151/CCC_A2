import couchdb
from mastodon import Mastodon, StreamListener
import json
from mpi4py import MPI
import time

# authentication
admin = 'admin'
password = 'Sjx991225'
url = f'http://{admin}:{password}@172.26.130.209:5984/'

# get couchdb instance
couch = couchdb.Server(url)

# indicate the db name
db = couch["mastodon"]

# use MPI to save processing time
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
begin_time = time.time()


def read_data_from_server(n_url, n_token):
    m = Mastodon(
        access_token=n_token,
        api_base_url=n_url
    )

    class Listener(StreamListener):
        # called when receiving new post or status update
        def on_update(self, status):
            # do sth
            json_str = json.dumps(status, indent=2, sort_keys=True, default=str)

            keyword_area = ['Sydney', 'Melbourne', 'Brisbane', 'Perth', 'Adelaide', 'Hobart', 'Darwin', 'Canberra',
                            'Australian', 'Australia']
            keyword_epidemic = ['epidemic', 'virus', 'coronavirus', 'COVID-19', 'vaccine',
                                'preventative measures', 'mask', 'social distancing', 'testing',
                                'quarantine', 'lockdown', 'outbreak', 'cases', 'death toll', 'recovery',
                                'state of emergency']
            keyword_time = ["2020", "2021"]
            keyword = ['unemployment rate', 'employment rate', 'job seekers', 'job vacancies', 'career transition',
                       'labor market', 'salary',
                       'full-time', 'part-time', 'self-employment', 'vocational training',
                       'employment opportunities', 'labor force participation rate', 'rent', 'apartment', 'house',
                       'lease',
                       'landlord', 'tenant',
                       'real estate', 'property management', 'security deposit', 'utilities',
                       'rental agreement', 'eviction', 'rental market', 'rental income', 'cost of living', 'inflation',
                       'consumer price index',
                       'price level', 'wage growth', 'price stability', 'deflation',
                       'living expenses', 'food prices', 'energy prices', 'housing costs',
                       'transportation costs', 'healthcare costs', 'education costs',
                       'childcare costs', 'retirement savings']
            stop_all_loops = False
            for i in keyword_area:
                if i in json_str:
                    for j in keyword_epidemic:
                        if j in json_str:
                            for p in keyword_time:
                                if p in json_str:
                                    for t in keyword:
                                        if t in json_str:
                                            stop_all_loops = True
                                            mastodon = json.loads(json_str)
                                            t_id = mastodon.get("account").get("acct")
                                            print(t_id)
                                            if db.get(t_id):
                                                rev = db.get(t_id).rev
                                                mastodon["_id"] = t_id
                                                mastodon["_rev"] = rev
                                            else:
                                                mastodon["_id"] = t_id
                                            doc_id, doc_rev = db.save(mastodon)
                                            print(f'Document saved with ID: {doc_id} and revision: {doc_rev}')
                                            break
                                    if stop_all_loops:
                                        break
                            if stop_all_loops:
                                break
                    if stop_all_loops:
                        break

            mastodon = json.loads(json_str)
            t_id = mastodon.get("account").get("acct")
            if db.get(t_id):
                rev = db.get(t_id).rev
                mastodon["_id"] = t_id
                mastodon["_rev"] = rev
            else:
                mastodon["_id"] = t_id
            doc_id, doc_rev = db.save(mastodon)
            print(f'Document saved with ID: {doc_id} and revision: {doc_rev}')


    # make it better with try-catch and error-handling
    m.stream_public(Listener())


if rank == 0:
    url = f'https://mastodon.cloud'
    token = '_a0u5oZfyz5AFL896YEglRPZc08zzV-2QKPcR5fzmfw'
    read_data_from_server(url, token)

if rank == 1:
    url = f'https://mastodon.au'
    token = '44vF0WecDpS34kI_HQuwTCYu4XE1GbH_kKK0B7G-nLQ'
    read_data_from_server(url, token)

if rank == 2:
    url = f'https://mastodon.social'
    token = 'Bf-Cjcq3Gdnhz8LmZmPU4uzB2QN0_Kq7gYZty0LQRwg'
    read_data_from_server(url, token)
