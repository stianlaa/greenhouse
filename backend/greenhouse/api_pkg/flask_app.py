"""
flask_app.py
- creates a Flask app instance and registers the database object
"""

from flask import Flask
from flask_cors import CORS
from .api import api
import logging

def create_flask_app(app_name='GREENHOUSE'):
  logging.info("starting flask app")
  flask_app = Flask(app_name)
  flask_app.config.from_object('greenhouse.api_pkg.config.BaseConfig')
  cors = CORS(flask_app, resources={"/api/*": {"origins": "*"}})
  flask_app.register_blueprint(api, url_prefix="/api")
  logging.info("flask app started")
  return flask_app
