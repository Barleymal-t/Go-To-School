from datetime import datetime
from random import randint
from flask import request, jsonify, Blueprint


from flask_cors import CORS

classes_route = Blueprint("classes_route", __name__)
CORS(classes_route)

# Get all classes