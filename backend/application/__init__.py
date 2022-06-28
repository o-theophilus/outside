from flask import Flask
from flask_cors import CORS

from .api import bp as api
from .api.photo import bp as photo
from .api.nft import bp as nft


def create_app(config_file="config.py"):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    CORS(app)

    app.register_blueprint(api)
    app.register_blueprint(photo)
    app.register_blueprint(nft)

    return app
