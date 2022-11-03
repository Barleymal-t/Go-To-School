from enum import unique
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float
from sqlalchemy.orm import relationship

from base import Base


class Course(Base):
    __tablename__ = 'Course'
    id_course = Column(Integer, primary_key=True, unique=True,
                        autoincrement=True, nullable=False)
    courseCode = Column("courseCode", String(60))
    courseName = Column("courseName", String(60))

    

    def __init__(self, courseCode, courseName, ):
        self.courseCode = courseCode
        self.courseName = courseName
        