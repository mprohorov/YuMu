from sqlalchemy import create_engine
from app import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime


Base = models.Base
Base.metadata.reflect(engine, extend_existing=True)



"""
example = account(user_id=000001, email="bob@example.com", phone_number=1234567890,
                  first_name='Bob', last_name='Smith', zipcode=11374, password='password')
"""

def createAccount(email, phone, fname, lname, zip, pw):
    act = account(email = email, phone_number = phone, first_name = fname, last_name = lname,
                   zipcode = zip, password = pw)
    return act


