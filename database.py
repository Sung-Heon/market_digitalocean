from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = f'''mysql+pymysql://{os.environ['DB_ID']}:{os.environ['DB_PASSWORD']}@kurly-ss.c78egjhpmq4e.ap-northeast-2.rds.amazonaws.com:3306/mydb'''

engine = create_engine(
    SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
