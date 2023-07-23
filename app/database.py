import os


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()
HOSTNAME = os.getenv("DATABASE_HOSTNAME")
PORT = os.getenv("DATABASE_PORT")
PASSWORD = os.getenv("DATABASE_PASSWORD")
DB_NAME = os.getenv("DATABASE_NAME")
USERNAME = os.getenv("DATABASE_USERNAME")


SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DB_NAME}"
)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()


def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()
