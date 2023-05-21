import json
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import couchdb
import base64
from PIL import Image
import io

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
@app.route('/get_source_data_GCCSA', methods=['GET'])
def get_source_data_GCCSA():
    with open('./couchdb_DX/SUDO_file/new_csv/GCCSA_json/Labour_2021.json') as f:
        res = json.load(f)
    # Return the results as JSON
    return res


@app.route('/get_source_data_SA4', methods=['GET'])
def get_source_data_SA4():
    with open('./couchdb_DX/SUDO_file/new_csv/SA4_json/Labour_2021.json') as f:
        res = json.load(f)
    # Return the results as JSON
    return res


@app.route('/get_graph_1', methods=['GET'])
def get_graph_1():
    image_path = './static/graph/sudo_Labour_pie.png'

    encoded = base64.b64encode(open(image_path, 'rb').read())
    return encoded


@app.route('/get_graph_2', methods=['GET'])
def get_graph_2():
    image_path = './static/graph/sudo_Labourem_g.png'

    encoded = base64.b64encode(open(image_path, 'rb').read())
    return encoded


@app.route('/get_graph_3', methods=['GET'])
def get_graph_3():
    image_path = './static/graph/sudo_Labourem_s.png'

    encoded = base64.b64encode(open(image_path, 'rb').read())
    return encoded


@app.route('/get_graph_4', methods=['GET'])
def get_graph_4():
    image_path = './static/graph/sudo_Labourunem_g.png'

    encoded = base64.b64encode(open(image_path, 'rb').read())
    return encoded


@app.route('/get_graph_5', methods=['GET'])
def get_graph_5():
    image_path = './static/graph/sudo_Labourunem_s.png'

    encoded = base64.b64encode(open(image_path, 'rb').read())
    return encoded




if __name__ == '__main__':
    app.run()
