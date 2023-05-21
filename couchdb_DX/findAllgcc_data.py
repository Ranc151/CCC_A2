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
bytesNo = os.path.getsize("G:\\py\\twitter-huge.json")
# Login authentication
admin = 'admin'
password = 'Sjx991225'
url = f'http://{admin}:{password}@172.26.130.209:5984/'

# get couchdb instance
couch = couchdb.Server(url)

# set the db name
db_name = 'twi_gcc_em'
db = couch[db_name]

# divide the file into parts and then read the file in parallel using MPI
startIndex = math.floor(bytesNo / size) * rank
endIndex = startIndex + math.floor(bytesNo / size)

# start to store the data
with open("G:\\py\\twitter-huge.json", 'r', encoding='utf-8') as file:
    if rank == 0:  # rank 0 is the first part of this file so need ignore the '[' at the beginning of
        new_line = file.readline()  # ignore the '[' at the beginning of twitter-data-small.json
    file.seek(startIndex)  # Read in from the assigned part

    employDictionary = {}
    employKeyword = [' Employment ', ' employment ', ' Job ', ' job ', ' Hiring ', ' hiring ', ' Workforce ',
                     ' workforce ', ' Employee ', ' employee ', ' Employer ', ' employer ', ' Job market ',
                     ' job market ', ' Job seeker ', ' job seeker ', ' Career ', ' career ', ' Wage ', ' wage ',
                     ' Salary ', ' salary ', ' Part-time ', ' part-time ', ' Full-time ', ' full-time ', ' Recruitment ',
                     ' recruitment ', ' Staffing ', ' staffing ', ' Labor force ', ' labor force ',
                     ' Employment rate ', ' employment rate ', ' Job creation ', ' job creation ',
                     ' Job growth ', ' job growth ', ' Labor statistics ', ' labor statistics ', ' Job opportunities ',
                     ' job opportunities ']
    while True:
        new_line = file.readline()
        if new_line != "]}":
            cities = [' Sydney ', ' Melbourne ', ' Brisbane ', ' Adelaide ', ' Perth ', ' sydney ',
                      ' melbourne ', ' brisbane ', ' adelaide ', ' perth ', ' SYD ', ' MEL ', ' BNE ',
                      ' ADL ', ' PER ']
            found = False
            for city in cities:
                if found:
                    break

                if city in (" " + new_line + " "):
                    for emp in employKeyword:
                        if emp in (" " + new_line + " "):
                            if city not in employDictionary.keys():
                                employDictionary[city] = 1
                            else:
                                employDictionary[city] += 1

                            twitter = json.loads(new_line[:-2])
                            t_id = twitter.get("id")
                            doc = db.get("_id")
                            if db.get(t_id):
                                rev = db.get(t_id).rev
                                twitter["_id"] = t_id
                                twitter["_rev"] = rev
                            else:
                                twitter["_id"] = t_id
                            doc_id, doc_rev = db.save(twitter)
                            print(employDictionary)
                            found = True
                            break

        else:
            break
if rank == 0:
    print(time.time() - begin_time)
