import os

from quart import Quart

from api.config import AppConfig
from api.routes import blueprint


def create_app():
    """Create Quart app with configuration"""
    app = Quart(__name__)

    app.config.from_object(AppConfig)

    app.register_blueprint(blueprint)

    return app
