from datetime import datetime
from random import randint
from flask import request, jsonify, Blueprint
from .LessonModel import Lesson
from flask_cors import CORS

lessons_route = Blueprint("lessons_route", __name__)
CORS(lessons_route)

# Get all lessons

#Get Lessons by ID
@lessons_route.route("/lessons/<id>", methods=['GET'])
def getLessonById(id):
    from app import session
    try:
        lesson = session.query(Lesson).get(id)

        return ({

            "msg": {

                "id_lesson": lesson.id_lesson,
                "id_lecturer": lesson.id_lecturer,
                "id_course": lesson.id_course,
                "id_class": lesson.id_class,
                "id_room": lesson.id_room,
                "timeStart": lesson.timeStart,
                "timeEnd": lesson.timeEnd,
            },
            "status": True

        }), 200
    except Exception as e:
        return ({
            'status': False,
            'msg': {
                "dev_message": (f"{e}"),
                "message": "Error: Lesson does not exist"
            }
        }), 400