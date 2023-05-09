from datetime import timedelta

from flask import Flask, request, render_template, jsonify

# setting config
app = Flask(__name__)
app.config['DEBUG'] = True          # debug model open
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)  # default Cache control by second

# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'


if __name__ == '__main__':
    app.run()
