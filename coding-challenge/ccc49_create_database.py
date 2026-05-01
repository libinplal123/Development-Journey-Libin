import sqlite3 
connection = sqlite3.connect('movies.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS movies(
               year INTEGER,
               title TEXT,
               genre TEXT
               )
''')
movie_data = [
    (2009, 'Brothers', 'Drama'),
    (2002, 'Spider Man', 'Sci-fi'),
    (2009, 'WatchMen', 'Drama'),
    (2010, 'Inception', 'Sci-fi'),
    (2009, 'Avatar', 'Fantasy')
]
query = "INSERT INTO movies (year, title, genre) values (?, ?, ?)"
cursor.executemany(query,movie_data)
connection.commit()

print("a) All movies")
cursor.execute('SELECT * FROM movies')
for row in cursor.fetchall():
    print(row)

print("\nb) only 'Brothers' movie")
cursor.execute("SELECT * from movies where title = 'Brothers'")
print(cursor.fetchone())

print("\nc) All movies released in 2009")
cursor.execute("SELECT * FROM movies where year = '2009'")
for row in cursor.fetchall():
    print(row)

print("\nd) Fantasy or Drama movies")
cursor.execute("SELECT * FROM movies where genre = 'Fantasy' OR genre = 'Drama'")
for row in cursor.fetchall():
    print(row)

print("\ne) Deleting all contents...")
cursor.execute("DELETE FROM movies")
connection.commit()