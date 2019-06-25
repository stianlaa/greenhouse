"""
appserver.py
- creates an application instance and runs the dev server
"""

if __name__ == '__main__':
  from application import start_greenhouse_app
  greehouse_app = start_greenhouse_app()
  greenhouse_app.run(host='0.0.0.0')
