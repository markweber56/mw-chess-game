import os

from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO, send

app = Flask(__name__)
cors = CORS(app, resources={r"/data": {"origins": "*"}})
socketio = SocketIO(app, cors_allowed_origins="*")
env = os.environ.get('env')

@app.route("/")
def index():
    return ("hello world!")

@app.route("/home")
def home():
    return("this is the home page!")

@app.route("/data")
def data():
    data = {'a': 1, 'b': 'a string', 'env': env}
    return data

@socketio.on("message")
def handleMessage(msg):
    print(msg)
    send(msg, broadcast=True)
    return
