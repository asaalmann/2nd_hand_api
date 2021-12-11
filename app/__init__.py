from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.models import db
from app.views.users import users
from app.views.items import items
from app.views.healthcheck import healthcheck

app = Flask(__name__)
db.init_app(app)
app.register_blueprint(users, url_prefix='/users')
app.register_blueprint(items, url_prefix='/items')
app.register_blueprint(healthcheck, url_prefix='/healthcheck')

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://admin:start#123@localhost:5432/second_hand_api_db"