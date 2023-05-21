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
db_name = 'final_smc'
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
            cityList = ['Central Coast', 'Sydney - Baulkham Hills and Hawkesbury', 'Sydney - Blacktown',
                        'Sydney - City and Inner South', 'Sydney - Eastern Suburbs', 'Sydney - Inner South West',
                        'Sydney - Inner West', 'Sydney - North Sydney and Hornsby', 'Sydney - Northern Beaches',
                        'Sydney - Outer South West', 'Sydney - Outer West and Blue Mountains', 'Sydney - Parramatta',
                        'Sydney - Ryde', 'Sydney - South West', 'Sydney - Sutherland', 'Capital Region', 'Central West',
                        'Coffs Harbour - Grafton', 'Far West and Orana', 'Hunter Valley exc Newcastle', 'Illawarra',
                        'Mid North Coast', 'Murray', 'New England and North West', 'Newcastle and Lake Macquarie',
                        'Richmond - Tweed',
                        'Riverina', 'Southern Highlands and Shoalhaven', 'Melbourne - Inner', 'Melbourne - Inner East',
                        'Melbourne - Inner South', 'Melbourne - North East', 'Melbourne - North West',
                        'Melbourne - Outer East',
                        'Melbourne - South East', 'Melbourne - West', 'Mornington Peninsula', 'Ballarat', 'Bendigo',
                        'Geelong',
                        'Hume', 'Latrobe - Gippsland', 'North West', 'Shepparton', 'Warrnambool and South West',
                        'Brisbane - East',
                        'Brisbane - North', 'Brisbane - South', 'Brisbane - West', 'Brisbane Inner City', 'Ipswich',
                        'Logan - Beaudesert',
                        'Moreton Bay - North', 'Moreton Bay - South', 'Cairns', 'Darling Downs - Maranoa',
                        'Central Queensland',
                        'Gold Coast', 'Mackay - Isaac - Whitsunday', 'Queensland - Outback', 'Sunshine Coast',
                        'Toowoomba', 'Townsville',
                        'Wide Bay', 'Adelaide - Central and Hills', 'Adelaide - North', 'Adelaide - South',
                        'Adelaide - West',
                        'Barossa - Yorke - Mid North', 'South Australia - Outback', 'South Australia - South East',
                        'Mandurah',
                        'Perth - Inner', 'Perth - North East', 'Perth - North West', 'Perth - South East',
                        'Perth - South West',
                        'Bunbury', 'Western Australia - Wheat Belt', 'Hobart', 'Launceston and North East',
                        'South East',
                        'West and North West', 'Darwin', 'Northern Territory - Outback']
            for city in cityList:
                if city in new_line:
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
