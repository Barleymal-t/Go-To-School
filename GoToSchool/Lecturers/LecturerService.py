from datetime import datetime
from random import randint
from flask import request, jsonify, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash

#
from .LecturerModel import Lecturer

from flask_cors import CORS

lecturers_route = Blueprint("lecturers_route", __name__)
CORS(lecturers_route)

# Lecturer SignUp
@lecturers_route.route("/lecturers/signup", methods=['POST'])
def createLecturer():
    from app import session
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')

        # Check for right body parameter type
        if (content_type == 'application/json'):
            req = request.json
            user_email = req["user_email"].lower()
            user_password = req["user_password"]
            isLecturer = session.query(Lecturer).filter(
                Lecturer.user_email == user_email).first()

            # If lecturer has already been registered
            if (isLecturer):
                return ({
                        'status': False,
                        'msg': {
                            "dev_messsage": '',
                            "message": "User Email already registered. Do you want to login?"
                        }
                        }), 400
            first_name = req["first_name"]
            last_name = req["last_name"]
            user_email = req["user_email"].lower()
            date_of_birth = req["date_of_birth"]
            user_password = req["user_password"]


            passwordHash = generate_password_hash(user_password)
            newLecturer = Lecturer(first_name=first_name, last_name=last_name, user_email=user_email, user_password=passwordHash,
                                 date_of_birth=date_of_birth)
            try:
                session.add(newLecturer)
                session.commit()
            except Exception as e:
                session.rollback()
                return ({
                        'status': False,
                        'msg': {
                            "dev_message": (f"{e}"),
                            "message": "Connection Error: User not recorded"
                        }
                        }), 400

            id_lecturer = session.query(Lecturer.idLecturer).filter(Lecturer.user_email == user_email).first()

            lecturerInfo = session.query(Lecturer).get(id_lecturer)
            
            session.commit()

            if (check_password_hash(lecturerInfo.user_password, user_password)):
                return ({
                    "msg": {

                "id_lecturer": lecturerInfo.idLecturer,
                "first_name": lecturerInfo.first_name,
                "last_name": lecturerInfo.last_name,
                "user_email": lecturerInfo.user_email,
                "user_password": lecturerInfo.user_password,
                "date_of_birth": lecturerInfo.date_of_birth,
            },
            "status": True
                }), 200
        else:
            return ({
                'status': False,
                'msg': {
                    "dev_message": "",
                    "message": "Error: Content-Type Error"
                }
            }), 400


# Lecturer LogIn
@lecturers_route.route("/lecturers/login", methods=['POST'])
def lecturerLogin():
    from app import session
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        req = request.json
        user_email = req["user_email"].lower()
        user_password = req["user_password"]

    # Check Email to make sure the student is already registered
        try:
            id_lecturer = session.query(Lecturer.idLecturer).filter(Lecturer.user_email == user_email).first()
            if (id_lecturer):
                lecturerInfo = session.query(Lecturer).get(id_lecturer)
                session.commit()

                # Check Password after user email has been verified to retreive corresponsing password hash
                try:
                    userDbPassword = str(lecturerInfo.user_password)
                    if (check_password_hash(userDbPassword, user_password)):
                        return ({
                            "msg": {
                                            "id_lecturer": lecturerInfo.idLecturer,
                                            "first_name": lecturerInfo.first_name,
                                            "last_name": lecturerInfo.last_name,
                                            "user_email": lecturerInfo.user_email,
                                            "user_password": lecturerInfo.user_password,
                                            "date_of_birth": lecturerInfo.date_of_birth,
                                        },
                                        "status": True
                        }), 200  # StatusCode
                    else:
                        return ({
                            'status': False,
                            'msg': {
                                "dev_message": "",
                                "message": "Incorrect Password. Kindly Try again"
                            }
                        }), 400

                except Exception as e:
                    session.rollback()
                    return ({
                        'status': False,
                        'msg': {
                            "dev_message": (f"{e}"),
                            "message": "Connection Error: Could not login"
                        }
                    }), 400

            # User has not yet been registered
            else:
                return ({
                        'status': False,
                        'msg': {
                            "dev_message": "",
                            "message": "User not registered.Do you want to sign up?"
                        }
                        }), 400

        except Exception as e:
            session.rollback()
            print(e)
            return ({
                'status': False,
                'msg': {
                    "dev_message": (f"{e}"),
                    "message": "Connection Error: Check your network connection"
                }
            }), 400
    else:
        return ({
            'status': False,
            'msg': {
                "dev_message": "",
                "message": "Bad Request Error"
            }
        }), 404
