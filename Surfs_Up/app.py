#Import flask
from flask import flask

#Create flask instance
app = Flask(__name__)

#Create flask route / denotes data put at root of routes 
@app.route('/')
def hello_world():
    return 'Hello world'