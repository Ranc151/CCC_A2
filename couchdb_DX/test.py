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
bytesNo = os.path.getsize("twitter-huge.json")
# Login authentication
admin = 'admin'
password = 'Sjx991225'
url = f'http://{admin}:{password}@172.26.130.209:5984/'

# get couchdb instance
couch = couchdb.Server(url)

# set the db name
db_name = 'riverina_price'
db = couch[db_name]

# divide the file into parts and then read the file in parallel using MPI
startIndex = math.floor(bytesNo / size) * rank
endIndex = startIndex + math.floor(bytesNo / size)


# start to store the data
with open("twitter-huge.json", 'r', encoding='utf-8') as file:
    if rank == 0:  # rank 0 is the first part of this file so need ignore the '[' at the beginning of
        new_line = file.readline()  # ignore the '[' at the beginning of twitter-data-small.json
    file.seek(startIndex)  # Read in from the assigned part

    while True:
        new_line = file.readline()
        if new_line != "]}":
            cities = ['riverina']
            keyword = ["Expensive", "Costly", "Pricey", "High-priced", "Premium", "Luxurious", "Overpriced",
                       "Exorbitant", "Steep", "Lavish", "Splurge", "Extravagant", "Upscale", "Deluxe", "Fancy",
                       "Posh", "Exclusive", "Price tag", "Marked up", "Inflated", "Sky-high", "Inflation",
                       "Price hike", "Price surge", "Price boom", "Price gouging", "Pricey", "Overpriced",
                       "Expensive", "Costly", "Premium", "Luxury", "High-end", "Upscale", "Lavish", "Extravagant",
                       "Splurge", "Exorbitant", "Steep", "Bank-breaking", "Outrageous", "Wallet-draining",
                       "Skyrocketing", "Inflated", "Sticker shock", "Mark-up", "Price tag", "Pricey", "Pricy",
                       "Dear", "Cost-prohibitive", "Overvalued", "Overinflated", "Overrated", "Price premium",
                       "Pricey goods", "Price escalation", "Price spike", "Price index", "Price surge",
                       "Price inflation", "Price jump"]
            if cities[0] in new_line:
                for key in keyword:
                    if key in new_line:
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
                        print(f'Document saved with ID: {doc_id} and revision: {doc_rev}')
                        break
        else:
            break
if rank == 0:
    print(time.time() - begin_time)
