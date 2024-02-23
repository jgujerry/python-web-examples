from flask import Flask
from flask_migrate import Migrate

from app.config import AppConfig
from app.db import db
from app.portal.routes import blueprint as portal_blueprint

migrate = Migrate()


def create_app():
    """Create a Flask app"""
    app = Flask(__name__)
    
    # config based on environment
    app.config.from_object(AppConfig)
    
    # db
    db.init_app(app)
    migrate.init_app(app, db)

    # blueprint
    app.register_blueprint(portal_blueprint)
    
    return app
