import os
import configuration

from flask import Flask
from flask_login import LoginManager
from dss.models import db, Administrator
from dss.routes import admin
from dss.routes import frontend

UPLOAD_FOLDER = os.path.dirname(os.path.realpath(__file__)) + "/static/img"


login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return Administrator.query.filter_by(id=user_id).first()


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
    login_manager.init_app(app)

    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.secret_key = "3d423f424f2"
    return app


