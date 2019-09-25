from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from sqlalchemy.sql import *

#TODO Thang em xoa di cac import khong su dung den


connection_string = 'postgresql://{user}:{pswd}@{host}:{port}/{db}'.format(
            user='macbook',
            pswd='101199',
            host='localhost',
            port='54322',
            db='user_tracking'
            # TODO Thang chi nen tab vao du'ng 1 lan i.e. 4 spaces
)

Base = declarative_base()

class Customer(Base):
    __tablename__ = "customers"

    # TODO Thang dong thang hang cac dau bang
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

#TODO Thang cuoi tep chi nen co 1 dong trang
#TODO Thang lam tiep cac CRUD tr.tiep va bang ORMr



