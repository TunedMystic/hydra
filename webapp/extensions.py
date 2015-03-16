from __future__ import absolute_import

from flask.ext.sqlalchemy import SQLAlchemy

# flask-sqlalchemy
db = SQLAlchemy()


INSTALLED_EXTENSIONS = (
    # flask-sqlalchemy
    db,
)
