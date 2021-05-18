# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:39:57 2020

@author: VALUED CUSTOMERC
"""
import sqlite3
import assignment1
from classes import Books

    
def display_menu():
    print("COMMAND MENU")
    print("every - display everything")
    print("cat  - view books by category")
    print("year  - view books by year")
    print("ti    - view books by title")
    print("pur   - check out books")
    print("exit - Exit program")
    print()    
    

def display_books_by_category():
    category_name = input("Category name: ")
    category = assignment1.get_books_by_category(category_name)
    if category == None:
        print("There is no category with that ID.\n")
    else:
        print()
        display_books(category)
    
def display_books_by_year():
    year = int(input("Year: "))
    print()
    books = assignment1.get_books_by_year(year)
    display_books(books)
    
def display_books_by_title():
    title = input("title: ")
    print()
    books = assignment1.get_books_by_title(title)
    display_books(books)
    
    
    
    
def display_books(books):
    print("Books - ")
  
   # print("-" * 64)
    line_format = "{:3s} {:20s} {:6s} {:18s} {:15s}"
    print(line_format.format("ID", "Name", "Year", "Author", 
                             "Category"))
    print("-" * 64)
    for book in books:
        print(line_format.format(str(book.id), book.name,
                                 str(book.year), 
                                 str(book.author),
                                 book.category))
    print()    
    



def display_everything():
    books = assignment1.get_everything()
    display_books(books)
    




def main():
#    conn = sqlite3.connect("Books")       
#    c = conn.cursor()
#    c.execute('CREATE TABLE IF NOT EXISTS Books (id INTEGER, name TEXT, year INTEGER,author TEXT, category TEXT)')
#    assignment1.add_books(1,"Catcher and the Rye", 1956, "Something Something", "Romance")
#    assignment1.add_books(2,"Oliver Twist", 1903, "Henry Dickons", "Period Drama")
#    assignment1.add_books(3,"Leviathan Wakes", 2014, "Henry Bowers", "Science Fiction")
#    assignment1.add_books(4,"Cibola Burns", 2017, "Charles Hapster", "Science Fiction")

    display_menu()
    while True:        
        command = input("Command: ")
        if command == "cat":
            display_books_by_category()
        elif command == "every":
            display_everything()
        elif command == "year":
            display_books_by_year()
        elif command == "ti":
            display_books_by_title()
        elif command == "pur":
            assignment1.get_reciept()
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
            display_menu()
    assignment1.close()
    print("Bye!")
    
if __name__ == "__main__":
    main()
