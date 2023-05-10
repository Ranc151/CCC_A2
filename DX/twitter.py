import couchdb
import json

from mpi4py import MPI

# use MPI to save processing time
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

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
    # divide the file into parts and then read the file in parallel using MPI
    line_count = 10
    each_part_bytes = int(line_count // size)
    mod = line_count % size
    if rank == size-1:
        begin = rank * each_part_bytes
        end = (rank + 1) * each_part_bytes + mod
    else:
        begin = rank * each_part_bytes
        end = (rank + 1) * each_part_bytes

    if rank == 0:  # rank 0 is the first part of this file so need ignore the '[' at the beginning of
        # twitter-data-small.json
        new_line = file.readline()  # ignore the '[' at the beginning of twitter-data-small.json
    file.seek(begin)  # Read in from the assigned part

    while True:
        new_line = file.readline()
        if new_line != "]}":
            twitter = json.loads(new_line[:-2])  # load a json string to dict
            keyword_area = ['Sydney', 'Melbourne', 'Brisbane', 'Perth', 'Adelaide', 'Hobart', 'Darwin', 'Canberra']
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
            for i in keyword_area:
                if i in new_line:
                    for j in keyword_epidemic:
                        if j in new_line:
                            for p in keyword_time:
                                if p in new_line:
                                    for t in key_word:
                                        if t in new_line:
                                            stop_all_loops = True

                                            data.save(twitter)  # analyse the twitter
                                            break
                                    if stop_all_loops:
                                        break
                            if stop_all_loops:
                                break
                    if stop_all_loops:
                        break
            if file.tell() >= end:  # stops when the assigned range is exceeded
                break

    #new_line = file.readline()
    #for i in range(1):
    #    new_line = file.readline()

    #    text = text + new_line

    #t = json.loads(text[:-2])
    #db.save(t)
    #print(line_count)
