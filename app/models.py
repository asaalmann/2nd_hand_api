from app import db


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

