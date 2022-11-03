from datetime import datetime
from random import randint
from flask import request, jsonify, Blueprint
from .RoomModel import Room
from flask_cors import CORS

rooms_route = Blueprint("rooms_route", __name__)
CORS(rooms_route)

# Get all rooms


#Get room by ID
@rooms_route.route("/rooms/<id>", methods=['GET'])
def getRoomById(id):
    from app import session
    try:
        room = session.query(Room).get(id)

        return ({

            "msg": {

                "id_room": room.idRoom,
                "room_name": room.room_name,
                "room_capacity": room.room_capacity,
            },
            "status": True

        }), 200
    except Exception as e:
        return ({
            'status': False,
            'msg': {
                "dev_message": (f"{e}"),
                "message": "Error: Room does not exist"
            }
        }), 400