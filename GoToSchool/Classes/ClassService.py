from datetime import datetime
from random import randint
from flask import request, jsonify, Blueprint
from .ClassModel import Classi
from flask_cors import CORS

classes_route = Blueprint("classes_route", __name__)
CORS(classes_route)

# Get all classes

#Get Class Route by ID
@classes_route.route("/classs/<id>", methods=['GET'])
def getClassById(id):
    from app import session
    try:
        classO = session.query(Classi).get(id)

        return ({

            "msg": {

                "id_class": classO.id_class,
                "first_name": classO.first_name,
                "last_name": classO.last_name,
                "user_email": classO.user_email,
                "user_password": classO.user_password,
                "date_of_birth": classO.date_of_birth,
                "id_proyear": classO.id_proyear,
            },
            "status": True

        }), 200
    except Exception as e:
        return ({
            'status': False,
            'msg': {
                "dev_message": (f"{e}"),
                "message": "Error: Class ID does not exist"
            }
        }), 400



# @classes_route.route()