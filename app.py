import json
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import couchdb

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

# setting config
app = Flask(__name__)
CORS(app)  # Resolve cross-domain issues and make the back-end api accessible to all


# CORS(app,origins='http://127.0.0.1:5000')


# app.config['DEBUG'] = True          # debug model open
# app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)  # default Cache control by second

@app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'
def root():  # the main page
    return render_template("Index.html")


# default GET
@app.route('/get_source_data_GCCSA')
def get_source_data_GCCSA():
    with open('./couchdb_DX/SUDO_file/new_csv/GCCSA_json/Labour_2021.json') as f:
        res = json.load(f)
    # Return the results as JSON
    return res


@app.route('/get_source_data_SA4')
def get_source_data_SA4():
    with open('./couchdb_DX/SUDO_file/new_csv/SA4_json/Labour_2021.json') as f:
        res = json.load(f)
    # Return the results as JSON
    return res


# @app.route('/api_1', methods=['GET', 'POST', 'DELETE'])
# def api_1():
#     if request.method == 'POST':
#         # using an existing view
#         view = db.view('languages/judge', group_level=1)
#         # Retrieve the view results
#         results = {}
#         for row in view:
#             results[row.key] = row.value
#         # Return the results as JSON
#         return {'data': results}
#     else:
#         view = db.view('languages/langAvg', group_level=1)
#         # Retrieve the view results
#         results = {}
#         print(view)
#         for row in view:
#             results[row.key] = row.value
#         # Return the results as JSON
#         return {'data': results}


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port='8080')
