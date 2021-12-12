from . import db, bcrypt
from flask import request, jsonify, current_app
import jwt
from datetime import datetime, timedelta, timezone

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    password = db.Column(db.String)
    first_name = db.Column(db.String)
    family_name = db.Column(db.String)
    city = db.Column(db.String)

    def __init__(self, email, password, first_name, family_name, city):
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
        self.first_name = first_name
        self.family_name = family_name
        self.city = city

    def __repr__(self):
        return '<id: {}, email:{}>'.format(self.id, self.email)

    def isValid(self):
        return self.nothingMissing() and self.hasUniqueEmail()

    def nothingMissing(self):
        return self.email and self.password and self.first_name and self.family_name and self.city

    def hasUniqueEmail(self):
        return User.query.filter(User.email == self.email).count() == 0

    @staticmethod
    def fromJson(json):
        return User(json['email'], json['password'], json['first_name'], json['family_name'], json['city'])

    def prepareForJson(self):
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "family_name": self.family_name,
            "city": self.city
        }

    def toJson(self):
        return jsonify(self.prepareForJson())

    def save(self):
        db.session.add(self)
        db.session.flush()
        db.session.refresh(self)
        db.session.commit()
        return self

    @staticmethod
    def verifyLoginData(json):
        try:
            email = json['email']
            password = json['password']
        except:
            return None

        user = User.query.filter(User.email == email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            return user
        else:
            return None

    def createAccessToken(self):
        expire = datetime.now(timezone.utc) + timedelta(hours=1)
        payload = dict(exp=expire, sub=self.id)
        return jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256')

    def createLoginResponse(self):
        response = {
            "user": self.prepareForJson(),
            "token": self.createAccessToken()
        }
        return jsonify(response)

    @staticmethod
    def evaluateAccessToken(token):
        return jwt.decode(token, current_app.config['SECRET_KEY'], algorithms='HS256')