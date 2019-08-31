import datetime

from flask import Blueprint, request
from flask_restful import Api, Resource

from DB import curs, conn

api = Api(Blueprint(__name__, __name__))
api.prefix = '/admin'


@api.resource('/upload')
class Upload(Resource):
    def post(self):
        try:
            uuid = request.json['uuid']
            title = request.json['title']
            cate = request.json['cate']
            loc = request.json['loc']
            point = request.json['point']
            main_img = request.json['main_img']
            buy_time = request.json['buy_time']
            permission = request.json['permission']

        except KeyError or TypeError:
            return {'msg': 'valueless'}, 400

        buy_time = datetime.datetime.strptime(buy_time, '%Y-%m-%d')

        if permission != 9:
            return {'msg': 'permission_denied'}, 403

        query_insert_item_info = 'insert into item (uuid, title, cate, loc, point, main_img, buy_time, write_time) ' \
                                 f"values ({uuid}, '{title}', '{cate}', '{loc}', {point}, '{main_img}', '{buy_time}', '{datetime.datetime.now()}')"
        curs.execute(query_insert_item_info)

        query_update_user_info = f'update user set point = point + {point} where uuid = {uuid}'
        curs.execute(query_update_user_info)

        conn.commit()

        return {'msg': 'success'}, 200
