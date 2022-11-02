from datetime import datetime
from random import randint
from flask import request, jsonify, Blueprint
# from werkzeug.security import generate_password_hash, check_password_hash

from flask_cors import CORS

lecturers_route = Blueprint("lecturers_route", __name__)
CORS(lecturers_route)

# Get all lecturers