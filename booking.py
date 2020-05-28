from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3


class Booking(Resource):
    TABLE_NAME = 'bookings'
    parser = reqparse.RequestParser()
    parser.add_argument('userid',
                        type=int,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('slotid',
                        type=int,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('start_time',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def post(self):
        data = Booking.parser.parse_args()

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO {table} VALUES (?, ?, NULL,?,?)".format(
            table=self.TABLE_NAME)
        cursor.execute(query, (data['userid'], data['slotid'],
                               data['start_time'], data['start_time']))

        connection.commit()
        connection.close()

        return {"message": "Your Slot is Booked"}, 201
