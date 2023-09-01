#database.py

import sqlite3

def create_connection():
    """ create a database connection to a SQLite database """
    # #delete the file if it exists
    # import os
    # if os.path.exists("darkwebreports.db"):
    #     os.remove("darkwebreports.db")
    conn = None
    try:
        conn = sqlite3.connect('darkwebreports.db')
        print("Connection to SQLite DB successful")
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")
    return conn

def close_connection(conn):
    """ close connection to the database """
    if conn:
        conn.execute('VACUUM')
        conn.commit()
        conn.close()
        print("The SQLite connection is closed")
