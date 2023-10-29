from extentions import db


class Product(db.Model):
    __tablename__ = "product"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False, index=True)
    description = db.Column(db.String, nullable=False, index=True)
    price = db.Column(db.Integer, nullable=False, index=True)
    active = db.Column(db.Integer, nullable=False, index=True)
