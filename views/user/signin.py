from flask import Blueprint, request
from flask_restful import Api, Resource

from DB import curs

api = Api(Blueprint(__name__, __name__))


@api.resource('/signin')
class Signin(Resource):
    def post(self):
        try:
            tel = request.json['tel']
            pw = request.json['pw']
        except KeyError or TypeError:
            return {'msg': 'valueless'}, 400

        query_select_user_info = 'select uuid, permission from user where tel = %s and pw = %s'
        curs.execute(query_select_user_info, (tel, pw))
        existing_user_info = curs.fetchone()

        if not existing_user_info:
            return {'msg': 'invalid_account'}, 401

        return existing_user_info, 200
