from flask import Blueprint, render_template, request
from dss.models import Administrator, db

bp = Blueprint(__name__, 'admin')


@bp.route("/admin")
def admin_home():
    return render_template("admin/index.html")


@bp.route("/admin/user")
def user_home():
    return "user list"


@bp.route("/admin/user/add")
def user_add():
    return render_template("admin/user_add.html")


@bp.route("/admin/user/add", methods=["POST"])
def user_add_post():
    username = request.form.get("username")
    status = request.form.get("status")
    password = request.form.get("password")

    administrator = Administrator(
        username=username,
        status=status,
        password=password
    )

    db.session.add(administrator)
    db.session.commit()

    return "User berhasil ditambahkan"


@bp.route("/admin/user/update")
def user_update():
    return "user update"


@bp.route("/admin/user/update", methods=["POST"])
def user_update_action():
    return  "action user update"