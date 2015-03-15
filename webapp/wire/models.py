from __future__ import absolute_import

from webapp.extensions import db


class Battery(db.Model):
    __tablename__ = "battery"

    id = db.Column(db.Integer, primary_key=True)


class Wire(db.Model):
    __tablename__ = "wire"

    id = db.Column(db.Integer, primary_key=True)
