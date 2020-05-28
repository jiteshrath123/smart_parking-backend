from flask import Flask, request
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from user import UserRegister, Login
from slot import Slot, SlotsList

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jose'
api = Api(app)


# @app.route("/auth", methods=['POST'])
# def myEndpoint():

#   requestJson = request.get_json(force=True)

#  return requestJson


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin',
                         'http://localhost:8100')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response


jwt = JWT(app, authenticate, identity)

api.add_resource(Login, '/login')
api.add_resource(Slot, '/slot/<string:slotid>')
api.add_resource(SlotsList, '/slots')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(debug=True)  # important to mention debug=True
