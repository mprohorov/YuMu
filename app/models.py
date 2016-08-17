from sqlalchemy import Column, Integer, String, DateTime, engine
from sqlalchemy import create_engine
from app import dbconnect
import __init__
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
Base.metadata.reflect(dbconnect.engine)

class account(Base):
    __table__ = Base.metadata.tables['account_settings']


    def is_active(self):
        return True
    def get_id(self):
        return self.email
    def is_authenticated(self):
        return self.authenticated
    def is_anonymous(self):
        return False;

class preferences(Base):
    __table__ = Base.metadata.tables['user_preferences']


@__init__.lm.user_loader
def load_user(user_id):
    return account.query.get(int(user_id))





