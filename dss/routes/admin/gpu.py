from flask import Blueprint, render_template

bp = Blueprint(__name__, "admin_gpu")


@bp.route("/admin/gpu/add")
def gpu_add():
    return render_template("admin/gpu_add.html")
