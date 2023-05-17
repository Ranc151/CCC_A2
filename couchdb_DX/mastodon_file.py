import couchdb
from mastodon import Mastodon, StreamListener
import json

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
token = 'Bf-Cjcq3Gdnhz8LmZmPU4uzB2QN0_Kq7gYZty0LQRwg'
m = Mastodon(
    # your server here
    api_base_url=f'https://mastodon.social',
    access_token=token
)


# listen on the timeline
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
                   'childcare costs', 'retirement savings', 'fever', 'cough', 'sore throat', 'nasal congestion',
                   'runny nose', 'sneezing', 'body aches', 'fatigue', 'loss of appetite', 'headache', 'chills',
                   'employed full-time', 'employed part-time', 'not in labour force', 'unemployed total', '15 to 24',
                   '25 to 34', '35 to44',
                   '45 to 54', '55 to 64', '65 and over']
        stop_all_loops = False
        for i in keyword_area:
            if i in json_str:
                for j in keyword_area:
                    if j in json_str:
                        for p in keyword_area:
                            if p in json_str:
                                for t in keyword_area:
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


# make it better with try-catch and error-handling
m.stream_public(Listener())
