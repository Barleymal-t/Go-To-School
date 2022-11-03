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
    id_lecturer = Column(Integer, ForeignKey(Lecturer.id_lecturer), nullable=False)
    id_course = Column(Integer, ForeignKey(Course.id_course), nullable=False)
    id_class = Column(Integer, ForeignKey(Classi.id_class), nullable=False)
    id_room = Column(Integer, ForeignKey(Room.id_room), nullable=False)
    timeStart = Column('time_start',Date)
    timeEnd = Column('time_end',Date)
   
    

    def __init__(self, id_lecturer, id_course, id_class, id_room, timeEnd,timeStart):
        self.id_lecturer = id_lecturer
        self.id_course = id_course
        self.id_class = id_class
        self.id_room = id_room
        self.timeEnd = timeEnd
        self.timeStart = timeStart
        