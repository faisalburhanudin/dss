from dss.models import db


class Gpu(db.Model):

    type = db.Column(db.String(50), primary_key=True)

    memory = db.Column(db.Integer)

    speed = db.Column(db.Integer)

    def __init__(self, type, memory, speed):
        self.type = type
        self.memory = memory
        self.speed = speed
