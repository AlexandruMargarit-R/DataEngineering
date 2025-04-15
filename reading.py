import pandas as pd
from snowflake.snowpark import Session

# link of the csv: https://www.kaggle.com/datasets/shivamb/netflix-shows
df = pd.read_csv("inputs/netflix_titles.csv")
# print(df.head())
# top_movies = df[df["type"] == "Movie"]
# print(top_movies)
#
# # connection_parameters = {
#     "account": "your_account",
#     "user": "your_user",
#     "password": "your_password",
#     "role": "your_role",
#     "warehouse": "your_warehouse",
#     "database": "your_database",
#     "schema": "your_schema",
# }


def top_each(dataframe, filter_value):
    filtered_df = dataframe[dataframe["type"] == filter_value]
    filtered_df = filtered_df.drop(columns=["show_id", "cast", "country", "date_added"])
    return filtered_df


best_tv_shows = top_each(df, "TV Show")
print(best_tv_shows)
print(best_tv_shows.describe(include="all"))


best_movies = top_each(df, "Movie")
print(best_movies)
print(best_movies.describe(include="all"))
