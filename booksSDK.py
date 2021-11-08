import sqlite3
from source import trySDK

def cursor():
    return sqlite3.connect('books.db').cursor()

c= cursor()
c.execute('CREATE TABLE IF NOT EXISTS books(title TEXT, pages INTEGER)') 
c.connection.close()

def add_book(book):
    c = cursor()

    with c.connection:
        c.execute('INSERT INTO  books VALUES(?, ?)', (book.title, book.pages))
    c.connection.close()
    return c.lastrowid

def get_books():
    c = cursor()
    books = []

    with c.connection:
        for book in c.execute('SELECT * FROM books'):
            books.append(trySDK(book[0], book[1]))
    c.connection.close()
    return  books

def get_book_by_title(title):
    c = cursor()
    c.execute('SELECT * FROM books WHERE title=?', (title,))
    # return c.fetchone()
    data = c.fetchone()
    c.connection.close()

    if not data:
        return None

    return trySDK(data[0], data[1])