from app import models
from app import dbconnect

def createAccount(email, phone, fname, lname, zip, pw):
    act = models.account(email = email, phone_number = phone, first_name = fname, last_name = lname,
                   zipcode = zip, password = pw)
    dbconnect.session.add(act)
    dbconnect.session.commit()

def enterPrefs(minb, maxb, activity, radius, location):
    prefs = models.preferences(min_budget = minb, max_budget = maxb,
                               activity = activity, radius = radius, location = location)
    dbconnect.session.add(prefs)
    dbconnect.session.commit()
