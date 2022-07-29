import os

database_infos = {
    "TYPE": os.getenv("DATABASE_TYPE"),
    "DB_NAME": os.getenv("DATABASE_DB_NAME"),
    "USERNAME": os.getenv("DATABASE_USERNAME"),
    "PASSWORD": os.getenv("DATABASE_PASSWORD"),
    "PORT": os.getenv("DATABASE_PORT"),
    "HOST": os.getenv("DATABASE_HOST")
}
