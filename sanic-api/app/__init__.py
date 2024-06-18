from sanic import Sanic

from .config import get_config
from .routes import setup_routes


def create_app(env):
    app = Sanic(__name__)
    config = get_config(env)
    app.update_config(config)

    setup_routes(app)

    return app
