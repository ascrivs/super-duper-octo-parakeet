from app import db
from uuid import uuid4


class Drug(db.Model):
    __tablename__ = 'drugs'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    ndc = db.Column(db.Integer, unique=True, index=True)
    name = db.Column(db.String(128))
    strength = db.Column(db.String(64))


class Location(db.Model):
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, index=True)
    address = db.Column(db.Integer, db.ForeignKey('addresses.id'))

    addresses = db.relationship('Address', backref='addresses')

class Address(db.Model):
    __tablename__ = 'addresses'

    id = db.Column(db.Integer, primary_key=True)
    address_line_one = db.Column(db.String(128))
    address_line_two = db.Column(db.String(32))
    post_code = db.Column(db.Integer)
    city = db.String(db.String(128))
    state = db.String(db.String(128))


class Manufacturer(db.Model):

    __tablename__ = 'manufacturers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True)
    address = db.Column(db.Integer, db.ForeignKey('addresses.id'))

    addresses = db.relationship('Address', backref='addresses')
