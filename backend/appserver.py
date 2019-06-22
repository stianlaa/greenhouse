"""
appserver.py
- creates an application instance and runs the dev server
"""
from datetime import datetime, timedelta


def start_main_loop():
  print("Starting main loop")
  database = "C:\\sqlite\db\pythonsqlite.db"
  from greenhouse.data.storage import create_connection
  from greenhouse.consumers.weatherstatus import fetch_and_store_weatherdata

  conn = create_connection(database)

  with conn:

    while True:
      next_time = next_request_time(1800, 30)
      print("fetching and storing weatherdata")
      fetch_and_store_weatherdata(conn)

      while datetime.now() < next_time:
        time.sleep(5)

def start_flask_app():
  from greenhouse.application import create_flask_app
  app = create_flask_app()
  app.run(host='0.0.0.0')
  

def next_request_time(interval_time_seconds, variation):
  from random import randint
  return datetime.now() + timedelta(seconds = interval_time_seconds) + timedelta(seconds = randint(-variation, variation))


if __name__ == '__main__':
  import threading
  import time

  threading.Thread(target=start_flask_app, daemon=True).start()

  time.sleep(1)

  threading.Thread(start_main_loop(), daemon=True).start()
  