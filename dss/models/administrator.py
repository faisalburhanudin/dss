from dss.models import db


class Administrator(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(50))

    status = db.Column(db.Integer)

    password = db.Column(db.String(100))

    def __init__(self, username, status, password):
        self.username = username
        self.status = status
        self.password = password
