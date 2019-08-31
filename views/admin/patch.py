from flask import Blueprint, request
from flask_restful import Api, Resource

from DB import curs, conn

api = Api(Blueprint(__name__, __name__))


@api.resource('/patch')
class Patch(Resource):
    def 