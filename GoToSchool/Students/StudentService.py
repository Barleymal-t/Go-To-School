from datetime import datetime
from random import randint
from flask import request, jsonify, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash

# 
from .StudentModel import Student

from flask_cors import CORS

students_route = Blueprint("students_route", __name__)
CORS(students_route)

# Get all students
@students_route.route("/students", methods=['GET'])
def getStudents():
    from app import session
    try:
        students = session.query(Student).all()
        Json_students = [{

            "msg": {

                "id_student": student.idStudent,
                "first_name": student.first_name,
                "last_name": student.last_name,
                "user_email": student.user_email,
                "user_password": student.user_password,
                "date_of_birth": student.date_of_birth,
                "id_proyear": student.id_proyear,
            },
            "status": True

        } for student in students]
        return jsonify(Json_students), 200
    except Exception as e:
        return ({
            'status': False,
            'msg': {
                "dev_message": (f"{e}"),
                "message": "Connection error: could not get students"
            }
        }), 400


# Student Signup
@students_route.route("/students/signup", methods=['POST'])
def createStudent():
    from app import session
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')

        # Check for right body parameter type
        if (content_type == 'application/json'):
            req = request.json
            user_email = req["user_email"].lower()
            user_password = req["user_password"]
            isStudent = session.query(Student).filter(
                Student.user_email == user_email).first()

            # If patient has already been registered
            if (isStudent):
                return ({
                        'status': False,
                        'msg': {
                            "dev_messsage": '',
                            "message": "Student Email already registered. Do you want to login?"
                        }
                        }), 400
            first_name = req["first_name"]
            last_name = req["last_name"]
            user_email = req["user_email"].lower()
            date_of_birth = req["date_of_birth"]
            user_password = req["user_password"]
            id_proyear = req["id_proyear"]


            passwordHash = generate_password_hash(user_password)
            newStudent = Student(first_name=first_name, last_name=last_name, user_email=user_email, user_password=passwordHash,
                                 date_of_birth=date_of_birth,id_proyear=id_proyear)
            try:
                session.add(newStudent)
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

            id_student = session.query(Student.idStudent).filter(Student.user_email == user_email).first()

            studentInfo = session.query(Student).get(id_student)
            
            session.commit()

            if (check_password_hash(studentInfo.user_password, user_password)):
                return ({
                    "msg": {

                "id_student": studentInfo.idStudent,
                "first_name": studentInfo.first_name,
                "last_name": studentInfo.last_name,
                "user_email": studentInfo.user_email,
                "user_password": studentInfo.user_password,
                "date_of_birth": studentInfo.date_of_birth,
                "id_proyear": studentInfo.id_proyear,
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


# Get student by ID
@students_route.route("/students/<id>", methods=['GET'])
def getStudentById(id):
    from app import session
    try:
        student = session.query(Student).get(id)

        return ({

            "msg": {

                "id_student": student.idStudent,
                "first_name": student.first_name,
                "last_name": student.last_name,
                "user_email": student.user_email,
                "user_password": student.user_password,
                "date_of_birth": student.date_of_birth,
                "id_proyear": student.id_proyear,
            },
            "status": True

        }), 200
    except Exception as e:
        return ({
            'status': False,
            'msg': {
                "dev_message": (f"{e}"),
                "message": "Error: Student ID does not exist"
            }
        }), 400

