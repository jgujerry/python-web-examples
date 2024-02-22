import os

from flask import Flask
from flask_migrate import Migrate


from app.config import get_config
from app.db import db
from app.portal.routes import blueprint as portal_blueprint

migrate = Migrate()


def create_app():
    """Create a Flask app"""
    app = Flask(__name__)
    
    # config based on environment
    env = os.environ.get("ENVIRONMENT", "development")
    config = get_config(env)
    app.config.from_object(config)
    
    # db
    db.init_app(app)
    migrate.init_app(app, db)

    # blueprint
    app.register_blueprint(portal_blueprint)
    
    return app
