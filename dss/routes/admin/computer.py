from flask import Blueprint, render_template, request
from dss.models import Computer, db

bp = Blueprint(__name__, "admin_computer")


@bp.route("/admin/computer")
def computer_list():
    """List computer"""
    computers = Computer.query.all()
    return render_template("admin/computer.html", computers=computers)


@bp.route("/admin/computer/add")
def computer_add():
    """Form add computer"""
    return render_template("admin/computer_add.html")


@bp.route("/admin/computer/add", methods=["POST"])
def computer_add_action():
    """Action save computer"""
    typ = request.form.get("type")
    price = request.form.get("price")
    cpu_id = request.form.get("cpu_id")
    gpu_id = request.form.get("gpu_id")
    ram = request.form.get("ram")
    harddisk = request.form.get("harddisk")
    monitor = request.form.get("monitor")

    computer = Computer(typ, price, cpu_id, gpu_id, ram, harddisk, monitor)
    db.session.add(computer)
    db.session.commit()

    return render_template("admin/message.html", message="Computer berhasil ditambahkan")


@bp.route("/admin/computer/update/<typ>")
def computer_update(typ):
    """Form update computer"""
    computer = Computer.query.filter_by(type=typ).first()
    return render_template("admin/computer_update.html",
                           type=typ,
                           price=computer.price,
                           cpu_id=computer.cpu_id,
                           gpu_id=computer.gpu_id,
                           ram=computer.ram,
                           harddisk=computer.harddisk,
                           monitor=computer.monitor)


@bp.route("/admin/computer/update/<typ>", methods=["POST"])
def computer_update_action(typ):
    """Action update computer"""
    price = request.form.get("price")
    cpu_id = request.form.get("cpu_id")
    gpu_id = request.form.get("gpu_id")
    ram = request.form.get("ram")
    harddisk = request.form.get("harddisk")
    monitor = request.form.get("monitor")

    computer = Computer.query.filter_by(type=typ).first()
    computer.price = price
    computer.cpu_id = cpu_id
    computer.gpu_id = gpu_id
    computer.ram = ram
    computer.harddisk = harddisk
    computer.monitor = monitor
    db.session.add(computer)
    db.session.commit()

    return "Computer berhasil di update"


@bp.route("/admin/computer/delete/<typ>")
def computer_delete_action(typ):
    """Actionn delete computer"""
    computer = Computer.query.filter_by(type=typ).first()
    db.session.delete(computer)
    db.session.commit()

    return "Computer berhasil di delete"
