import couchdb
import json
import time
from mpi4py import MPI
import os.path
import math

# use MPI to save processing time
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
begin_time = time.time()
bytesNo = os.path.getsize("twitter-huge.json")
# Login authentication
admin = 'admin'
password = 'Sjx991225'
url = f'http://{admin}:{password}@172.26.130.209:5984/'

# get couchdb instance
couch = couchdb.Server(url)

# set the db name
<<<<<<< HEAD
db_name = 'twitter_dataset'
db = couch[db_name]

=======
db_name = 't'
# db = couch[db_name]

# Whether the database exists
if db_name in couch:
    db = couch[db_name]
else:
    db = couch.create(db_name)

>>>>>>> origin/master
# divide the file into parts and then read the file in parallel using MPI
startIndex = math.floor(bytesNo / size) * rank
endIndex = startIndex + math.floor(bytesNo / size)


# start to store the data
with open('twitter-huge.json', 'r', encoding='utf-8') as file:
    if rank == 0:  # rank 0 is the first part of this file so need ignore the '[' at the beginning of
        new_line = file.readline()  # ignore the '[' at the beginning of twitter-data-small.json
    file.seek(startIndex)  # Read in from the assigned part

    while True:
        new_line = file.readline()
        if new_line != "]}":
<<<<<<< HEAD
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
                       'employed full-time', 'employed part-time', 'not in labour force', 'unemployed total',
                       '15 to 24', '25 to 34', '35 to44',
                       '45 to 54', '55 to 64', '65 and over']
            stop_all_loops = False
            for i in keyword_area:
                if i in new_line:
                    for j in keyword_epidemic:
                        if j in new_line:
                            for p in keyword_time:
                                if p in new_line:
                                    for t in keyword:
                                        if t in new_line:
                                            stop_all_loops = True
=======
>>>>>>> origin/master

            twitter = json.loads(new_line[:-2])  # load a json string to dict
            t_id = twitter.get("id")
            doc = db.get("_id")
            if db.get(t_id):
                rev = db.get(t_id).rev
                twitter["_id"] = t_id
                twitter["_rev"] = rev
            else:
                twitter["_id"] = t_id
                doc_id, doc_rev = db.save(twitter)  # analyse the twitter

<<<<<<< HEAD
                                            doc_id, doc_rev = db.save(twitter)  # analyse the twitter
                                            break
                                    if stop_all_loops:
                                        break
                            if stop_all_loops:
                                break
                    if stop_all_loops:
                        break
=======
>>>>>>> origin/master
            if file.tell() >= endIndex:  # stops when the assigned range is exceeded
                break
        else:
            break

if rank == 0:
    print(time.time() - begin_time)
