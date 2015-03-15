from flask.blueprints import Blueprint
from flask import render_template

wire_kwargs = {
    "name": "wire",
    "import_name": __name__,
    "url_prefix": "/w"
}
wire = Blueprint(**wire_kwargs)


@wire.route("/", methods=["GET"])
def index():
    return render_template("base/index.html")
