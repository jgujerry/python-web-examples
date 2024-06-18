from sanic import Sanic

from .config import get_config
from .routes import setup_routes


def create_app(env):
    app = Sanic(__name__)
    config = get_config(env)
    app.config.from_object(config)

    setup_routes(app)

    return app
