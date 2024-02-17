from quart import Blueprint, render_template

blueprint = Blueprint("app", __name__)


@blueprint.route("/")
async def index():
    return await render_template("index.html")
