from app import models
from app import dbconnect

Base = models.Base

def createAccount(email, phone, fname, lname, zip, pw):
    act = models.account(email = email, phone_number = phone, first_name = fname, last_name = lname,
                   zipcode = zip, password = pw)
    dbconnect.session.add(act)