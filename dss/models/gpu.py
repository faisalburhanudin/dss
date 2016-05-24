from dss.models import db


class Gpu(db.Model):

    type = db.Column(db.String(50))

    memory = db.Column(db.Integer)

    speed = db.Column(db.Integer)