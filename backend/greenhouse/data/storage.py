"""
storage.py
- offers storage writing and reading methods to other modules
"""

import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    try:
        print("establishing database connection")
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
def store_weatherdata(conn, weatherdata):
    sql = ''' INSERT INTO weatherdata(dateAndTime, temperature, humidity, cloudiness)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    try:
        cur.execute(sql, weatherdata)
        conn.commit()
        return cur.lastrowid
    except Exception as err:
        if str(err) != "interrupted":
            print ("Database error: {0}".format(str(err)))
        return None

def select_all_weatherdata(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM weatherdata")
    rows = cur.fetchall()
    
    for row in rows:
        print(row)
    return rows