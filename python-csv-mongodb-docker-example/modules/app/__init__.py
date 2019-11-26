""" flask app with mongo """
from flask import Flask
app = Flask(__name__)

from modules.app.apis import *
