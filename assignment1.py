# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 17:30:51 2020

@author: VALUED CUSTOMER
"""

import sqlite3
from contextlib import closing
from classes import Books
# connect to the database and set the row factory


conn = sqlite3.connect("Book")       
c = conn.cursor()


def close():
    if conn:
        conn.close()
        

def make_book(row):
    return Books(row[0], row[1], row[2], row[3], row[4])


def get_books_by_category(category_name):
    try:
        query = '''SELECT  id, name, year, author,
                          category as "category Name"
                   FROM Book
                   WHERE category = ?'''
        with closing(conn.cursor()) as c:
            c.execute(query, (category_name,))
            results = c.fetchall()
            
        book = []
        for row in results:
            book.append(make_book(row))
        return book
    except:
        print("An error occured, check back code")

def get_books_by_title(category_name):
    try:
        query = '''SELECT  id, name, year, author,
                          category
                   FROM Book
                   WHERE name = ?'''
        with closing(conn.cursor()) as c:
            c.execute(query, (category_name,))
            results = c.fetchall()
            
        book = []
        for row in results:
            book.append(make_book(row))
        return book
    except ValueError:
        print("an error occured. Check back code")

def get_everything():
    query = '''SELECT *
               FROM Book'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()
        
    book = []
    for row in results:
        book.append(make_book(row))
    return book




def get_books_by_year(year):
    query = '''SELECT id, name, year, author,
                      category
               FROM Book 
               WHERE year = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (year,))
        results = c.fetchall()
        
    book = []
    for row in results:
        book.append(make_book(row))
    return book

def get_reciept():  
    choice = "";
    s = ""
    book = []
   # display_everything()
    try:
            while choice !="0":
                choice = input("Please name selection. Type 0 to stop ")
                
                query = '''SELECT id, name, year, author,
                              category
                       FROM Book 
                       WHERE name = ?'''
                with closing(conn.cursor()) as c:
                    c.execute(query, (choice,))
                    results = c.fetchall()
                    
                
                for row in results:
                    book.append(make_book(row))
             
            for books in book:
                s += books.name +"\n"
            print()
            print("Your checkout reciept")  
            print("-" * 64)
            print(s)
            print("Return in 3 weeks")
    except ValueError:
            print("An error occured. Please check back code.")

def add_books(id,name,year,author,category):
    sql = '''INSERT INTO Book (id
    , name, year, author, category)
    VALUES (?, ?, ?, ?,?)'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (id, name,year,author,category))
        conn.commit()


    
  
