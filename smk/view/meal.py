from flask_restful import Resource
from flask import request

from smk.controller.meal import get_meal


class Meal(Resource):

    def get(self):
        date = request.args['date']

        return get_meal(date)
