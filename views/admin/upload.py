from flask import Blueprint, request
from flask_restful import Api, Resource
import time

from DB import curs, conn

api = Api(Blueprint(__name__, __name__))


@api.resource('/upload')
class Upload(Resource):
    def post(self):
        try:
            uuid = request.json['uuid']
            title = request.json['title']
            cate = request.json['cate']
            loc = request.json['loc']
            main_img = request.json['main_img']
            buy_time = request.json['buy_time']
            permission = request.json['permission']
        except KeyError or TypeError:
            return {'msg': 'valueless'}, 400

        if permission != 9:
            return {'msg': 'permission_denied'}, 403

        buy_time = time.mktime(time.strftime(buy_time, '%Y-%m-%d'))

        query_insert_item_info = 'insert into item (uuid, title, cate, loc, main_img, buy_time, write_time) ' \
                                 'values (%s, %s, %s, %s, %s, %s, )'
        curs.execute(query_insert_item_info, (uuid, title, cate, loc, main_img, buy_time, time.time()))
        conn.commit()

        return {'msg': 'success'}, 200