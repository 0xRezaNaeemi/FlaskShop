from sqlalchemy import *
from extentions import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False, index=True)
    password = db.Column(db.String, nullable=False, index=True)
    email = db.Column(db.String, nullable=False, index=True)
    phone = db.Column(db.String(11), nullable=False, index=True)
    address = db.Column(db.String, nullable=False, index=True)

    # independence from db and use from sqlalchemy directly
    # id = Column(Integer, primary_key=True)
    # username = Column(String, unique=True, nullable=False)
    # email = Column(String)
