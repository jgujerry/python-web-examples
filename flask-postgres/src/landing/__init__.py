import os
from flask import Flask

from .exts import db
from .routes import bp


def create_app(script_info=None):
    
    # instantiate the app
    app = Flask(__name__)
    
    # set config
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)
    
    # set up extensions
    db.init_app(app)
    
    # register blueprints
    app.register_blueprint(bp)
    
    # shell context for flask cli
    app.shell_context_processor({"app": app, "db": db})
    
    return app
