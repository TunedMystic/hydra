from __future__ import absolute_import

import os
from flask import Flask

from webapp import extensions as ext
from webapp.base import base


# Installed Extensions.
INSTALLED_EXTENSIONS = (
    # flask-sqlalchemy
    ext.db,
)

# Installed Blueprints.
INSTALLED_BLUEPRINTS = (
    base,
)


def create_app(app_name=None, config=None, blueprints=None):
    """
    Create a Flask app.
    """
    app_kwargs = {
        "import_name": __name__,
        # "static_url_path": "static",
        "static_folder": "client/static",
        "template_folder": "client/templates",
    }
    app = Flask(**app_kwargs)
    # App config from object...
    configure_app(app)
    configure_extensions(app)
    configure_blueprints(app)

    return app


def configure_app(app):
    """
    Configure Flask application settings.
    """
    pass


def configure_extensions(app):
    """
    Configure Flask Extensions.
    """

    # flask-sqlalchemy
    ext.db.init_app(app)


def configure_blueprints(app):
    """
    Configure Flask Blueprints.
    """

    for blueprint in INSTALLED_BLUEPRINTS:
        app.register_blueprint(blueprint)
