class UserController:
    def __init__(self, db):
        self.db = db

    def register_user(self, name, email, password, profile):
        self.db.execute_query('INSERT INTO users (name, email, password, profile) VALUES (?, ?, ?, ?)',
                              (name, email, password, profile))

    def authenticate_user(self, email, password):
        cursor = self.db.execute_query('SELECT * FROM users WHERE email = ? AND password = ?', (email, password))
        return cursor.fetchone()
