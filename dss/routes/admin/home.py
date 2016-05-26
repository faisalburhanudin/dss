from flask import Blueprint, render_template

bp = Blueprint(__name__, 'admin')


@bp.route("/admin")
def admin_home():
    """Administration home"""
    return render_template("admin/index.html")
