import pathlib
from bottle import Bottle, run, static_file, template

app = Bottle()
BASE_DIR = pathlib.Path(__file__).parent
STATIC_ROOT = str(BASE_DIR.joinpath("static"))


@app.route('/static/<filename:path>')
def static(filename):
    return static_file(filename, root=STATIC_ROOT)


@app.route("/")
def home():
    context = {"title": "Bottle HTML", "name": "Sample App"}
    return template("index.html", **context)
