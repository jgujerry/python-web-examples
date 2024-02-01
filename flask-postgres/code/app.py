from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from landing.routes import bp as landing_bp

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    """Create a Flask app"""
    
    flask_app = Flask(__name__)

    with flask_app.app_context():
        flask_app.config.from_object("config.DevelopmentConfig")
        
    # db
    db.init_app(flask_app)
    migrate.init_app(flask_app, db)

    # blueprint
    flask_app.register_blueprint(landing_bp)
    
    flask_app.shell_context_processor({"app": flask_app, "db": db})

    return flask_app
