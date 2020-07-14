from flask_restful import Resource
from flask import request

from smk.controller.parsing import parsing


class Parsing(Resource):

    def get(self):
        start_date = request.args['start_date']
        end_date = request.args['end_date']

        return parsing(start_date, end_date)
