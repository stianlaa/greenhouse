"""
appserver.py
- creates an application instance and runs the dev server
"""
def start_main_loop():
  print("Starting main loop")
  database = "C:\\sqlite\db\pythonsqlite.db"
  from greenhouse.data.storage import create_connection, add_weatherdata, select_all_weatherdata
  from greenhouse.consumers.weatherstatus import fetch_and_store_weatherdata

  conn = create_connection(database)

  with conn:
    i = 0
    
    while i < 3:
      fetch_and_store_weatherdata(conn)
      # print("last row id:")
      # print(add_weatherdata(conn, ("dateAndTimeEntry", "temperatureEntry", "humidityEntry", "cloudinessEntry")))
      i+=1
      time.sleep(1)
    select_all_weatherdata(conn)

def start_flask_app():
  from greenhouse.application import create_flask_app
  app = create_flask_app()
  app.run(host='127.0.0.1')
  
if __name__ == '__main__':
  import threading
  import time

  threading.Thread(target=start_flask_app, daemon=True).start()

  time.sleep(1)

  threading.Thread(start_main_loop(), daemon=True).start()
  

  
