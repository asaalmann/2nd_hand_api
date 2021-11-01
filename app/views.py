from app import app

from flask import render_template


@app.route("/healthcheck")
def index():
    user_count = 0
    item_count = 0
    return render_template("healthcheck.html", user_count=user_count, item_count=item_count)
