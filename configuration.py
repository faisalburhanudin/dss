import os


class FlaskTesting(object):
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Config(object):
    SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://%s:%s@%s/%s" % (
        os.getenv("dbuser"), os.getenv("dbpass"), os.getenv("dbhost"), os.getenv("dbname"))

    SQLALCHEMY_TRACK_MODIFICATIONS = False
