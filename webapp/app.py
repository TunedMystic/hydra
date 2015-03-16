from __future__ import absolute_import

from flask import Flask

from webapp.utils import find_blueprints
from webapp.extensions import INSTALLED_EXTENSIONS


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
    configure_app(app)
    configure_extensions(app)
    configure_blueprints(app)

    return app


def configure_app(app):
    """
    Configure Flask application settings.
    """
    app.config.from_object("webapp.settings")


def configure_extensions(app):
    """
    Configure Flask Extensions.
    """

    for ext in INSTALLED_EXTENSIONS:
        ext.init_app(app)


def configure_blueprints(app):
    """
    Configure Flask Blueprints.
    """

    for blueprint in find_blueprints():
        app.register_blueprint(blueprint)
