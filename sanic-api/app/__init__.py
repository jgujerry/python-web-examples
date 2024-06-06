from sanic import Sanic
import os

def create_app():
    app = Sanic(__name__)

    # Determine which configuration to use
    env = os.getenv('SANIC_ENV', 'development')

    if env == 'production':
        from app.config.production import ProductionConfig
        app.config.from_object(ProductionConfig)
    else:
        from app.config.development import DevelopmentConfig
        app.config.from_object(DevelopmentConfig)

    from app.routes import init_routes
    from app.utils.db import init_db

    init_db(app)
    init_routes(app)

    return app
