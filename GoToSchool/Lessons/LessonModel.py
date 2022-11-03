from enum import unique
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float
from sqlalchemy.orm import relationship

# Import Other models
from Lecturers.LecturerModel import Lecturer
from Courses.CourseModel import Course
from Classes.ClassModel import Classi
from Rooms.RoomModel import Room

from base import Base


class Lesson(Base):
    __tablename__ = 'Lesson'
    idLesson = Column(Integer, primary_key=True, unique=True,
                        autoincrement=True, nullable=False)
    idLecturer = Column(Integer, ForeignKey(Lecturer.idLecturer), nullable=False)
    idCourse = Column(Integer, ForeignKey(Course.idCourse), nullable=False)
    idClass = Column(Integer, ForeignKey(Classi.idClass), nullable=False)
    idRoom = Column(Integer, ForeignKey(Room.idRoom), nullable=False)
    timeStart = Column('timeStart',Date)
    timeEnd = Column('timeEnd',Date)
   
    

    def __init__(self, idLecturer, idCourse, idClass, idRoom, timeEnd,timeStart):
        self.id_lecturer = idLecturer
        self.id_course = idCourse
        self.id_class = idClass
        self.id_room = idRoom
        self.timeEnd = timeEnd
        self.timeStart = timeStart
        