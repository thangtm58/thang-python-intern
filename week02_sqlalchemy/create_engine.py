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

    def __init__(self, user_id, name, dob, updated_at):
        self.user_id = user_id
        self.name = name
        self.dob = dob
        self.updated_at = updated_at

#CREATE ENGINE
engine = create_engine(connection_string)

#MAKE SESSION AND CONNECT
Session = sessionmaker(bind=engine)
session = Session()

#CRUD
#CREATE
customer05 = Customer('user05','Vinicius','20011006','2019-06-12 07:53:01')
session.add(customer05)
session.commit()

#READ
for data in session.query(Customer):
    print(f'{data.name} : {data.dob}')

#UPDATE
customer_data = session.query(Customer).get('user01')
customer_data.name = 'Post Malone'
session.commit()

# DELETE
customer_data = session.query(Customer).get('user02')
session.delete(customer_data)
session.commit()
