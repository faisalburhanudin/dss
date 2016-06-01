from flask import Blueprint, render_template, request
from dss.models import Cpu, db

bp = Blueprint(__name__, "admin_cpu")


@bp.route("/admin/cpu")
def cpu():
    """List cpu"""
    cpus = Cpu.query.all()
    return render_template("admin/cpu.html", cpus=cpus)


@bp.route("/admin/cpu/add")
def cpu_add():
    """Form add cpu"""
    return render_template("admin/cpu_add.html")


@bp.route("/admin/cpu/add", methods=["POST"])
def cpu_add_action():
    """Action save cpu"""
    typ = request.form.get("type")
    core = request.form.get("core")
    speed = request.form.get("speed")
    cache = request.form.get("cache")

    cpu = Cpu(typ, core, speed, cache)
    db.session.add(cpu)
    db.session.commit()

    return render_template("admin/message.html", message="CPU berhasil ditambahkan")


@bp.route("/admin/cpu/update/<typ>")
def cpu_update(typ):
    """Form update cpu"""
    cpu = Cpu.query.filter_by(type=typ).first()
    return render_template("admin/cpu_update.html",
                           type=typ,
                           core=cpu.core,
                           speed=cpu.speed,
                           cache=cpu.cache)


@bp.route("/admin/cpu/update/<typ>", methods=["POST"])
def cpu_update_action(typ):
    """Action update cpu"""
    core = request.form.get("core")
    speed = request.form.get("speed")
    cache = request.form.get("cache")

    cpu = Cpu.query.filter_by(type=typ).first()
    cpu.core = core
    cpu.speed = speed
    cpu.cache = cache
    db.session.add(cpu)
    db.session.commit()

    return "CPU berhasil di update"


@bp.route("/admin/cpu/delete/<typ>")
def cpu_delete_action(typ):
    """Actionn delete cpu"""
    cpu = Cpu.query.filter_by(type=typ).first()
    db.session.delete(cpu)
    db.session.commit()

    return "CPU berhasil di delete"
