import couchdb
import json
import time
from mpi4py import MPI


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

    for i in range(5):
        new_line = file.readline()
        if new_line != "]}":
            keyword_area = ['sydney', 'melbourne', 'brisbane', 'perth', 'adelaide', 'hobart', 'darwin', 'canberra', 'australia']
            keyword_epidemic = ['epidemic', 'virus', 'coronavirus', 'COVID-19', 'vaccine',
                                'preventative measures', 'mask', 'social distancing', 'testing',
                                'quarantine', 'lockdown', 'outbreak', 'cases', 'death toll', 'recovery',
                                'state of emergency']
            keyword_time = ["2020", "2021", "2022"]
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
            for i in keyword_time:
                if i in new_line.lower():
                    for j in keyword_time:
                        if j in new_line.lower():
                            for p in keyword_time:
                                if p in new_line.lower():
                                    for t in keyword_time:
                                        if t in new_line.lower():
                                            stop_all_loops = True
                                            print(new_line)
                                             # load a json string to dict

                                            # analyse the twitter
                                            break
                                    if stop_all_loops:
                                        break
                            if stop_all_loops:
                                break
                    if stop_all_loops:
                        break
        else:
            break
