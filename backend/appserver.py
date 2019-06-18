"""
appserver.py
- creates an application instance and runs the dev server
"""
def start_main_loop():
  i = 0
  while i < 10:
    i+=1
    print(i)
    time.sleep(1)

def start_flask_app():
  from greenhouse.application import create_flask_app
  app = create_flask_app()
  app.run(host='127.0.0.1')
  
if __name__ == '__main__':
  import threading
  import time

  print("beep-boop")
  threading.Thread(target=start_flask_app, daemon=True).start()
  print("Success!")
  threading.Thread(start_main_loop()).start()

  
