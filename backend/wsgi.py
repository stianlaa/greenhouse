"""
wsgi.py
- should make the app object serve as callable for the uwsgi container server to execute against
"""

from appserver import start_greenhouse_app

app = start_greenhouse_app()  