from enum import unique
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float
from sqlalchemy.orm import relationship

from base import Base


class Room(Base):
    __tablename__ = 'Room'
    idRoom = Column(Integer, primary_key=True, unique=True,
                        autoincrement=True, nullable=False)
    room_name = Column("roomName", String(60))
    room_capacity = Column("roomCapacity", Integer, unique=True, nullable=False)

    # relationships
    lessons = relationship("Lesson", backref="room")

    

    def __init__(self, room_name, room_capacity):
        self.room_name = room_name
        self.room_capacity = room_capacity
        