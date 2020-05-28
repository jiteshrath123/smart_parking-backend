from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3

class Booking(Resource):
    TableName = 'bookings'
    