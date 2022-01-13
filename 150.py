# There is duplication in create_table_* methods!!!
# I need to use with statement to avoid conn.close()


import sqlite3
from sqlite3 import Error



class Database:
    def __init__(self, dbname):
        self.dbname = dbname

    def _connect(self):
        conn = None
        try:
            conn = sqlite3.connect(self.dbname)
            return conn
        except Error as e:
            print("Error in connection::", e)
        

    def create_artist_table(self):
        sql = """ CREATE TABLE IF NOT EXISTS artists (
                  id integer PRIMARY KEY,
                  name text,
                  address text,
                  town text,
                  country text,
                  postcode text
              );
              """
        conn = self._connect()
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
        except Error as e: 
            print("Error in create table::", e) 
        finally:
            conn.close()

    def create_price_of_art_table(self):
        sql = """ CREATE TABLE IF NOT EXISTS (
                  id INTEGER PRIMARY KEY,
                  artist_id INTEGER NOT NULL,
                  title TEXT,
                  meidum TEXT,
                  price REAL,
                  FOREIGN KEY(artist_id) REFERENCES artists (id)
              );
              """
        conn = self._connect()
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
        except Erorr as e:
            print(e)
        finally:
            conn.close()


if __name__ == "__main__":
    ### TEST  ###
    db = Database("art_gallery.db")
    db.create_artist_table()
    db.create_price_of_art_table()

       

