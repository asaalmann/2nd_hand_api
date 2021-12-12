from flask import Blueprint, render_template

from app.models.items import Item
from app.models.users import User

healthcheck = Blueprint('healthcheck', __name__)


@healthcheck.route("/")
def index():
    item_count = Item.query.count()
    user_count = User.query.count()
    return render_template("healthcheck.html", user_count=user_count, item_count=item_count)

