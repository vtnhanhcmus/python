""" flask app with mongo """
import os
from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_URI'] = os.environ.get('DB')
mongo = PyMongo(app)

from modules.app.apis import *
