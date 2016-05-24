from flask import Blueprint

bp = Blueprint(__name__, 'admin')


@bp.route("/admin")
def admin_home():
    return "Home admin"


@bp.route("/admin/user/add")
def user_add():
    return "user add"


@bp.route("/admin/user/add", methods=["POST"])
def user_add_post():
    # todo action add
    return "add success"


@bp.route("/admin/user/update")
def user_update():
    return "user update"
