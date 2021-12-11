from . import db
from flask import request

class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    price = db.Column(db.Integer)
    city = db.Column(db.String)

    def __init__(self, title, description, price, city):
        self.title = title
        self.description = description
        self.price = price
        self.city = city

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def isValid(self):
        if not (self.title and self.description and self.price and self.city):
            return False
        else:
            return True

    @staticmethod
    def fromJson(json):
        return Item(json['title'], json['description'], json['price'], json['city'])

    def save(self):
        db.session.add(self)
        db.session.flush()
        db.session.refresh(self)
        db.session.commit()
        return self


    @staticmethod
    def filterByParams(params):
        city = params.get('city')
        max_price = params.get('max_price')
        if city and max_price:
            return Item.query.filter(Item.city == city).filter(Item.price <= max_price)
        elif city:
            return Item.query.filter(Item.city == city)
        elif max_price:
            return Item.query.filter(Item.price <= max_price)
        else:
            return Item.query.all()

