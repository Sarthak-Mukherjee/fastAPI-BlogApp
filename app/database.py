from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQLALCHEMY_DATABASE_URL = 'username:password@host:port/database_name'
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:password123@localhost/fastapi'

# engine is responsible for managing the connection to the database
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SessionLocal is a factory for talking to the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# dependency - we use this to create a new session for every request and close it once the request is done
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()