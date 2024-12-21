import sqlite3
import json 
from pathlib import Path

# What is SQLite?

# SQLite is a lightweight, self-contained, serverless database engine that is widely used for local storage in applications. It is open-source and provides a simple way to store, query, and manipulate structured data. SQLite stores the entire database in a single file, making it easy to use without requiring a separate server or configuration.
# Key Features of SQLite:

#     Serverless: No need for a separate server to run; the database is directly embedded in the application.
#     Zero Configuration: Requires no setup or administration.
#     Portable: Database files are cross-platform and can be easily shared or transferred.
#     Lightweight: Minimal resource usage, ideal for small to medium-sized applications.

# Working with SQLite in Python

# Python provides the sqlite3 module to work with SQLite databases. Below are the key steps to interact with an SQLite database.

# CREATING THE  DATABASE
# movie_data = json.loads(Path("Section-3/15-sqlite_in_action/movies.json").read_text())
# print(movie_data)

# # connect to sqlite
# # connections = sqlite3.connect("db.sqlite")
# with sqlite3.connect("Section-3/15-sqlite_in_action/db.sqlite") as connections:
#     command = "INSERT INTO Movies VALUES(?, ?, ?)"
#     for movie in movie_data:
#         connections.execute(command, tuple(movie.values()))
#     connections.commit()  # sqlite3.OperationalError: no such table: Movies  

# if we run this program we are going to get an error, create the table manually 


# ACCESSING THE DATABASE
# connect to sqlite
with sqlite3.connect("Section-3/15-sqlite_in_action/db.sqlite") as connections:
    command = "SELECT * FROM Movies"
    cursor = connections.execute(command)
    # for row in cursor:
    #     print(row)  
    # # we can also use the cursor command to fetchall data , but if we run it below
        # without commenting the above we get and empty result because the for command has finished the iteration
movies = cursor.fetchall()

print(movies)