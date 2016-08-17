from sqlalchemy import create_engine
from app import models
from app import dbconnect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, DateTime

Base = models.Base

"""
example = account(user_id=000001, email="bob@example.com", phone_number=1234567890,
                  first_name='Bob', last_name='Smith', zipcode=11374, password='password')
"""

def createAccount(email, phone, fname, lname, zip, pw):
    act = models.account(email = email, phone_number = phone, first_name = fname, last_name = lname,
                   zipcode = zip, password = pw)
    dbconnect.session.add(act)


createAccount('asdar@re.com', "1234567890", 'Max', 'Prohorov', 11374, 'asdhasd')
dbconnect.session.commit()



