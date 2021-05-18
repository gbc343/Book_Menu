# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 20:03:32 2020

@author: VALUED CUSTOMER
"""
import sqlite3
import assignment1

conn = sqlite3.connect("Book")       
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS Books (id INTEGER, name TEXT, year INTEGER,author TEXT, category TEXT)')
conn.commit()
assignment1.add_books(1,"Catcher and the Rye", 1956, "Something Something", "Romance")
assignment1.add_books(2,"Oliver Twist", 1903, "Henry Dickons", "Period Drama")
assignment1.add_books(3,"Leviathan Wakes", 2014, "Henry Bowers", "Science Fiction")
assignment1.add_books(4,"Cibola Burns", 2017, "Charles Hapster", "Science Fiction")

conn.close()