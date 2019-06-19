"""
storage.py
- offers storage writing and reading methods to other modules
"""

import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
def add_weatherdata(conn, weatherdata):
    sql = ''' INSERT INTO weatherdata(dateAndTime, temperature, humidity, cloudiness)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, weatherdata)
    return cur.lastrowid

def select_all_weatherdata(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM weatherdata")
    rows = cur.fetchall()
    
    for row in rows:
        print(row)
    return rows