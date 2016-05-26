from flask import Blueprint, render_template

bp = Blueprint(__name__, 'frontend')


@bp.route("/")
def home():
    return render_template("index.html")
