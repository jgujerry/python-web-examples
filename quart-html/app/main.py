import os

from quart import Quart

from app.config import get_config
from app.routes import blueprint


env = os.getenv("QUART_ENV", "development")


def create_app(env):
    """Create Quart app with configuration"""
    app = Quart(__name__, static_folder="./static", template_folder="./templates")

    config = get_config(env)
    app.config.from_object(config)

    app.register_blueprint(blueprint)

    return app


app = create_app(env)
