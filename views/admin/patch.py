from flask import Blueprint, request
from flask_restful import Api, Resource

from DB import curs, conn

api = Api(Blueprint(__name__, __name__))
api.prefix = '/admin'


@api.resource('/patch')
class Patch(Resource):
    def patch(self):
        try:
            permission = request.json['permission']
            item_id = request.json['item_id']
        except KeyError or TypeError:
            return {'msg': 'valueless'}, 400

        if permission != 9:
            return {'msg': 'permission_denied'}, 403

        query_select_item_info = 'select point, status from item where item_id = %s'
        curs.execute(query_select_item_info, item_id)
        point = curs.fetchone()['point']
        uuid = curs.fetchone()['status']

        query_select_user_info = 'select point from user where uuid = %s'
        curs.execute(query_select_user_info, uuid)
        existing_point = curs.fetchone()['point']

        if point > existing_point:
            return {'msg': 'low_point'}, 403

        query_update_item_info = 'update item set status = -1 where item_id = %s'
        curs.execute(query_update_item_info, item_id)

        conn.commit()

        return {'msg': 'success'}, 200
