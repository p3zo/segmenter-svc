import os

from flask import Flask
from flask_cors import CORS

APP_NAME = "segmenter"

THIS_DIR = os.path.dirname(os.path.realpath(__file__))

def create_app():

    app = Flask(__name__)
    app.title = APP_NAME

    with app.app_context():
        from .routes import bp

        app.register_blueprint(bp)

    CORS(app)

    return app
