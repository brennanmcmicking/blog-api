import sqlite3
from sqlite3 import Error

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)


if __name__ == '__main__':
    conn = create_connection(r"posts.db")
    sql_create_posts_table = """ CREATE TABLE IF NOT EXISTS posts (
                                    id INTEGER PRIMARY KEY,
                                    title text NOT NULL,
                                    body text NOT NULL,
                                    author text NOT NULL,
                                    date text NOT NULL
                                ); """

    if conn is not None:
        create_table(conn, sql_create_posts_table)
        conn.close()
    else:
        print("Error, failed to open connection")