from sanic import Sanic

from .config import get_config
from .routes import setup_routes

from . import blueprints


def create_app(env):
    app = Sanic(__name__)
    config = get_config(env)
    app.update_config(config)
    
    app.blueprint(blueprints.auth.bp, url_prefix='/auth/')
    app.blueprint(blueprints.hello.bp, url_prefix='/api/')

    return app
