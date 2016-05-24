from dss.models import db


class Cpu(db.Model):

    type = db.Column(db.String(50))

    core = db.Column(db.Integer)

    speed = db.Column(db.Integer)

    cache = db.Column(db.Integer)