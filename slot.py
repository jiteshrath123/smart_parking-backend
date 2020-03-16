from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3


class Slot(Resource):
    TABLE_NAME = 'slots'

    parser = reqparse.RequestParser()
    parser.add_argument('status',
                        type=bool,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    @jwt_required()
    def get(self, slotid):
        slot = self.find_by_name(slotid)
        if slot:
            return slot
        return {'message': 'Slots not found'}, 404

    @classmethod
    def find_by_name(cls, slotid):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table} WHERE slotid=?".format(
            table=cls.TABLE_NAME)
        result = cursor.execute(query, (slotid,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'slot': {'id': row[0], 'status': row[1]}}

    def post(self, slotid):
        if self.find_by_name(slotid):
            return {'message': "An item with name '{}' already exists.".format(slotid)}

        data = Slot.parser.parse_args()

        slot = {'slotid': slotid, 'status': data['status']}

        try:
            Slot.insert(slot)
        except:
            return {"message": "An error occurred inserting the item."}

        return slot

    @classmethod
    def insert(cls, slot):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO {table} VALUES(?, ?)".format(table=cls.TABLE_NAME)
        cursor.execute(query, (slot['slotid'], slot['status']))

        connection.commit()
        connection.close()

    @jwt_required()
    def delete(self, slotid):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM {table} WHERE slotid=?".format(
            table=self.TABLE_NAME)
        cursor.execute(query, (slotid,))

        connection.commit()
        connection.close()

        return {'message': 'Item deleted'}

    @jwt_required()
    def put(self, slotid):
        data = Slot.parser.parse_args()
        slot = self.find_by_name(slotid)
        updated_slot = {'slotid': slotid, 'status': data['status']}
        if slot is None:
            try:
                Slot.insert(updated_slot)
            except:
                return {"message": "An error occurred inserting the slot."}
        else:
            try:
                Slot.update(updated_slot)
            except:
                return {"message": "An error occurred updating the slot."}
        return updated_slot

    @classmethod
    def update(cls, slot):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "UPDATE {table} SET status=? WHERE slotid=?".format(
            table=cls.TABLE_NAME)
        cursor.execute(query, (slot['status'], slot['slotid']))

        connection.commit()
        connection.close()


class SlotsList(Resource):
    TABLE_NAME = 'slots'

    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table}".format(table=self.TABLE_NAME)
        result = cursor.execute(query)
        slots = []
        for row in result:
            slots.append({'slotid': row[0], 'status': row[1]})
        connection.close()

        return {'slots': slots}
