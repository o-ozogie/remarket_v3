from flask import Flask
from flask_cors import CORS

from views.route import Route


def create_app(*configs):
    app_ = Flask(__name__)

    for config in configs:
        app_.config.from_object(config)

    CORS(app_, resources={
        r"*": {'origin': '*'},
    })

    Route().route(app_)

    return app_
