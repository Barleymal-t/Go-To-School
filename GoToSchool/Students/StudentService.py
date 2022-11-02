from datetime import datetime
from random import randint
from flask import request, jsonify, Blueprint
# from werkzeug.security import generate_password_hash, check_password_hash

from flask_cors import CORS

students_route = Blueprint("students_route", __name__)
CORS(students_route)

# Get all students
