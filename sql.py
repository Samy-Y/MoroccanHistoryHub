import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('users.db')

# Create a cursor object
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    USERNAME TEXT NOT NULL,
    EMAIL TEXT NOT NULL,
    PASSWORD TEXT NOT NULL,
    PERMLEVEL INTEGER NOT NULL
)
''')

cursor.execute('''
INSERT INTO users (USERNAME, EMAIL, PASSWORD, PERMLEVEL)
VALUES (?, ?, ?, ?)
''', ('epicUserAdmin', 'bill@gates.us', 'superSecretPass123', 2))

# Commit the changes and close the connection
conn.commit()
conn.close()
