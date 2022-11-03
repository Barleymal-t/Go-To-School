from enum import unique
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float
from sqlalchemy.orm import relationship

from base import Base


class Lesson(Base):
    __tablename__ = 'Lesson'
    id_lesson = Column(Integer, primary_key=True, unique=True,
                        autoincrement=True, nullable=False)
    id_lecturer = Column("id_lecturer", String(60))
    id_course = Column("id_course", String(60))
    id_class = Column("id_class", String(50), unique=True, nullable=False)
    id_room = Column("id_room", String(200), nullable=False)
    timeframe = Column("timeframe", Date)
    id_proyear = Column("id_number", String(45), unique=True)
    gender = Column("gender", String(45))

    

    def __init__(self, id_lecturer, id_course, id_class, id_room, timeframe, ):
        self.id_lecturer = id_lecturer
        self.id_course = id_course
        self.id_class = id_class
        self.id_room = id_room
        self.timeframe = timeframe
        