from flask import Flask
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from flask import Flask,jsonify,request
from flask_cors import CORS


from sqlalchemy import create_engine,MetaData

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


load_dotenv()

engine = create_engine( os.getenv('dbconnectionstring'),pool_pre_ping = True,pool_size=20, max_overflow=10)#establish a connection with the database

Session = sessionmaker(bind=engine)
session = Session()
meta = MetaData()
from base import Base

# Database Connection
try:
    engine.connect()
    Base.metadata.create_all(engine)
    session.commit()
    print("Database Successfully Connected")
except Exception as e:
    print('Database connection failed: %s'%(e))
    session.rollback()
finally:
    session.close()



# Home route
@app.route("/",methods = ['GET'])
def home():
    return "Welcome to GoToSchool"


#Main Logic
if __name__ == "__main__":
    CORS(app)
    app.run(debug=True)