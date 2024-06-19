from sanic import Sanic

from .config import get_config

from . import blueprints


def create_app(env):
    app = Sanic(__name__)
    config = get_config(env)
    app.update_config(config)
    
    app.config.OAS_URL_PREFIX = "/docs"
    
    app.blueprint(blueprints.auth.bp, url_prefix='/auth/')
    app.blueprint(blueprints.hello.bp, url_prefix='/api/')

    return app
