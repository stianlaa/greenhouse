"""
create_database.py
- creates the database used for the greenhouse backend application
"""

import sqlite3
from sqlite3 import Error
import platform

db_path_linux = "/home/stian/sqlite/greenhouse.db"
db_path_win = "C:\\sqlite\\greenhouse.db"

def get_db_path():
    current_os = platform.system().lower()
    if (current_os == 'windows'):
        return db_path_win
    elif (current_os == 'linux'):
        return db_path_linux
    else:
        print("Unable to determine os")


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database_path = get_db_path()
    weatherdata_table = """CREATE TABLE IF NOT EXISTS weatherdata (
                                        id integer PRIMARY KEY,
                                        dateAndTime text NOT NULL,
                                        temperature text NOT NULL,
                                        humidity text NOT NULL,
                                        cloudiness text NOT NULL
                                    );""" 
    # create a database connection
    conn = create_connection(database_path)
    if conn is not None:
        create_table(conn, weatherdata_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
