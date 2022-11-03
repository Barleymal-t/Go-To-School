from enum import unique
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float
from sqlalchemy.orm import relationship

from base import Base


class Student(Base):
    __tablename__ = 'Student'
    idStudent = Column(Integer, primary_key=True, unique=True,
                        autoincrement=True, nullable=False)
    first_name = Column("firstName", String(45))
    last_name = Column("lastName", String(45))
    user_email = Column("email", String(45), unique=True, nullable=False)
    user_password = Column("userPassword", String(200), nullable=False)
    date_of_birth = Column("dOB", Date)
    id_proyear = Column("proyear", String(45), unique=True)
    # gender = Column("gender", String(45))

    

    def __init__(self, first_name, last_name, user_email, user_password, date_of_birth, id_proyear):
        self.first_name = first_name
        self.last_name = last_name
        self.user_email = user_email
        self.user_password = user_password
        self.date_of_birth = date_of_birth
        self.id_proyear = id_proyear
        