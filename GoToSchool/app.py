from flask import Flask

# Route importations
from Students.StudentService import students_route
from Rooms.RoomService import rooms_route
from Lessons.LessonService import lessons_route
from Lecturers.LecturerService import lecturers_route
from Courses.CourseService import courses_route
from Classes.ClassService import classes_route


app = Flask(__name__)




# App Blueprinte
app.register_blueprint(students_route)
app.register_blueprint(rooms_route)
app.register_blueprint(lessons_route)
app.register_blueprint(lecturers_route)
app.register_blueprint(courses_route)
app.register_blueprint(classes_route)




# Home route
@app.route("/",methods = ['GET'])
def home():
    return "Welcome to GoToSchool"


#Main Logic
if __name__ == "__main__":
    # CORS(app)
    app.run(debug=True)