from enum import unique
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float
from sqlalchemy.orm import relationship

from base import Base


class Student(Base):
    __tablename__ = 'Student'
    id_student = Column(Integer, primary_key=True, unique=True,
                        autoincrement=True, nullable=False)
    first_name = Column("first_name", String(60))
    last_name = Column("last_name", String(60))
    user_email = Column("user_email", String(50), unique=True, nullable=False)
    user_password = Column("user_password", String(200), nullable=False)
    date_of_birth = Column("date_of_birth", Date)
    id_proyear = Column("id_number", String(45), unique=True)
    gender = Column("gender", String(45))

    

    def __init__(self, first_name, last_name, user_email, user_password, date_of_birth, id_proyear, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.user_email = user_email
        self.user_password = user_password
        self.date_of_birth = date_of_birth
        self.id_proyear = id_proyear
        self.gender = gender
        