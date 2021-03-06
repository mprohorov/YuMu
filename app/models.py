from sqlalchemy import Column, Integer, String, DateTime, engine
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship

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
        return False

    preferences = relationship("preferences")


class preferences(Base):
    __table__ = Base.metadata.tables['user_preferences']



class times(Base):
    __table__ = Base.metadata.tables['preferred_times']

class event(Base):
    __table__ = Base.metadata.tables['event_proposal']
    preferences = relationship("preferences")

class friendsInvited(Base):
    __table__ = Base.metadata.tables['friends_invited']



@__init__.lm.user_loader
def load_user(user_id):
    return account.query.get(int(user_id))





