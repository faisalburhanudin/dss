import os
import configuration

from flask import Flask
from dss.models import db
from dss.routes import admin
from dss.routes import frontend

UPLOAD_FOLDER = os.path.dirname(os.path.realpath(__file__)) + "/static/img"


def factory(testing=False):
    app = Flask(__name__.split(',')[0])
    app.register_blueprint(admin.home.bp)
    app.register_blueprint(admin.user.bp)
    app.register_blueprint(admin.gpu.bp)
    app.register_blueprint(admin.cpu.bp)
    app.register_blueprint(admin.computer.bp)
    app.register_blueprint(frontend.bp)

    if testing:
        app.config['TESTING'] = True
        app.config.from_object(configuration.FlaskTesting)
    else:
        app.config.from_object(configuration.Config)

    db.init_app(app=app)

    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    return app


