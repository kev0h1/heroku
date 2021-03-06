import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        required=True,
                        help="this field cannot be left blank")
    parser.add_argument('password',
                        required=True,
                        help="this field cannot be left blank")

    def post(self):
        data = UserRegister.parser.parse_args()
        user = UserModel.find_by_username(data['username'])

        if user:
            return {'message': 'user already exists.'}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {'message': 'user created successfully.'}, 201
