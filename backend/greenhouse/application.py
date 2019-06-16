"""
application.py
- creates a Flask app instance and registers the database object
"""

from flask import Flask
from flask_cors import CORS

def create_app(app_name='SURVEY_API'):
  app = Flask(app_name)
  app.config.from_object('greenhouse.config.BaseConfig')
  cors = CORS(app, resources={"/api/*": {"origins": "*"}})

  from greenhouse.api import api
  app.register_blueprint(api, url_prefix="/api")

  return app
