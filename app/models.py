import os

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from dotenv import load_dotenv
# import psycopg2
import pandas as pd

from .database import Base, engine
from .file_operations import Csv

SCV_FOLDER = Csv._folder_path


load_dotenv()
HOSTNAME = os.getenv("DATABASE_HOSTNAME")
PORT = os.getenv("DATABASE_PORT")
PASSWORD = os.getenv("DATABASE_PASSWORD")
DB_NAME = os.getenv("DATABASE_NAME")
USERNAME = os.getenv("DATABASE_USERNAME")


# DATABASE_URL = f"postgresql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DB_NAME}"
# conn = psycopg2.connect(
# dbname=DB_NAME, user=USERNAME, password=PASSWORD, host=HOSTNAME, port=PORT
# )
# cur = conn.cursor()


# def create_table_from_csv(file):
# cur.copy_from(file=file, table=file.filename)


def create_table_from_csv(filename):
    df = pd.read_csv(Csv._folder_path + f"/{filename}")
    print(file)
    df.to_sql("_".join(filename.split(".")[:-1]).strip().lower(), engine)

def get_file_from_table(filename):
    file = pd.read_sql_query()

