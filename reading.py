import pandas as pd
from snowflake.snowpark import Session

df = pd.read_csv("inputs/netflix_titles.csv")
top_movies = df[df["type"] == "Movie"]
print(top_movies)

connection_parameters = {
    "account": "your_account",
    "user": "your_user",
    "password": "your_password",
    "role": "your_role",
    "warehouse": "your_warehouse",
    "database": "your_database",
    "schema": "your_schema",
}
