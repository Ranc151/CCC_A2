import couchdb
from mastodon import Mastodon, StreamListener
import json
import threading
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


def read_data_from_server(server_url, access_token):
    mastodon = Mastodon(
        access_token=access_token,
        api_base_url=server_url
    )
    timeline = mastodon.timeline_home()
    for status in timeline:
        print(status['content'])

# 定义服务器和访问令牌列表
servers = [
    {
        'url': 'https://server1.com',
        'access_token': 'access_token_1'
    },
    {
        'url': 'https://server2.com',
        'access_token': 'access_token_2'
    },
    {
        'url': 'https://server3.com',
        'access_token': 'access_token_3'
    }
]

# 创建线程列表
threads = []
for server in servers:
    thread = threading.Thread(target=read_data_from_server, args=(server['url'], server['access_token']))
    threads.append(thread)
    thread.start()

# 等待所有线程完成
for thread in threads:
    thread.join()
