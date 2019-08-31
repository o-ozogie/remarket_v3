from flask import Blueprint, request
from flask_restful import Api, Resource

from DB import curs, conn

api = Api(Blueprint(__name__, __name__))


@api.resource('/update')
class Update(Resource):
    def update(self):
        try:
            uuid = request.args['uuid']
            item_id = request.args['item_id']
        except KeyError or TypeError:
            return {'msg': 'valueless'}, 400

        query_update_item_info = 'update item set status = %s where item_id = %s'
        curs.execute(query_update_item_info, (uuid, item_id))
        conn.commit()

        return {'msg': 'success'}, 200
