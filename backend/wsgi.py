"""
wsgi.py
- should make the app object serve as callable for the uwsgi container server to execute against
"""

from greenhouse.application import create_app
app = create_app()
