import sqlite3

def create_db():
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY,
            title TEXT,
            username TEXT,
            url TEXT,
            password TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_password(title, username, url, password):
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute('INSERT INTO passwords (title, username, url, password) VALUES (?, ?, ?, ?)',
              (title, username, url, password))
    conn.commit()
    conn.close()

def get_passwords():
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute('SELECT * FROM passwords')
    rows = c.fetchall()
    conn.close()
    return rows

def delete_password(password_id):
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute('DELETE FROM passwords WHERE id = ?', (password_id,))
    conn.commit()
    conn.close()
