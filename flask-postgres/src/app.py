from flask import Flask

from landing.routes import bp as landing_bp


def create_app():
    """Create a Flask app"""
    flask_app = Flask(__name__)

    with flask_app.app_context():
        flask_app.config.from_object("config.DevelopmentConfig")
        
    flask_app.register_blueprint(landing_bp)

    return flask_app
