from datetime import datetime
from random import randint
from flask import request, jsonify, Blueprint
# from werkzeug.security import generate_password_hash, check_password_hash

from flask_cors import CORS

courses_route = Blueprint("courses_route", __name__)
CORS(courses_route)

# Get all courses