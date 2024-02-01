# manage.py
from flask.cli import FlaskGroup
from flask_migrate import Migrate
from app import create_app, db

app = create_app()

migrate = Migrate(app, db)
cli = FlaskGroup(app)


if __name__ == "__main__":
    cli()
