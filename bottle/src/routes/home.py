from pathlib import Path
from bottle import Bottle, template, static_file


home_router = Bottle()
static_root = str(Path(__file__).parent.parent.joinpath("static"))
print("================================================", static_root)


@home_router.route("/")
def index():
    return template("index.html")


@home_router.route("/static/<filename:path>")
def serve_static(filename):
    return static_file(filename, root=static_root)
