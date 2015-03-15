from __future__ import absolute_import

from webapp.extensions import db


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)


class Tweet(db.Model):
    __tablename__ = "tweet"

    id = db.Column(db.Integer, primary_key=True)


class Employee(User):
    __tablename__ = "employee"

    id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
