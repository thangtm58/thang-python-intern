from sqlalchemy import create_engine, Column, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# CREATE CONNECTION STRING
connection_string = 'postgresql://{user}:{pswd}@{host}:{port}/{db}'.format(
    user='macbook',
    pswd='101199',
    host='localhost',
    port='5432',
    db='user_tracking'
)

#CREATE MODEL CLASS
Base = declarative_base()
class Customer(Base):
    __tablename__ = "customers"
    user_id       = Column(String, Sequence('id_seq'), primary_key=True)
    name          = Column(String)
    dob           = Column(String)
    updated_at    = Column(String)

#CREATE ENGINE
engine = create_engine(connection_string)

#MAKE SESSION AND CONNECT
Session = sessionmaker(bind=engine)
session = Session()

# Insert data of name column
for data in session.query(Customer):
    print([data.user_id])
