from datetime import datetime
from random import randint
from flask import request, jsonify, Blueprint
# from werkzeug.security import generate_password_hash, check_password_hash

from flask_cors import CORS

lessons_route = Blueprint("lessons_route", __name__)
CORS(lessons_route)

# Get all lessons