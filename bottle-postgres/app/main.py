import pathlib

from bottle import route, template, run, static_file
from sqlalchemy import text

from db import pg_engine


BASE_DIR = pathlib.Path(__file__).parents[1]
STATIC_ROOT = str(BASE_DIR.joinpath("static"))


@route('/static/<path:path>')
def static(path):
    return static_file(path, root=STATIC_ROOT)


@route("/")
def home():
    
    # RAW Sqlalchemy query
    databases = []
    with pg_engine.connect() as conn:
        result = conn.execute(text("SELECT datname FROM pg_database;"))
        for row in result.fetchall():
            databases.append(row[0])
    
    context = {"databases": databases}
    
    return template("home.tpl", **context)


run(host="0.0.0.0", port=8080, debug=True, reloader=True)
