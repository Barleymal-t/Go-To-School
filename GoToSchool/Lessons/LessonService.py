from datetime import datetime,date
from random import randint
from flask import request, jsonify, Blueprint
# from werkzeug.security import generate_password_hash, check_password_hash

from .LessonModel import Lesson
from Lecturers.LecturerModel import Lecturer
from Classes.ClassModel import Classi
from Rooms.RoomModel import Room
from Courses.CourseModel import Course

from flask_cors import CORS

lessons_route = Blueprint("lessons_route", __name__)
CORS(lessons_route)

# Get all lessons
@lessons_route.route("/lessons", methods=['GET'])
def getlessonss():
    from app import session
    try:
        lessons = session.query(Lesson).all()
        Json_lessons = []

        for lesson in lessons:
            lecturer = session.query(Lecturer).get(lesson.idLecturer)
            classO = session.query(Classi).get(lesson.idClass)
            room = session.query(Room).get(lesson.idRoom)
            course = session.query(Course).get(lesson.idCourse)

            Json_lessons.append(
                {

                "id_lesson": lesson.idLesson,
                "id_lecturer": lecturer.idLecturer,
                "course_name": course.courseName,
                "class_name": classO.className,
                "room_number": room.room_name,
                "start_time": lesson.timeStart,
                "end_time": lesson.timeEnd,
            }
            )
                
            #     {
            #     "msg": {

            #     "id_lesson": lesson.idLesson,
            #     "id_lecturer": lecturer.idLecturer,
            #     "course_name": course.courseName,
            #     "class_name": classO.className,
            #     "room_number": room.room_name,
            #     "start_time": lesson.timeStart,
            #     "end_time": lesson.timeEnd,
            # },
            # "status": True
            # })
        return jsonify(Json_lessons), 200
    except Exception as e:
        return ({
            'status': False,
            'msg': {
                "dev_message": (f"{e}"),
                "message": "Connection error: could not get students"
            }
        }), 400


# Get lesson by ID
@lessons_route.route("/lessons/<id>", methods=['GET'])
def getLessonById(id):
    from app import session
    try:
        lesson = session.query(Lesson).get(id)

        return ({

            "msg": {

                "id_lecturer": lesson.idStudent,
                "d_class": lesson.first_name,
                "id_room": lesson.last_name,
                "time_start": lesson.user_email,
                "time_end": lesson.user_password,
                "id_course": lesson.date_of_birth,
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



# delete lesson
@lessons_route.route("/lessons/<id>", methods=["DELETE"])
def deleteLessonsById(id):
    from app import session
    try:

        lesson = session.query(Lesson).get(id)

        # delete patient with corresponding ID

        session.delete(lesson)
        session.commit()
        return ({

            "msg": {

                "id_lecturer": lesson.idLecturer,
                "id_class": lesson.idClass,
                "id_room": lesson.idRoom,
                "time_start": lesson.timeStart,
                "time_end": lesson.timeEnd,
                "id_course": lesson.idCourse,
            },
            "status": True

        }), 200
    except Exception as e:
        session.rollback()
        return ({
            'status': False,
            'msg': {
                "dev_message": (f"{e}"),
                "message": "Error: Could not delete patient"
            }
        }), 400


# # Update patient info
# @lessons_route.route("/lessons/<id>", methods=["PUT"])
# def updateLessonDetailsById(id):
#     from app import session
#     req = request.json
# 
#id_Lecturer = req["id_lecturer"]
# 
# 
# 
# 
# 
# 
# 
#     try:
#         lesson = session.query(Lesson).get(id)

#         # update details with new parameters
#         lesson.idLecturer = req["id_lecturer"]
#         lesson.idClass = req["id_class"]
#         lesson.idRoom = req[""]
#         lesson.timeStart = req[""]
#         lesson.timeEnd = req[""]
#         lesson.idCourse = req[""]

#         patient.first_name = req["first_name"]
#         patient.middle_name = req["middle_name"]
#         patient.last_name = req["last_name"]
#         patient.user_email = req["user_email"].lower()
#         patient.person_image = req["person_image"]
#         patient.date_of_birth = req["date_of_birth"]
#         patient.house_address = req["house_address"]
#         patient.phone_number = req["phone_number"]
#         patient.id_number = req["id_number"]
#         patient.nationality = req["nationality"]
#         patient.gender = req["gender"]
#         # patient.id_doctor = req["id_doctor"]
#         patient.id_guardian = req["id_guardian"]

#         session.commit()
#         return ({

#             "msg": {
#                 "id_patient": patient.id_patient,
#                 "first_name": patient.first_name,
#                 "middle_name": patient.middle_name,
#                 "last_name": patient.last_name,
#                 "user_email": patient.user_email,
#                 "person_image": patient.person_image,
#                 "id_number": patient.id_number,
#                 "id_guardian": patient.id_guardian,
#                 "id_doctor": patient.id_doctor,
#                 "house_address": patient.house_address,
#                 "nationality": patient.nationality,
#                 "phone_number": patient.phone_number,
#                 "gender": patient.gender,
#                 "date_of_birth": patient.date_of_birth,
#                 "id_message": patient.id_message

#             },
#             "status": True

#         }), 200
#     except Exception as e:
#         session.rollback()
#         return ({
#             'status': False,
#             'msg': {
#                 "dev_message": (f"{e}"),
#                 "message": "Error: Could not update patient details"
#             }
#         }), 400