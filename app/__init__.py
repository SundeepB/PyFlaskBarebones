import logging
from logging.handlers import RotatingFileHandler

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS, cross_origin

from config import app_config

db = SQLAlchemy()

ROOT_PATH = ''

def create_app(config_name, rootDirPath):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    ROOT_PATH = rootDirPath

    handler = RotatingFileHandler('server.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)

    db.init_app(app)
    app.logger.info('Initialized db with app')

    migrate = Migrate(app, db)

    from .barebones import barebones
    app.register_blueprint(barebones, url_prefix='/barebones')

    @app.route('/')
    def hello_world():
        return 'Hello, Universe!'

    return app
