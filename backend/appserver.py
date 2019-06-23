"""
appserver.py
- creates an application instance and runs the dev server
"""
from datetime import datetime, timedelta
import logging


def start_main_loop():
  from greenhouse.data.storage import create_connection
  from greenhouse.consumers.weatherstatus import fetch_and_store_weatherdata
  from db.create_database import get_db_path

  conn = create_connection(get_db_path())

  with conn:
    logging.info("Started weatherstatus fetcher")

    while True:
      # next_time = next_request_time(1800, 30)
      next_time = next_request_time(30, 3)
      fetch_and_store_weatherdata(conn)

      while datetime.now() < next_time:
        time.sleep(5)


def start_flask_app():
  from greenhouse.application import create_flask_app
  app = create_flask_app()
  logging.info("Started flask app")
  app.run(host='0.0.0.0') # 0.0.0.0 for opening to non-localhost
  

def next_request_time(interval_time_seconds, variation):
  from random import randint
  return datetime.now() + timedelta(seconds = interval_time_seconds) + timedelta(seconds = randint(-variation, variation))


def setup_logging(log_level):
  logFormatter = '%(asctime)s - %(levelname)s - %(message)s'
  logging.basicConfig(format=logFormatter, level=log_level)
  logger = logging.getLogger(__name__)


def start_greenhouse_app():
  import threading
  import time

  setup_logging(logging.INFO)

  threading.Thread(target=start_flask_app, daemon=True).start()

  time.sleep(1)

  threading.Thread(start_main_loop(), daemon=True).start()
  

if __name__ == '__main__':
  start_greenhouse_app()