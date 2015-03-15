from flask.blueprints import Blueprint
from flask import render_template

base_kwargs = {
    "name": "base",
    "import_name": __name__,
    "url_prefix": "/b"
}
base = Blueprint(**base_kwargs)


@base.route("/", methods=["GET"])
def index():
    return render_template("base/index.html")
