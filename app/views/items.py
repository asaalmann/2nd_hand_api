from flask import Blueprint, make_response, jsonify, request

from app.models.items import Item

items = Blueprint('items', __name__)


@items.route("/", methods=["GET"])
def getItems():
    items = Item.filterByParams(request.args)
    result = [
        {
            "id": item.id,
            "title": item.title,
            "price": item.price
        } for item in items]
    return make_response(jsonify(result), 200)

@items.route("/", methods=["POST"])
def createItem():
    item = Item.fromJson(request.json)
    if item.isValid():
        item = item.save()
        return make_response("new id is " + str(item.id), 201)
    else:
        return make_response("bad", 400)


@items.route("/<itemId>", methods=["GET"])
def getItem(itemId):
    item = Item.query.get(itemId)
    result = {
        "id": item.id,
        "title": item.title,
        "price": item.price,
        "description": item.description
    }
    return make_response(jsonify(result), 200)
