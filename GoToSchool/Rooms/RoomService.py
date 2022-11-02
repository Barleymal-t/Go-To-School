from datetime import datetime
from random import randint
from flask import request, jsonify, Blueprint
# from werkzeug.security import generate_password_hash, check_password_hash

from flask_cors import CORS

rooms_route = Blueprint("rooms_route", __name__)
CORS(rooms_route)

# Get all rooms