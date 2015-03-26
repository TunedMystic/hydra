from __future__ import absolute_import

from webapp.extensions import db


class Author(db.Model):
    __tablename__ = "author"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    
    books = db.relationship("Book", backref="author")
    
    def __repr__(self):
      return "<Author {0}>".format(self.name[:24])


class Book(db.Model):
  __tablename__ = "book"
  
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(60), nullable=False)
  date_published = db.Column(db.DateTime)
  
  author_id = db.Column(db.Integer, db.ForeignKey("author.id"))
  
  def __init__(self, *args, **kwargs):
    print "args: {0}".format(args)
    print "kwargs: {0}".format(kwargs)
    super(Book, self).__init__(*args, **kwargs)
  
  def __repr__(self):
    return "<Book {0}>".format(self.title[:24])


'''
class Tweet(db.Model):
    __tablename__ = "tweet"

    id = db.Column(db.Integer, primary_key=True)


class Employee(User):
    __tablename__ = "employee"

    id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
'''
