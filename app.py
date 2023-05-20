from datetime import timedelta

from flask import Flask, request, render_template, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS

# setting config
app = Flask(__name__)
CORS(app)  # Resolve cross-domain issues and make the back-end api accessible to all
# CORS(app,origins='http://127.0.0.1:5000')
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port='5000')


# app.config['DEBUG'] = True          # debug model open
# app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)  # default Cache control by second

@app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'
def root():  # the main page
    return render_template("Index.html")


# default GET
@app.route('/api_0/<param>')
def api_0(param):
    print(param)

    return param


@app.route('/api_1/', methods=['GET', 'POST'])
def api_1():
    if request.method == 'POST':
        print((request.json['type']))
        return
    else:
        return
