from flask import Flask
from flask_cors import CORS

from smk.router import bp_basic


def create_app():

    _app = Flask(__name__)

    CORS(_app, resources={
        r"/api/*": {"origin": "*"}
    })

    _app.register_blueprint(bp_basic)

    return _app
