from datetime import datetime
from random import randint
from flask import request, jsonify, Blueprint
from .CourseModel import Course
from flask_cors import CORS

courses_route = Blueprint("courses_route", __name__)
CORS(courses_route)

# Get all courses


#Get Course by ID
@courses_route.route("/courses/<id>", methods=['GET'])
def getCourseById(id):
    from app import session
    try:
        course = session.query(Course).get(id)

        return ({

            "msg": {

                "id_course": course.id_course,
                "courseCode": course.courseCode,
                "courseName": course.courseName,
            },
            "status": True

        }), 200
    except Exception as e:
        return ({
            'status': False,
            'msg': {
                "dev_message": (f"{e}"),
                "message": "Error: Course ID does not exist"
            }
        }), 400
