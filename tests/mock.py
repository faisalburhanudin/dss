import unittest
from dss import http
from dss.models import db


class ServerTest(unittest.TestCase):
    # application context
    context = http.factory(testing=True)

    # flask client test
    app = context.test_client()

    # make sqlalchemy known application
    context.app_context().push()

    def db_migrate(self):
        """Create all tables"""
        with self.context.app_context():
            db.create_all()

    def db_drop(self):
        """drop all tables"""
        with self.context.app_context():
            db.drop_all()
