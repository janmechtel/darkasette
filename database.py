#database.py

import sqlite3

pings_tablename = "pings"
services_tablename = "services"
files_tablename = "files"

def create_connection():
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect('darkasette.db')
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

def generateCreateTableQuery(tablename, columns):
    query = 'CREATE TABLE IF NOT EXISTS "' + tablename + '" ('
    for column in columns:
        query += '\n"' + column[0] + '" ' + column[1] + ','
    query = query[:-1] + ');'
    print(query)
    return query

def drop_table(tablename, conn):
    query = 'DROP TABLE IF EXISTS "' + tablename + '";'
    conn.execute(query)
    print("Table " + tablename + " dropped")