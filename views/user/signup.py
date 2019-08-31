from flask import Blueprint, request
from flask_restful import Api, Resource

from DB import curs, conn
from static.static import BASIC_PROFILE_IMAGE

api = Api(Blueprint(__name__, __name__))


@api.resource('/signup')
class Signup(Resource):
    def post(self):
        try:
            tel = request.json['tel']
            pw = request.json['pw']
            name = request.json['name']
        except KeyError or TypeError:
            return {'msg': 'valueless'}, 400

        query_select_user_info = 'select uuid from user where tel = %s'
        curs.execute(query_select_user_info, tel)
        existing_user = curs.fetchone()

        if existing_user:
            return {'msg': 'existing_user'}, 403

        query_insert_user_info = 'insert into user (tel, pw, name, profile_img) values(%s, %s, %s, %s)'
        curs.execute(query_insert_user_info, (tel, pw, name, BASIC_PROFILE_IMAGE))
        conn.commit()

        return {'msg': 'success'}, 200
