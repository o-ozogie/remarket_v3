from flask import Blueprint, request
from flask_restful import Api, Resource

from DB import curs, conn

api = Api(Blueprint(__name__, __name__))


@api.resource('/update')
class Update(Resource):
    def post(self):
        try:
            uuid = request.json['uuid']
            item_id = request.json['item_id']
        except KeyError or TypeError:
            return {'msg': 'valueless'}, 400

        query_select_user_info = 'select point from user where uuid = %s'
        curs.execute(query_select_user_info, uuid)
        point = curs.fetchone()['point']

        query_select_item_info = 'select point from item where item_id = %s'
        curs.execute(query_select_item_info, item_id)
        item_point = curs.fetchone()['point']

        if point < item_point:
            return {'msg': 'low_point'}, 403

        query_update_user_point = 'update user set point = point - %s where uuid = %s'
        curs.execute(query_update_user_point, (item_point, uuid))

        query_update_item_info = 'update item set status = %s where item_id = %s'
        curs.execute(query_update_item_info, (uuid, item_id))
        conn.commit()

        return {'msg': 'success'}, 200
