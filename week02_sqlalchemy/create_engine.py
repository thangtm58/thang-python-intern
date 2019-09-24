from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from sqlalchemy.sql import *

connection_string = 'postgresql://{user}:{pswd}@{host}:{port}/{db}'.format(
            user='macbook',
            pswd='101199',
            host='localhost',
            port='5432',
            db='user_tracking'
        )

Base = declarative_base()

class Customer(Base):
    __tablename__ = "customers"
    user_id = Column(String, Sequence('id_seq'), primary_key=True)
    name = Column(String)
    dob = Column(String)
    updated_at = Column(String)

engine = create_engine(connection_string)

# id.__table__.create(bind=engine, checkfirst=True)

Session = sessionmaker(bind=engine)

session = Session()

# insert data of name c
for data in session.query(Customer):
    print([data.user_id])





