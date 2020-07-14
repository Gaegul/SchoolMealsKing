from flask import Blueprint
from flask_restful import Api

bp_basic = Blueprint("auth", __name__, url_prefix="/api/v1")
api_basic = Api(bp_basic)

from smk.view.parsing import Parsing
api_basic.add_resource(Parsing, '/parsing')

from smk.view.meal import Meal
api_basic.add_resource(Meal, '/meal')
