from flask import Blueprint, render_template

from app.models.items import Item

healthcheck = Blueprint('healthcheck', __name__)


@healthcheck.route("/")
def index():
    item_count = Item.query.count()
    return render_template("healthcheck.html", item_count=item_count)
