class BookController:
    def __init__(self, db):
        self.db = db

    def add_book(self, title, author):
        self.db.execute_query('INSERT INTO books (title, author, available) VALUES (?, ?, ?)',
                              (title, author, True))

    def list_books(self):
        cursor = self.db.execute_query('SELECT * FROM books')
        return cursor.fetchall()

    def search_book_by_title(self, title):
        cursor = self.db.execute_query('SELECT * FROM books WHERE title LIKE ?', ('%' + title + '%',))
        return cursor.fetchall()
