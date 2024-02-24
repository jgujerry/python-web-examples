from typing import List

from quart import Blueprint, jsonify, request
from quart_schema import validate_request, validate_response

from .models import User, Team

blueprint = Blueprint("app", __name__)


@blueprint.route("/", methods=["GET"])
async def index():
    return {"Hello": "I am a Simple REST API built with Quart!"}


@blueprint.route("/list", methods=["GET"])
async def list():
    return jsonify(["a", "c", "c", "d", "e", "f", "g"])


@blueprint.route("/user", methods=["GET"])
@validate_response(User)
async def user():
    return {"username": "user1", "email": "user1@example.com"}


@blueprint.route("/team", methods=["GET"])
@validate_response(Team)
async def team():
    u1 = {"username": "user1", "email": "user1@example"}
    u2 = {"username": 2, "email": "user2@example"}
    return {"users": [u1, u2]}


@blueprint.route("/users", methods=["POST"])
@validate_request(User)
async def users(data: User):
    return jsonify({"message": "Users data validation is successful.", "user": data})
