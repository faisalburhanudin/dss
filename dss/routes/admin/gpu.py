from flask import Blueprint, render_template, request
from dss.models import Gpu, db

bp = Blueprint(__name__, "admin_gpu")


@bp.route("/admin/gpu/add")
def gpu_add():
    """Form add gpu"""
    return render_template("admin/gpu_add.html")


@bp.route("/admin/gpu/add", methods=["POST"])
def gpu_add_action():
    """Action save gpu"""
    typ = request.form.get("type")
    memory = request.form.get("memory")
    speed = request.form.get("speed")

    gpu = Gpu(typ, memory, speed)
    db.session.add(gpu)
    db.session.commit()

    return "GPU berhasil ditambahkan"


@bp.route("/admin/gpu/update/<typ>")
def gpu_update(typ):
    """Form update gpu"""
    gpu = Gpu.query.filter_by(type=typ).first()
    return render_template("admin/gpu_update.html",
                           type=typ,
                           memory=gpu.memory,
                           speed=gpu.speed)


@bp.route("/admin/gpu/update/<typ>", methods=["POST"])
def gpu_update_action(typ):
    """Action update gpu"""
    memory = request.form.get("memory")
    speed = request.form.get("speed")

    gpu = Gpu.query.filter_by(type=typ).first()
    gpu.memory = memory
    gpu.speed = speed
    db.session.add(gpu)
    db.session.commit()

    return "GPU berhasil di update"


@bp.route("/admin/gpu/delete/<typ>")
def gpu_delete_action(typ):
    """Actionn delete gpu"""
    gpu = Gpu.query.filter_by(type=typ).first()
    db.session.delete(gpu)
    db.session.commit()

    return "GPU berhasil di delete"
