from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from app.core.config import settings

Base = declarative_base()

engine = create_engine(settings.DB_CONNECTION)

locaclSession = sessionmaker(bind=engine)

def get_db():
    db = locaclSession()
    try:
        yield db
    finally:
        db.close()
