import pandas as pd
from func.functions import top_each

# link of the csv: https://www.kaggle.com/datasets/shivamb/netflix-shows
df = pd.read_csv("../assets/netflix_titles.csv")


best_tv_shows = top_each(df, "TV Show")
print(best_tv_shows)
print(best_tv_shows.describe(include="all"))


best_movies = top_each(df, "Movie")
print(best_movies)
print(best_movies.describe(include="all"))
