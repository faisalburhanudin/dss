from dss.models import db


class Computer(db.Model):

    type = db.Column(db.String(50), primary_key=True)

    price = db.Column(db.Integer)

    cpu_id = db.Column(db.String(50))

    gpu_id = db.Column(db.String(50))

    ram = db.Column(db.Integer)

    harddisk = db.Column(db.Integer)

    monitor = db.Column(db.Integer)
