from app import app

from flask import render_template, make_response, jsonify, request

from app.models import Item


@app.route("/healthcheck")
def index():
    item_count = Item.query.count()
    return render_template("healthcheck.html", item_count=item_count)


@app.route("/items", methods=["GET"])
def getItems():
    max_price = request.args.get('max_price')
    if max_price:
        items = Item.query.filter(Item.price <= max_price)
    else:
        items = Item.query.all()
    result = [
        {
            "id": item.id,
            "title": item.title,
            "price": item.price
        } for item in items]
    return make_response(jsonify(result), 200)


@app.route("/items/<itemId>", methods=["GET"])
def getItem(itemId):
    item = Item.query.get(itemId)
    result = {
        "id": item.id,
        "title": item.title,
        "price": item.price,
        "description": item.description
    }
    return make_response(jsonify(result), 200)
