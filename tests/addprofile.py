from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

#Connection key
s = "mysql+mysqldb://max:Gentech16@148.4.117.98:3306/yumu_db"
engine = create_engine(s)

#use  sqlalchemy to execute SQL commands
"""
conn = engine.connect()
result = conn.execute("SELECT * FROM yumu_db.account_settings")
"""

conn = engine.connect()

Base = declarative_base()
Base.metadata.reflect(engine)

class account(Base):
    __tablename__ = 'account_settings'

    user_id = Column(Integer, primary_key=True)
    email = Column(String)
    phone_number = Column(Integer)
    first_name = Column(String)
    last_name = Column(String)
    zipcode = Column(Integer)
    createdOn = Column(DateTime)

example = account(user_id=000001, email="bob@example.com", phone_number=1234567890,
                  first_name='Bob', last_name='Smith', zipcode=11374)
print(example.first_name, example.last_name)