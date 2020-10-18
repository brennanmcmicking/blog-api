import sqlitecreator
import sqlite3
from sqlite3 import Error
from datetime import datetime

def insert_post(title, author, body):
    try:
        conn = sqlitecreator.create_connection('posts.db')
        cursor = conn.cursor()
        cursor.execute(f'INSERT INTO posts (title, body, author, date) VALUES (\'{title}\', \'{author}\', \'{body}\', \'{datetime.now()}\');')
        conn.commit()
    except Error as e:
        print(e)
        
    conn.close()


if __name__ == "__main__":
    f = open('newpost.txt', 'r')
    title = f.readline()
    author = f.readline()
    body = f.readline()
    f.close()

    insert_post(title, author, body)