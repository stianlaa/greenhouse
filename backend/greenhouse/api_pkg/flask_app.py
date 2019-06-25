"""
flask_app.py
- creates a Flask app instance and registers the database object
"""

from flask import Flask
from flask_cors import CORS
from .api import api

def create_flask_app(app_name='GREENHOUSE'):
  print("0")
  logging.info("0")
  flask_app = Flask(app_name)
  print("1")  
  flask_app.config.from_object('greenhouse.api_pkg.config.BaseConfig')
  print("2")
  logging.info("2")
  cors = CORS(flask_app, resources={"/api/*": {"origins": "*"}})
  print("3")  
  flask_app.register_blueprint(api, url_prefix="/api")
  print("Started flask app")
  logging.info("4")
  return flask_app
