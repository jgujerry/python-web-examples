from quart import Quart

from app.config import AppConfig
from app.routes import blueprint


def create_app():
    """Create Quart app with configuration"""
    app = Quart(__name__, static_folder="./static", template_folder="./templates")

    app.config.from_object(AppConfig)

    app.register_blueprint(blueprint)

    return app
