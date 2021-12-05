from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://admin:start#123@2nd_hand_api_db:5432/second_hand_api_db"
db = SQLAlchemy(app)

from app import views
from app import models