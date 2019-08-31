from flask import Blueprint, request
from flask_restful import Api, Resource

from DB import curs, conn

api = Api(Blueprint(__name__, __name__))


@api.resource('/mypage')
class Mypage(Resource):
    def get(self):
        try:
            uuid = request.args['uuid']
        except KeyError or TypeError:
            return {'msg': 'valueless'}, 400

        query_select_user_info = 'select tel, name, profile_img, point, (select title, main_img, item_id from item where status = %s) from user where uuid = %s'
        curs.execute(query_select_user_info, uuid)
        user_info = curs.fetchone()

        return user_info

    def patch(self):
        try:
            uuid = request.json['uuid']
            pw = request.json['pw']
        except KeyError or TypeError:
            return {'msg': 'valueless'}, 400

        query_select_user_info = 'select pw from user where uuid = %s and pw = %s'
        curs.execute(query_select_user_info, (uuid, pw))

        if not curs.fetchone():
            return {'msg': 'invalid_pw'}, 403

        try:
            name = request.json['name']
        except KeyError or TypeError:
            name = None
        try:
            change_pw = request.json['change_pw']
        except KeyError or TypeError:
            change_pw = None
        try:
            profile_img = request.json['profile_img']
        except KeyError or TypeError:
            profile_img = None

        if not name and not change_pw and not profile_img:
            return {'msg': 'invalid_request'}, 400

        query_update_user_info = 'update user set '

        if name:
            query_update_user_info += f"name = '{name}', "

        if change_pw:
            query_update_user_info += f"change_pw = '{change_pw}', "

        if profile_img:
            query_update_user_info += f"profile_img = '{profile_img}', "

        query_update_user_info = query_update_user_info[:-2] + ' where uuid = %s'
        curs.execute(query_update_user_info, uuid)
        conn.commit()

        return {'msg': 'success'}, 200
