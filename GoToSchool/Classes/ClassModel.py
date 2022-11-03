from enum import unique
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float
from sqlalchemy.orm import relationship

from base import Base


class Classi(Base):
    __tablename__ = 'Class'
    idClass = Column(Integer, primary_key=True, unique=True,
                        autoincrement=True, nullable=False)
    classSize = Column("classSize", Integer)
    className = Column("classSize", String(10))

    # relationships
    lessons = relationship("Lesson", backref="class")

    

    def __init__(self, classSize, className ):
        self.classSize = classSize
        self.className = className
        