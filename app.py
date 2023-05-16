from datetime import timedelta

from flask import Flask, request, render_template, jsonify
from flask_restful import Api, Resource

# setting config
app = Flask(__name__)



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

    return


@app.route('/api_1/', methods=['GET', 'POST'])
def api_1():
    if request.method == 'POST':
        print((request.json['type']))
        return
    else:
        return




if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port='8080')
