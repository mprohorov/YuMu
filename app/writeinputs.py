from app import models
from app import dbconnect

# Take inputs form frontend, write them into the Database
def createAccount(email, phone, fname, lname, pw):
    act = models.account(email = email, phone_number = phone, first_name = fname, last_name = lname, password = pw)
    dbconnect.session.add(act)
    dbconnect.session.commit()

def createEvent()

def enterPrefs1(lat, long, cat):
    prefs = models.preferences(latitude=lat, longitude=long, category=cat)
    dbconnect.session.add(prefs)
    dbconnect.session.commit()

def enterPrefs2(minb, maxb, startTime, endTime):
    prefs = models.preferences(min_budget=minb, max_budget=maxb)
    dbconnect.session.add(prefs)
    times = models.times(start_time = startTime, end_time = endTime)
    dbconnect.session.add(times)
    dbconnect.session.commit()




