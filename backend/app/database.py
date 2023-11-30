import os
from contextvars import ContextVar
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Compose the MySQL URL using environment variables
DB_USER = os.environ.get("PGUSER")
DB_PASSWORD = os.environ.get("PGPASSWORD")
DB_HOST = os.environ.get("PGHOST")
DB_PORT = os.environ.get("PGPORT")
DB_NAME = os.environ.get("PGDATABASE")

# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
SQLALCHEMY_DATABASE_URL = f"mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

# create the SessionLocal class using the function sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class, inherit from this class to create ORM models
Base = declarative_base()


@contextmanager
def get_db():
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()


# setup context variable
db = ContextVar("db")