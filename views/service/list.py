from flask import Blueprint, request
from flask_restful import Api, Resource

from DB import curs

api = Api(Blueprint(__name__, __name__))


@api.resource('/list')
class List(Resource):
    def get(self):
        try:
            title = request.args['title']
        except KeyError or TypeError:
            return {'msg': 'valueless'}, 400

        query_select_item_info = 'select item_id, uuid as u, (select name from user where uuid = u), ' \
                                 'title, cate, loc, main_img, buy_time, write_time, status, point' \
                                 f" from item where title like '%{title}%' or cate like '%{title}%' order by item_id desc"
        curs.execute(query_select_item_info)
        item_infos = curs.fetchall()

        refined_info = {}
        cnt = 0

        for item_info in item_infos:
            refined_info[cnt] = item_info
            cnt += 1

        return refined_info
