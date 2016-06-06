from flask_login import login_required
from flask import Blueprint, render_template

bp = Blueprint(__name__, 'admin')


@bp.route("/admin")
@login_required
def admin_home():
    """Administration home"""
    return render_template("admin/index.html")
