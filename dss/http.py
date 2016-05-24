import configuration

from flask import Flask
from dss.models import db
from dss.routes import admin
from dss.routes import frontend


def factory(testing=False):
    app = Flask(__name__.split(',')[0])
    app.register_blueprint(admin.bp)
    app.register_blueprint(frontend.bp)

    if testing:
        app.config['TESTING'] = True
        app.config.from_object(configuration.FlaskTesting)

    db.init_app(app=app)
    return app
