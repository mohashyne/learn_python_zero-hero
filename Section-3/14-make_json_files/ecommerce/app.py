import json
from pathlib import Path    

# What is JSON?

# JSON stands for JavaScript Object Notation. It is a lightweight data format used for exchanging and storing data in a structured way. JSON is easy to read and write for humans, and it is also simple for machines to parse and generate.

# It is widely used for transmitting data between a server and a web application or between different software systems.


# In the example below:

#     Keys are strings (e.g., "name", "age").
#     Values can be strings, numbers, booleans, arrays, or other JSON objects.

# Working with JSON Files in Python

# Python provides a built-in module called json to work with JSON data.

# movies = [
#     {'id': 1, 'title': 'The Shawshank Redemption', 'year': 1994},
#     {'id': 2, 'title': 'The Godfather', 'year': 1972},
#     {'id': 3, 'title': 'The Dark Knight', 'year': 2008},
#     {'id': 4, 'title': 'Pulp Fiction', 'year': 1994},
#     {'id': 5, 'title': 'Forrest Gump', 'year': 1994},
#     {'id': 6, 'title': 'Inception', 'year': 2010},
#     {'id': 7, 'title': 'Fight Club', 'year': 1999},
#     {'id': 8, 'title': 'The Matrix', 'year': 1999},
#     {'id': 9, 'title': 'The Lord of the Rings: The Fellowship of the Ring', 'year': 2001},
#     {'id': 10, 'title': 'Interstellar', 'year': 2014}
# ]


# data = json.dumps(movies)
# print(data)
# Path("Section-3/14-make_json_files/movies.json").write_text(data)





# READ JSON FILES
movie_data = Path("Section-3/14-make_json_files/movies.json").read_text()
get_movies = json.loads(movie_data)
print(get_movies)


print(get_movies[0]) # {'id': 1, 'title': 'The Shawshank Redemption', 'year': 1994}
print(get_movies[0]["title"]) # The Shawshank Redemption