import pandas as pd

data = {
    "year": [2009, 2002, 2009, 2010, 2009],
    "Title": ["Brothers", "Spider-Man", "WatchMen", "Inception", "Avatar"],
    "genre": ["Drama", "Sci-fi", "Drama", "Sci-fi", "Fantasy"]
}

df = pd.DataFrame(data)
print(df)