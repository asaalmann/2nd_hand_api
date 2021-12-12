from flask import Blueprint, make_response, jsonify, request
from app.models.users import User
from app.helper.errors import makeJsonError

users = Blueprint('users', __name__)


@users.route('/', methods=["POST"])
def createUser():
    user = User.fromJson(request.json)
    if user.isValid():
        user = user.save()
        return make_response(user.toJson(), 201)
    else:
        return make_response("bad", 400)

@users.route('/<userId>', methods=["GET"])
def getUser(userId):
    user = User.query.get(userId)
    try:
        return make_response(user.toJson(), 200)
    except:
        message = "An user with id {} does not exist."
        return make_response(makeJsonError(message.format(userId)), 404)

@users.route('/<userId>', methods=["PUT"])
def updateUser():
    return make_response(jsonify({"result": "ok"}), 200)

@users.route('/<userId>', methods=["DELETE"])
def destroyUser():
    return make_response(jsonify({"result": "ok"}), 200)
