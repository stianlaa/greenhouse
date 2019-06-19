"""
application.py
- creates the application instance
"""

from greenhouse.api_pkg import flask_app
from greenhouse.api_pkg import flask_app

def create_flask_app():

  app = flask_app.create_flask_app()
  return app
