from sqlalchemy_venv import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
Sessionlocal = sessionmaker(autocommit=False, autoFlush=False, bind=engine)
Base = declarative_base() #this is whats imported from models