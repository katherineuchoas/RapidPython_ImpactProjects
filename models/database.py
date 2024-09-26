import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('library.db')
        self.create_tables()

    def create_tables(self):
        with self.conn:
            self.conn.execute('''CREATE TABLE IF NOT EXISTS users (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT NOT NULL,
                                    email TEXT NOT NULL UNIQUE,
                                    password TEXT NOT NULL,
                                    profile TEXT NOT NULL)''')
            self.conn.execute('''CREATE TABLE IF NOT EXISTS books (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    title TEXT NOT NULL,
                                    author TEXT NOT NULL,
                                    available BOOLEAN NOT NULL)''')

    def execute_query(self, query, params=()):
        with self.conn:
            cursor = self.conn.execute(query, params)
            return cursor

    def close(self):
        self.conn.close()
