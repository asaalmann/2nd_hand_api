from flask import Blueprint, make_response, jsonify

users = Blueprint('users', __name__)


@users.route('/', methods=["GET"])
def getUsers():
    return make_response(jsonify({"result": "ok"}), 200)
