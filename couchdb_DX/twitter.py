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
db_name = 't'
# db = couch[db_name]

# Whether the database exists
if db_name in couch:
    db = couch[db_name]
else:
    db = couch.create(db_name)

# divide the file into parts and then read the file in parallel using MPI
startIndex = math.floor(bytesNo / size) * rank
endIndex = startIndex + math.floor(bytesNo / size)

# startIndex = 1500000 * rank
# endIndex = startIndex + 1500000

# start to store the data
with open('twitter-huge.json', 'r', encoding='utf-8') as file:
    if rank == 0:  # rank 0 is the first part of this file so need ignore the '[' at the beginning of
        # twitter-data-small.json
        new_line = file.readline()  # ignore the '[' at the beginning of twitter-data-small.json
    file.seek(startIndex)  # Read in from the assigned part

    while True:
        new_line = file.readline()
        if new_line != "]}":

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

            if file.tell() >= endIndex:  # stops when the assigned range is exceeded
                break
        else:
            break

if rank == 0:
    print(time.time() - begin_time)
    # new_line = file.readline()
    # for i in range(1):
    #    new_line = file.readline()

    #    text = text + new_line

    # t = json.loads(text[:-2])
    # db.save(t)
    # print(line_count)

