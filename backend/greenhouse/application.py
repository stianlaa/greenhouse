"""
application.py
- creates the application instance
"""

from greenhouse.api_pkg import flask_app

def create_app(app_name='GREENHOUSE_BACKEND'):

  app = flask_app.create_app()
  return app
