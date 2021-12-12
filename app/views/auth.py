from flask import Blueprint, make_response, jsonify, request
from app.models.users import User
from app.helper.errors import makeJsonError
import jwt


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=["POST"])
def createToken():
    user = User.verifyLoginData(request.json)
    if user:
        return make_response(user.createLoginResponse(), 201)
    else:
        return make_response("bad", 400)


@auth.route('/check', methods=["GET"])
def check():
    token = request.headers.get("Authorization")
    payload = User.evaluateAccessToken(token)
    return make_response(jsonify(payload), 200)