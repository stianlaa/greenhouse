"""
flask_app.py
- creates a Flask app instance and registers the database object
"""

from flask import Flask
from flask_cors import CORS
from .api import api

def create_app(app_name='SURVEY_API'):
  app = Flask(app_name)
  app.config.from_object('greenhouse.api_pkg.config.BaseConfig')
  cors = CORS(app, resources={"/api/*": {"origins": "*"}})

  app.register_blueprint(api, url_prefix="/api")

  return app
