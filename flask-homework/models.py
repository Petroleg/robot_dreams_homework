from datetime import datetime

from app import db, app


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    age = db.Column(db.Integer)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    author = db.Column(db.String())
    year = db.Column(db.Integer)
    price = db.Column(db.Integer)


class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    date = db.Column(db.String(), default=datetime.utcnow)

    user = db.relationship('User', backref=db.backref('purchases', lazy=True))
    book = db.relationship('Book', backref=db.backref('purchases', lazy=True))
