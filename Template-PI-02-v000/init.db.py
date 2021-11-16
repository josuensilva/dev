import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Post', 'Content for the first post')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Post', 'Content for the second post')
            )

cur.execute("INSERT INTO Users (fname, lname, email, password) VALUES (?, ?, ?, ?)",
            ('fname', 'lname', 'email', 'password')
            )

cur.execute("INSERT INTO Purchases (nameproduct, quantity, email, description) VALUES (?, ?, ?, ?)",
            ('nameproduct', 'quantity', 'email', 'description')
            )


connection.commit()
connection.close()