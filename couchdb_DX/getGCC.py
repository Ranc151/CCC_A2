import couchdb
import json
import time
from mpi4py import MPI
import os.path
import math

# use MPI to save processing time.
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
begin_time = time.time()
bytesNo = os.path.getsize("G:\\py\\twitter-huge.json")
# Login authentication
admin = 'admin'
password = 'Sjx991225'
url = f'http://{admin}:{password}@172.26.130.209:5984/'

# get couchdb instance
couch = couchdb.Server(url)

# set the db name
db_name = 'final_gcc'
db = couch[db_name]

# divide the file into parts and then read the file in parallel using MPI
startIndex = math.floor(bytesNo / size) * rank
endIndex = startIndex + math.floor(bytesNo / size)

# start to store the data
with open("G:\\py\\twitter-huge.json", 'r', encoding='utf-8') as file:
    if rank == 0:  # rank 0 is the first part of this file so need ignore the '[' at the beginning of
        new_line = file.readline()  # ignore the '[' at the beginning of twitter-data-small.json
    file.seek(startIndex)  # Read in from the assigned part

    while True:
        new_line = file.readline()
        if new_line != "]}":
            cityList = [' 1GSYD ', ' 1gsyd ', ' 2GMEL ', ' 2gmel ', ' 3GBRI ', ' 3gbri ', ' 4GADE ',
                        ' 4gade ', ' 5GPER ', ' 5gper ', ' SYD ', ' syd ', ' MEL ', ' mel ', ' BRI ', ' bri ',
                        ' ADE ', ' ade ', ' PER ', ' per ', ' Sydney ', ' sydney ', ' Melbourne' , ' melbourne ',
                        ' Brisbane ', ' brisbane ', ' Adelaide ',  'adelaide ', ' Perth ', ' perth ', ' Hobart ',
                        ' hobart ', ' Canberra ', ' canberra ', ' Darwin' , ' darwin ']
            for city in cityList:
                if city in (" " + new_line + " "):
                    twitter = json.loads(new_line[:-2])
                    t_id = twitter.get("id")
                    doc = db.get("_id")
                    if db.get(t_id):
                        rev = db.get(t_id).rev
                        twitter["_id"] = t_id
                        twitter["_rev"] = rev
                    else:
                        twitter["_id"] = t_id
                    doc_id, doc_rev = db.save(twitter)  # analyse the twitter
                    break
        else:
            break
if rank == 0:
    print(time.time() - begin_time)
