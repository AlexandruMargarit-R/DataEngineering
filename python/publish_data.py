import io
import os

import fetch_data
import psycopg2
from dotenv import load_dotenv

dotenv_path = os.path.abspath("dbt.env")
load_dotenv(dotenv_path)

print(df.head())

# connection = psycopg2.connect(
#     database="postgres",
#     user=os.getenv("postgress_user"),
#     password=os.getenv("postgress_password"),
#     host="localhost",
#     port=5432,
# )
#
#
