# There is duplication in create_table_* methods!!!
# I need to use with statement to avoid conn.close()


import sqlite3
import tkinter as tk

from sqlite3 import Error
from tkinter import ttk




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
        sql = """ CREATE TABLE IF NOT EXISTS price_of_art (
                  id INTEGER PRIMARY KEY,
                  artist_id INTEGER NOT NULL,
                  title TEXT,
                  meidum TEXT,
                  price REAL,
                  FOREIGN KEY (artist_id) REFERENCES artists (id)
              );
              """
        conn = self._connect()
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
        except Error as e:
            print(e)
        finally:
            conn.close()
    def create_artist(self, *record):
        sql = """ INSERT INTO artists(name, address, town, country, postcode)
                  VALUES(?, ?, ?, ?, ?);
              """
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute(sql, record)
        conn.commit()
        print("Artist saved.")


class ArtGallery:
    def __init__(self, db):
        self.db = db
        self.root = tk.Tk()
        self.root.title("Art Gallery")
        
        add_artist = ttk.Button(self.root, text="Add New Art")
        add_artist["command"] = self.add_new_artist
        add_artist.pack()
        self.root.mainloop()
    
    def add_new_artist(self):
        window = tk.Toplevel(self.root)
        ttk.Label(window, text="Name: ").pack()
        name = ttk.Entry(window)
        name.pack()
        ttk.Label(window, text="Address").pack()
        addr = ttk.Entry(window)
        addr.pack()
        ttk.Label(window, text="Town").pack()
        town = ttk.Entry(window)
        town.pack()
        ttk.Label(window, text="Country").pack()
        country = ttk.Entry(window)
        country.pack()
        ttk.Label(window, text="Postcode").pack()
        postcode = ttk.Entry(window)
        postcode.pack()
        save_btn = ttk.Button(window, text="Save Artist")
        save_btn.pack()
        save_btn["command"] = lambda: self.db.create_artist(
                name.get(), 
                addr.get(), 
                town.get(),
                country.get(), 
                postcode.get()
            )


if __name__ == "__main__":
    ### TEST  ###
    db = Database("art_gallery.db")
    #db.create_artist_table()
    #db.create_price_of_art_table()
    art_gallery = ArtGallery(db)

