# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from importlib import import_module
from flask_mongoengine import MongoEngine,MongoEngineSessionInterface

db = MongoEngine()
login_manager = LoginManager()


def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)


def register_blueprints(app):
    for module_name in ('authentication', 'home'):
        module = import_module('apps.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)
    return app
