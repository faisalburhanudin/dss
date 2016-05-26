from dss.models import Administrator, db
from flask import Blueprint, render_template, request

bp = Blueprint(__name__, 'admin_user')


@bp.route("/admin/user")
def user_home():
    """Return user list table"""
    return "user list"


@bp.route("/admin/user/add")
def user_add():
    """Form add user"""
    return render_template("admin/user_add.html")


@bp.route("/admin/user/add", methods=["POST"])
def user_add_post():
    """Action add user"""
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


@bp.route("/admin/user/update/<int:user_id>")
def user_update(user_id):
    """Form update user"""
    administrator = Administrator.query.filter_by(id=user_id).first()

    return render_template(
        "admin/user_update.html",
        admin_id=administrator.id,
        username=administrator.username,
        status=administrator.status,
        password=administrator.password
    )


@bp.route("/admin/user/update/<int:user_id>", methods=["POST"])
def user_update_action(user_id):
    """action update user"""
    username = request.form.get("username")
    status = request.form.get("status")
    password = request.form.get("password")

    administrator = Administrator.query.filter_by(id=user_id).first()
    administrator.username = username
    administrator.status = status
    administrator.password = password

    db.session.add(administrator)
    db.session.commit()

    return "User berhasil diupdate"


@bp.route("/admin/user/delete/<int:user_id>")
def user_delete(user_id):
    """Action delete user"""
    administrator = Administrator.query.filter_by(id=user_id).first()
    db.session.delete(administrator)
    db.session.commit()

    return "User berhasil dihapus"
