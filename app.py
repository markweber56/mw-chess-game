from flask import Flask

app = Flask(__name__)

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
