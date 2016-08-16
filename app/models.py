from sqlalchemy import Column, Integer, String, DateTime, engine
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

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

