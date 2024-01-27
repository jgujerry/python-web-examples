from flask import Blueprint, jsonify, request
from sqlalchemy import exc

from .exts import db
from .models import User

bp = Blueprint("users", __name__)


@bp.route("/users/ping", methods=["GET"])
def ping():
    return jsonify({
        "status": "success",
        "message": "pong"
    })


@bp.route("/users", methods=["POST"])
def add_user():
    post_data = request.get_json()
    response_object = {
        "status": "fail",
        "message": "Invalid payload."
    }
    if not post_data:
        return jsonify(response_object), 400
    
    username = post_data.get("username", None)
    email = post_data.get("email", None)
    if not username or not email:
        return jsonify(response_object), 400
    
    try:
        user = User.query.filter_by(email=email).first()
        if not user:
    
            db.session.add(User(username=username, email=email))
            db.session.commit()
            response_object["status"] = "success"
            response_object["message"] = f"{username} was added successfully"
            return jsonify(response_object), 201
        else:
            response_object['message'] = f"This email '{email}' already exists."
            return jsonify(response_object), 400
    except exc.IntegrityError as e:
        db.session.rollback()
        return jsonify(response_object), 400


@bp.route("/users/<user_id>", methods=["GET"])
def get_single_user(user_id):
    response_object = {
        "status": "fail",
        "message": "User does not exist"
    }
    try:
        user = User.query.filter_by(id=user_id).first()
        if not user:
            return jsonify(response_object), 404
        else:
            response_object = {
                "status": "success",
                "data": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "active": user.active
                }
            }
            return jsonify(response_object), 200
    except exc.DataError:
        return jsonify(response_object), 404


@bp.route("/users", methods=["GET"])
def get_all_users():
    response_object = {
        "status": "success",
        "data": {
            "users": [user.to_json() for user in User.query.all()]
        }
    }
    return jsonify(response_object), 200
