from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os


DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://locationuser:L0Le9lpsyOQJKWeBObdT8kcBILs4BmSg@dpg-da35gumk1f9s73e3ojr0-a.oregon-postgres.render.com/locationdb_cdnv"
)


engine = create_engine(
    DATABASE_URL
)


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


Base = declarative_base()