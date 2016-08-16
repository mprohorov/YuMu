from sqlalchemy import Column, Integer, String, DateTime, engine
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class account(Base):
    __tablename__ = 'account_settings'

    user_id = Column(Integer, primary_key=True)
    email = Column(String)
    phone_number = Column(Integer)
    first_name = Column(String)
    last_name = Column(String)
    zipcode = Column(Integer)
    createdOn = Column(DateTime)