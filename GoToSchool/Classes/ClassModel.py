from enum import unique
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float
from sqlalchemy.orm import relationship

from base import Base


class Class(Base):
    __tablename__ = 'Class'
    id_class = Column(Integer, primary_key=True, unique=True,
                        autoincrement=True, nullable=False)
    classSize = Column("classSize", String(60))

    

    def __init__(self, classSize, ):
        self.classSize = classSize
        