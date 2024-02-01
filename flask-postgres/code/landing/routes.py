from flask import Blueprint, render_template

bp = Blueprint("landing", __name__, template_folder="./templates")


@bp.route("/", methods=["GET"])
def home():
    return render_template("index.html")
