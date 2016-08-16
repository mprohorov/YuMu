from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

#Connection key
s = "mysql+mysqldb://max:Gentech16@192.168.0.11:3306/yumu_db"
engine = create_engine(s)

#use  sqlalchemy to execute SQL commands
"""
conn = engine.connect()
result = conn.execute("SELECT * FROM yumu_db.account_settings")
"""

conn = engine.connect()

Base = declarative_base()
Base.metadata.reflect(engine, extend_existing=True)

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


"""
example = account(user_id=000001, email="bob@example.com", phone_number=1234567890,
                  first_name='Bob', last_name='Smith', zipcode=11374, password='password')
"""+
def createAccount(email, phone, fname, lname, zip, pw):
    act = account(email = email, phone_number = phone, first_name = fname, last_name = lname,
                   zipcode = zip, password = pw)
    return act

