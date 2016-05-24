from dss.models import db


class Administrator(db.Model):

    id = db.Column(db.Integer)

    username = db.Column(db.String(50))

    status = db.Column(db.Integer)

    password = db.Column(db.String(100))
