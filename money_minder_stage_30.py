# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: MoneyMinder
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save(self, db_path='users.db'):
        import sqlite3
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE, password TEXT)')
        try:
            c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (self.username, self.password))
        except sqlite3.IntegrityError:
            pass
        conn.commit()
        conn.close()

    def authenticate(self, db_path='users.db'):
        import sqlite3
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute('SELECT password FROM users WHERE username = ?', (self.username,))
        row = c.fetchone()
        conn.close()
        return self.password == row[0] if row else False

    @staticmethod
    def login(username, db_path='users.db'):
        import sqlite3
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute('SELECT id FROM users WHERE username = ?', (username,))
        user = c.fetchone()
        conn.close()
        return User.__new__(User) if user else None

    def __repr__(self):
        return f'User({self.username!r})'
