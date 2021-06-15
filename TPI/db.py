from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pymysql
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("mysql+pymysql://root:asd123asd@localhost/dbTest",
                       )
Session = sessionmaker(bind=engine)
session=Session()
Base = declarative_base()