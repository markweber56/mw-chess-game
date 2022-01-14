from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/data": {"origins": "*"}})

@app.route("/")
def index():
        return ("hello world!")

@app.route("/home")
def home():
        return("this is the home page!")

@app.route("/data")
def data():
    data = {'a': 1, 'b': 'a string'}
    return data
