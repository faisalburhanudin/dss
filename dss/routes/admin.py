from flask import Blueprint, render_template

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
    # todo action add
    return "add success"


@bp.route("/admin/user/update")
def user_update():
    return "user update"


@bp.route("/admin/user/update", methods=["POST"])
def user_update_action():
    return  "action user update"