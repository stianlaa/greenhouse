"""
wsgi.py
- should make the app object serve as callable for the uwsgi container server to execute against
"""

from appserver import create_flask_app

app = create_flask_app()  
