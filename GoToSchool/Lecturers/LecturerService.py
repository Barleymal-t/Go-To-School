from datetime import datetime
from random import randint
from flask import request, jsonify, Blueprint
from .LecturerModel import Lecturer
from flask_cors import CORS

lecturers_route = Blueprint("lecturers_route", __name__)
CORS(lecturers_route)

# Get all lecturers


#Get Lecturers by ID
@lecturers_route.route("/lecturers/<id>", methods=['GET'])
def getLecturerById(id):
    from app import session
    try:
        lecturer = session.query(Lecturer).get(id)

        return ({

            "msg": {

                "id_lecturer": lecturer.id_lecturer,
                "first_name": lecturer.first_name,
                "last_name": lecturer.last_name,
                "user_email": lecturer.user_email,
                "user_password": lecturer.user_password,
                "date_of_birth": lecturer.date_of_birth,
            },
            "status": True

        }), 200
    except Exception as e:
        return ({
            'status': False,
            'msg': {
                "dev_message": (f"{e}"),
                "message": "Error: Lecturer ID does not exist"
            }
        }), 400

