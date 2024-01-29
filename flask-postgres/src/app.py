from flask import Flask


def create_app(config=None, testing=False):
    """Create a Flask app"""
    flask_app = Flask(__name__)
    flask_app.secret_key = config.get("FLASK_APP_SECRET_KEY")

    with flask_app.app_context():
        flask_app.config.from_object(config)

    return flask_app
