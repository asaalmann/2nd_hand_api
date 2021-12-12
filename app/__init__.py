from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.models import db, bcrypt
from app.views.users import users
from app.views.items import items
from app.views.healthcheck import healthcheck
from app.views.auth import auth

app = Flask(__name__)
db.init_app(app)
bcrypt.init_app(app)
app.register_blueprint(users, url_prefix='/users')
app.register_blueprint(items, url_prefix='/items')
app.register_blueprint(auth)
app.register_blueprint(healthcheck, url_prefix='/healthcheck')

app.config['JSON_SORT_KEYS'] = False
app.config['SECRET_KEY'] = '1429e65af740e874fa14a7a492ed94f9dba68afd9e554975'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://admin:start#123@localhost:5432/second_hand_api_db"